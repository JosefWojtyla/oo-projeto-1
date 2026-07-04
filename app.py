import tkinter as tk

from package.cliente import Cliente
from package.produto import Produto
from package.mercado import Mercado

from persistencia.gerenciador_persistencia import GerenciadorPersistencia

class App(tk.Tk):
    def __init__(self, cliente_logado = None):
        super().__init__()

        self.cliente_logado = cliente_logado

        self.var_user = tk.StringVar(value="Usuário: Nenhum")

        self.title("Mercadinho")
        self.geometry("800x600")
        self.configure(bg="#1e1e2e")

        # dados do mercado
        self.mercado = Mercado(lista_produtos=[], lista_clientes=[])
        self.gerenciador = GerenciadorPersistencia()
        
        self.gerenciador.carregar_dados(self.mercado)

        # frame do menu principal
        self.frame_menu = tk.Frame(self, bg="#1e1e2e")
        self.frame_menu.pack(expand = True)

        tk.Label(
            self.frame_menu, textvariable = self.var_user,
            font=("Arial", 12), fg="#a6e3a1", bg="#1e1e2e"
        ).pack(pady=(0, 5))

        self.btn_deslogar = tk.Button(self.frame_menu, text="Deslogar", font=("Arial", 10), bg="#f38ba8", fg="#1e1e2e", command=self._deslogar)
        if self.cliente_logado:
            self.btn_deslogar.pack(pady=5)
        else:
            self.btn_deslogar.pack_forget()

        # titulo
        tk.Label(
            self.frame_menu,
            text = "MERCADINHO",
            font = ("Arial", 24, "bold"),
            fg = "#cdd6f4",
            bg = "#1e1e2e",
        ).pack(pady = (0, 30))

        # lista botoes menu
        botoes_menu = [
            ("Cadastrar Produto", self.abrir_cadastro_produto),
            ("Cadastrar Cliente", self.abrir_cadastro_cliente),
            ("Listar Produto", self.abrir_lista_produtos),
            ("Listar Cliente", self.abrir_lista_clientes),
            ("Realizar Compras (login)", self.abrir_venda),
            ("Visualizar Carrinho", self.abrir_carrinho),
            ("Finalizar Compras", self.finalizar_compra)
        ]

        # criar botoes
        for texto, comando in botoes_menu:
            tk.Button(
                self.frame_menu,
                text = texto,
                command = comando,
                width = 20,
                font = ("Arial", 14),
                bg = "#45475a",
                fg = "#cdd6f4",
                activebackground = "#585b70",
                activeforeground = "#cdd6f4"
            ).pack(pady = 5)

    def abrir_cadastro_produto(self):
        print("Abrindo cadastro de produto...")

        frame = tk.Frame(self, bg = "#1e1e2e")

        # titulo
        tk.Label(
            frame, text = "Cadastrar Produto",
            font = ("Arial", 24, "bold"),
            fg = "#cdd6f4",
            bg = "#1e1e2e",
        ).pack(pady = (0, 20))

#-----------------------------------------------------------------------------
#        Campos da tela de cadastro de produto:
#-----------------------------------------------------------------------------
        # Campo: Nome do Produto
        tk.Label(frame, text="Nome:", font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e").pack()
        entrada_nome = tk.Entry(frame, font=("Arial", 12), width=30)
        entrada_nome.pack(pady=(0, 10))

        # Campo: Preço
        tk.Label(frame, text="Preço:", font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e").pack()
        entrada_preco = tk.Entry(frame, font=("Arial", 12), width=30)
        entrada_preco.pack(pady=(0, 10))

        # Campo: Estoque
        tk.Label(frame, text="Quantidade Estoque:", font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e").pack()
        entrada_estoque = tk.Entry(frame, font=("Arial", 12), width=30)
        entrada_estoque.pack(pady=(0, 10))

        # Label de erro (começa vazio, aparece vermelho se algo der errado)
        label_erro = tk.Label(frame, text="", font=("Arial", 11), fg="#f38ba8", bg="#1e1e2e")
        label_erro.pack()

        # botao cadastrar
        tk.Button(
            frame, text="Cadastrar", font=("Arial", 13),
            bg="#a6e3a1", fg="#1e1e2e",    # cor verde para o botao
            width=20,
            command=lambda: self._cadastrar_produtos(entrada_nome, entrada_preco, entrada_estoque, label_erro, frame)
        ).pack(pady=10)

        # botao voltar
        tk.Button(
            frame, text="← Voltar", font=("Arial", 11),
            bg="#313244", fg="#cdd6f4",
            command=lambda: self.trocar_tela(frame, self.frame_menu)  # volta pro menu
        ).pack()

        self.trocar_tela(self.frame_menu, frame)

    def _cadastrar_produtos(self, entrada_nome, entrada_preco, entrada_estoque, label_erro, frame):
        nome = entrada_nome.get()
        preco = entrada_preco.get()
        estoque = entrada_estoque.get()
        
        # validação
        if not nome or not preco or not estoque:
            label_erro.config(text="Preencha todos os campos", fg="#f38ba8")
            return
        
        try:
            preco_float = float(preco)
            estoque_int = int(estoque)
        
        except ValueError:
            label_erro.config(text="Preço ou estoque inválido",fg="#f38ba8")
            return

        # valores positivos
        if preco_float <= 0 or estoque_int <= 0:
            label_erro.config(text = "Valores devem ser maiores que zero", fg="#f38ba8")
            return 
        
        novo_produto = Produto(1, nome, preco_float, estoque_int)

            
        if self.mercado.cadastrar_produto(novo_produto):
            self.gerenciador.salvar_dados(self.mercado)
            label_erro.config(text = "Produto cadastrado", fg="#a6e3a1")
            entrada_nome.delete(0, tk.END)
            entrada_preco.delete(0, tk.END)
            entrada_estoque.delete(0, tk.END)
        else:
            label_erro.config(text="Erro: Produto já cadastrado", fg="#f38ba8")

            
    def abrir_cadastro_cliente(self):
        print("Abrindo cadastro de cliente...")
    
        frame = tk.Frame(self, bg = "#1e1e2e")

        # titulo
        tk.Label(
            frame, text = "Cadastrar Cliente",
            font = ("Arial", 24, "bold"),
            fg = "#cdd6f4",
            bg = "#1e1e2e",
        ).pack(pady = (0, 20))
#-----------------------------------------------------------------------------
#        Campos da tela de cadastro de cliente:
#-----------------------------------------------------------------------------
        # nome
        tk.Label(frame, text="Nome:", font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e").pack()
        entrada_nome = tk.Entry(frame, font=("Arial", 12), width=30)
        entrada_nome.pack(pady=(0, 10))

        # cpf
        tk.Label(frame, text="CPF:", font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e").pack()
        entrada_cpf = tk.Entry(frame, font=("Arial", 12), width=30)
        entrada_cpf.pack(pady=(0, 10))

        # email
        tk.Label(frame, text="Email:", font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e").pack()
        entrada_email = tk.Entry(frame, font=("Arial", 12), width=30)
        entrada_email.pack(pady=(0, 10))
        
        # idade
        tk.Label(frame, text="Idade:", font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e").pack()
        entrada_idade = tk.Entry(frame, font=("Arial", 12), width=30)
        entrada_idade.pack(pady=(0, 10))

        # Label de erro (começa vazio, aparece vermelho se algo der errado)
        label_erro = tk.Label(frame, text="", font=("Arial", 11), fg="#f38ba8", bg="#1e1e2e")
        label_erro.pack()
        
        # botao cadastrar
        tk.Button(
            frame, text="Cadastrar", font=("Arial", 13),
            bg="#a6e3a1", fg="#1e1e2e",    # cor verde para o botao
            width=20,
            command=lambda: self._cadastrar_cliente(entrada_nome, entrada_cpf, entrada_email, entrada_idade, label_erro, frame)
        ).pack(pady=10)

        # botao voltar
        tk.Button(
            frame, text="← Voltar", font=("Arial", 11),
            bg="#313244", fg="#cdd6f4",
            command=lambda: self.trocar_tela(frame, self.frame_menu)  # volta pro menu
        ).pack()

        self.trocar_tela(self.frame_menu, frame)

    def _cadastrar_cliente(self, entrada_nome, entrada_cpf, entrada_email, entrada_idade, label_erro, frame):
        nome = entrada_nome.get()
        cpf = entrada_cpf.get()
        email = entrada_email.get()
        idade = entrada_idade.get()
        
        # validação
        if not nome or not cpf or not email or not idade:
            label_erro.config(text="Preencha todos os campos", fg="#f38ba8")
            return
        
        try:
            idade_int = int(idade)
        
        except ValueError:
            label_erro.config(text="Idade inválida",fg="#f38ba8")
            return

        # valores positivos
        if idade_int <= 0:
            label_erro.config(text = "Idade deve ser maior que zero", fg="#f38ba8")
            return 
        
        novo_cliente = Cliente(1, nome, cpf, email, idade_int)
            
        if self.mercado.cadastrar_cliente(novo_cliente):
            self.gerenciador.salvar_dados(self.mercado)
            label_erro.config(text = "Cliente cadastrado", fg="#a6e3a1")
            entrada_nome.delete(0, tk.END)
            entrada_cpf.delete(0, tk.END)
            entrada_email.delete(0, tk.END)
            entrada_idade.delete(0, tk.END)
        else:
            label_erro.config(text="Erro: Cliente já cadastrado", fg="#f38ba8")

    def abrir_lista_produtos(self):
        print("Abrindo lista de produtos...")

        frame = tk.Frame(self, bg="#1e1e2e")

        tk.Label(
            frame, text="Produtos disponiveis",
            font=("Arial", 20, "bold"), fg="#cdd6f4", bg="#1e1e2e"
        ).pack(pady=(0, 20)) 

# - - - LISTA DE PRODUTOS - - -
        if not self.mercado.lista_produtos:
            label_vazio = tk.Label(
                frame, text = "Nenhum produto cadastrado",
                font=("Arial", 12), fg="#a6adc8", bg="#1e1e2e"
            )
            label_vazio.pack(pady=20)

        else:
            for prod in self.mercado.lista_produtos:
                # frame pra cada produto
                frame_prod = tk.Frame(frame, bg="#1e1e2e")
                frame_prod.pack(pady=5)

                # nome
                tk.Label(frame_prod, text=f"Nome: {prod.nome}", font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e").pack()

                # quantidade e preço
                tk.Label(frame_prod, text=f"Quantidade: {prod.get_estoque()} | Preço: {prod.get_preco()}", font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e").pack()

        

        # botao voltar
        tk.Button(
            frame, text="← Voltar", font=("Arial", 11),
            bg="#313244", fg="#cdd6f4",
            command=lambda: self.trocar_tela(frame, self.frame_menu)
        ).pack()
        self.trocar_tela(self.frame_menu, frame)


    def abrir_lista_clientes(self):
        print("Abrindo lista de clientes...")

        frame = tk.Frame(self, bg="#1e1e2e")

        tk.Label(
            frame, text="Clientes cadastrados",
            font=("Arial", 20, "bold"), fg="#cdd6f4", bg="#1e1e2e"
        ).pack(pady=(0, 20)) 

# - - - LISTA DE CLIENTES - - - 
        if not self.mercado.lista_clientes:
            label_vazio = tk.Label(
                frame, text = "Nenhum cliente cadastrado",
                font=("Arial", 12), fg="#a6adc8", bg="#1e1e2e"
            )
            label_vazio.pack(pady=20)
        
        else:
            for cliente in self.mercado.lista_clientes:
                # frame pra cada cliente
                frame_cliente = tk.Frame(frame, bg="#1e1e2e")
                frame_cliente.pack(pady=5)

                # nome
                tk.Label(frame_cliente, text=f"Nome: {cliente.get_nome()}", font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e").pack()

                # cpf, email, idade
                tk.Label(frame_cliente, text=f"CPF: {cliente.get_cpf()} | Email: {cliente.email} | Idade: {cliente.idade}" , font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e").pack()

        # botao voltar
        tk.Button(
            frame, text="← Voltar", font=("Arial", 11),
            bg="#313244", fg="#cdd6f4",
            command=lambda: self.trocar_tela(frame, self.frame_menu)
        ).pack()
        self.trocar_tela(self.frame_menu, frame)

    def abrir_venda(self):
        print("Abrindo venda...")
        
        frame = tk.Frame(self, bg="#1e1e2e")

        tk.Label(
            frame, text = "Carrinho"
        )


        if self.cliente_logado is None:
            tk.Label(
                frame, text = "Você precisa estar logado para realizar compras",
                font = ("Arial", 14), fg = "#f38ba8", bg = "#1e1e2e"
            ).pack(pady=20)
            
            tk.Label(
                frame, text = "Digite o CPF", font = ("Arial", 14), fg = "#cdd6f4", bg = "#1e1e2e"
            ).pack(pady=10)

            cpf_login = tk.Entry(frame, font = ("Arial", 14), fg = "#cdd6f4", bg = "#1e1e2e")
            cpf_login.pack(pady=10)

            tk.Button(
                frame, text="Login", font = ("Arial", 14), bg = "#a6e3a1", fg = "#1e1e2e", command = lambda: self._login(cpf_login, label_erro, frame)
            ).pack(pady=10)

            label_erro = tk.Label(frame, text = "", font = ("Arial", 14), fg = "#f38ba8", bg = "#1e1e2e")
            label_erro.pack(pady=10)



            tk.Button(
                frame, text="Voltar", font = ("Arial", 14), bg = "#313244", fg = "#cdd6f4", command = lambda: self.trocar_tela(frame, self.frame_menu)
            ).pack(pady=10)

            self.trocar_tela(self.frame_menu, frame)
            return 
        
        else:
            # - - - Lista de Produtos
            if not self.mercado.lista_produtos:
                label_vazio = tk.Label(
                    frame, text = "Nenhum produto cadastrado",
                    font=("Arial", 12), fg="#a6adc8", bg="#1e1e2e"
                )
                label_vazio.pack(pady=20)

            else:
                for prod in self.mercado.lista_produtos:
                    # frame pra cada produto
                    frame_prod = tk.Frame(frame, bg="#1e1e2e")
                    frame_prod.pack(pady=5)

                    # nome
                    tk.Label(frame_prod, text=f"Nome: {prod.nome}", font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e").pack()

                    # quantidade e preço
                    tk.Label(frame_prod, text=f"Quantidade: {prod.get_estoque()} | Preço: {prod.get_preco()}", font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e").pack()

                    # botao adicionar ao carrinho e entrada de quantidade
                    frame_add = tk.Frame(frame_prod, bg="#1e1e2e")
                    frame_add.pack(pady=5)
                    
                    tk.Label(frame_add, text="Qtd:", font=("Arial", 11), fg="#cdd6f4", bg="#1e1e2e").pack(side=tk.LEFT)
                    entrada_qtd = tk.Entry(frame_add, font=("Arial", 11), width=5)
                    entrada_qtd.pack(side=tk.LEFT, padx=5)
                    
                    label_msg_prod = tk.Label(frame_add, text="", font=("Arial", 10), bg="#1e1e2e")
                    label_msg_prod.pack(side=tk.RIGHT)

                    tk.Button(
                        frame_prod, text="Adicionar ao carrinho", font=("Arial", 11), bg = "#a6e3a1", fg = "#1e1e2e", 
                        command = lambda p=prod, e=entrada_qtd, l=label_msg_prod: self._adicionar_ao_carrinho(p, e, l)
                    ).pack(pady=5)

        # botao voltar
        tk.Button(
            frame, text="← Voltar", font=("Arial", 11),
            bg="#313244", fg="#cdd6f4",
            command=lambda: self.trocar_tela(frame, self.frame_menu)
        ).pack()
        self.trocar_tela(self.frame_menu, frame)


    def _login(self, cpf_login, label_erro, frame):
        
        for clie in self.mercado.lista_clientes:
                if clie.get_cpf() == cpf_login.get():
                    self.cliente_logado = clie
                    self.var_user.set(f"Usuário: {clie.get_nome()}")
                    self.btn_deslogar.pack(pady=5)
                    tk.Label(
                        frame, text = "Login realizado com sucesso", font = ("Arial", 14), fg = "#a6e3a1", bg = "#1e1e2e"
                    ).pack(pady=10)
                    self.trocar_tela(frame, self.frame_menu)
                    return 

        else:
            label_erro.config(text="Cliente não encontrado", fg="#f38ba8")
            return

    def _deslogar(self):
        self.cliente_logado = None
        self.var_user.set("Usuário: Nenhum")
        self.btn_deslogar.pack_forget()
        
    def _adicionar_ao_carrinho(self, produto, entrada_qtd, label_msg):
        qtd_str = entrada_qtd.get()
        if not qtd_str.isdigit():
            label_msg.config(text="Qtd inválida!", fg="#f38ba8")
            return
        qtd = int(qtd_str)
        if qtd <= 0:
            label_msg.config(text="Qtd deve ser > 0", fg="#f38ba8")
            return
        if qtd > produto.get_estoque():
            label_msg.config(text="Estoque insuficiente", fg="#f38ba8")
            return
        
        self.cliente_logado.carrinho.adicionar_carrinho(produto, qtd)
        label_msg.config(text=f"Adicionado {qtd}x", fg="#a6e3a1")
        entrada_qtd.delete(0, tk.END)

    def abrir_carrinho(self):
        print("Abrindo carrinho...")
        frame = tk.Frame(self, bg="#1e1e2e")
        tk.Label(frame, text="Seu Carrinho", font=("Arial", 20, "bold"), fg="#cdd6f4", bg="#1e1e2e").pack(pady=20)
        
        if self.cliente_logado is None:
            tk.Label(frame, text="Faça login primeiro!", font=("Arial", 14), fg="#f38ba8", bg="#1e1e2e").pack(pady=20)
        elif not self.cliente_logado.carrinho.lista_itens:
            tk.Label(frame, text="Carrinho vazio.", font=("Arial", 14), fg="#a6adc8", bg="#1e1e2e").pack(pady=20)
        else:
            for prod, qtd in self.cliente_logado.carrinho.lista_itens:
                subtotal = prod.get_preco() * qtd
                tk.Label(frame, text=f"{prod.nome} | Qtd: {qtd} | Subtotal: R$ {subtotal:.2f}", font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e").pack(pady=2)
            
            total = self.cliente_logado.carrinho.calcular_total()
            tk.Label(frame, text=f"TOTAL: R$ {total:.2f}", font=("Arial", 16, "bold"), fg="#a6e3a1", bg="#1e1e2e").pack(pady=20)
            
            tk.Button(frame, text="Finalizar Compra", font=("Arial", 14, "bold"), bg="#a6e3a1", fg="#1e1e2e", command=lambda: self.finalizar_compra(frame)).pack(pady=10)

        tk.Button(frame, text="← Voltar", font=("Arial", 11), bg="#313244", fg="#cdd6f4", command=lambda: self.trocar_tela(frame, self.frame_menu)).pack(pady=10)
        self.trocar_tela(self.frame_menu, frame)


    def finalizar_compra(self, frame_anterior=None):
        print("Abrindo finalização de compras...")
        if self.cliente_logado is None or not self.cliente_logado.carrinho.lista_itens:
            return
            
        frame = tk.Frame(self, bg="#1e1e2e")
        
        for prod, qtd in self.cliente_logado.carrinho.lista_itens:
            prod.descontar_estoque(qtd)
        
        self.cliente_logado.carrinho.limpar_carrinho()
        self.gerenciador.salvar_dados(self.mercado)
        
        tk.Label(frame, text="Compra Finalizada com Sucesso!", font=("Arial", 16, "bold"), fg="#a6e3a1", bg="#1e1e2e").pack(pady=20)
        
        tk.Button(frame, text="Voltar ao Menu", font=("Arial", 12), bg="#313244", fg="#cdd6f4", command=lambda: self.trocar_tela(frame, self.frame_menu)).pack(pady=20)
        
        frame_origem = frame_anterior if frame_anterior else self.frame_menu
        self.trocar_tela(frame_origem, frame)


    def trocar_tela(self, frame_atual, frame_novo):
        if frame_atual == self.frame_menu:
            frame_atual.pack_forget()
        else:
            frame_atual.destroy()
        
        frame_novo.pack(expand = True)

if __name__ == "__main__":
    app = App()
    app.mainloop()