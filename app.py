import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mercadinho")
        self.geometry("800x600")
        self.configure(bg="#1e1e2e")

        # frame do menu principal
        self.frame_menu = tk.Frame(self, bg="#1e1e2e")
        self.frame_menu.pack(expand = True)

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
            command=lambda: print(f"Nome: {entrada_nome.get()}, Preço: {entrada_preco.get()}, Estoque: {entrada_estoque.get()}")
        ).pack(pady=10)

        # botao voltar
        tk.Button(
            frame, text="← Voltar", font=("Arial", 11),
            bg="#313244", fg="#cdd6f4",
            command=lambda: self.trocar_tela(frame, self.frame_menu)  # volta pro menu
        ).pack()

        self.trocar_tela(self.frame_menu, frame)

            
    def abrir_cadastro_cliente(self):
        print("Abrindo cadastro de cliente...")

    def abrir_lista_produtos(self):
        print("Abrindo lista de produtos...")

    def abrir_lista_clientes(self):
        print("Abrindo lista de clientes...")

    def abrir_venda(self):
        print("Abrindo venda...")

    def abrir_historico_vendas(self):
        print("Abrindo histórico de vendas...")

        
    def trocar_tela(self, frame_atual, frame_novo):
        frame_atual.pack_forget()
        frame_novo.pack(expand = True)

if __name__ == "__main__":
    app = App()
    app.mainloop()