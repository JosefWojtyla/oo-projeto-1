# Projeto inicial de Mercadinho (POO-1)

Este é um sistema de simulação de um Mercadinho desenvolvido em **Python**, construído puramente no terminal, focando nos conceitos de **Programação Orientada a Objetos (POO)** e **Persistência de Dados**. 

O projeto aplica na prática conceitos como Classes, Objetos, Herança, Encapsulamento, relacionamentos entre classes (Cliente, Produto, Carrinho e Mercado) e manipulação de arquivos JSON.

---

## Pré-requisitos

Para rodar este projeto na sua máquina, você precisa ter apenas o **Python 3.x** instalado. 

Para verificar se você já tem o Python instalado, abra o seu terminal (Prompt de Comando ou PowerShell no Windows, Terminal no Mac/Linux) e digite:
```bash
python --version
```
*(Se não tiver instalado, baixe gratuitamente em [python.org](https://www.python.org/downloads/))*

---

## Como executar o projeto

1. **Clone este repositório** para a sua máquina local:
   ```bash
   git clone https://github.com/JosefWojtyla/oo-projeto-1.git
   ```

2. Acesse a pasta do projeto através do terminal:
   ```bash
   cd oo-projeto-1
   ```

3. Execute o sistema:

   Para rodar no modo Terminal (linha de comando):
   ```bash
   python main.py
   ```

   Para rodar com a Interface Gráfica (novo):
   ```bash
   python app.py
   ```

---

## Guia de Testes (Como usar o sistema)

Para testar todas as funcionalidades desenvolvidas nesta primeira entrega, siga este fluxo no menu principal:

1. **Cadastrar Produto (`Opção 1`)**:
   * Adicione alguns produtos ao estoque (ex: nome: Maçã, preço: 2.50, Quantidade: 50).
2. **Listar Produtos (`Opção 3`)**:
   * Verifique se o produto que você cadastrou aparece na lista com o estoque correto.
3. **Cadastrar Cliente (`Opção 2`)**:
   * Crie o seu perfil preenchendo os dados solicitados. **Guarde bem o seu CPF**, ele é a sua chave de login.
4. **Login e Carrinho (`Opção 4 - Fazer Login para Comprar`)**:
   * Digite seu CPF para entrar na sua conta.
   * O menu vai mudar para o "Modo Compra".
   * Escolha a `Opção 4` novamente para adicionar itens ao seu carrinho de compras digitando o nome exato do produto.
5. **Finalizar Compra (`Opção 5`)**:
   * Veja o extrato completo do seu carrinho e confirme o pagamento.
6. **Deslogar (`Opção 6`)**:
   * Saia da conta para permitir que outro visitante utilize o terminal do mercado.
7. **Testar Persistência (`Opção 0`)**:
   * Saia do sistema e inicie novamente (`python main.py`). Suas contas, produtos e itens no carrinho continuarão lá, salvos no arquivo JSON!

---

## Estrutura do Projeto

O sistema foi estruturado da seguinte maneira para facilitar a manutenção e leitura:
* `main.py`: Ponto de entrada do sistema contendo a interface de usuário via Terminal.
* `app.py`: Ponto de entrada do sistema contendo a Interface Gráfica nova.
* `package/`: Pacote contendo as regras de negócio e modelagem.
  * `mercado.py`: Gerenciamento geral das listas de clientes e produtos.
  * `pessoa.py` e `cliente.py`: Representação dos usuários do sistema com Herança.
  * `produto.py`: Representação dos itens do mercado.
  * `carrinho.py`: Classe responsável por calcular o subtotal e agregar itens de uma compra.
* `persistencia/`:
  * `gerenciador_persistencia.py`: Classe responsável por salvar (serializar) e carregar (desserializar) o estado do mercado em formato JSON.
  * `persistencia.json`: Banco de dados em formato de texto onde as informações repousam enquanto o sistema está desligado.

---
*Desenvolvido para a disciplina de Orientação a Objetos.*
