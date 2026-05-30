# Projeto inicial de Mercadinho (POO-1)

Este é um sistema de simulação de um Mercadinho desenvolvido em **Python**, construído puramente no terminal, focando nos conceitos de **Programação Orientada a Objetos (POO)**. 

O projeto aplica na prática conceitos como Classes, Objetos, Herança, Encapsulamento e relacionamentos entre classes (Cliente, Produto, Carrinho e Mercado).

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

3. Execute o arquivo principal:
   ```bash
   python main.py
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

---

## Estrutura do Projeto

O sistema foi estruturado da seguinte maneira para facilitar a manutenção e leitura:
* `main.py`: Ponto de entrada do sistema contendo a interface de usuário via Terminal.
* `package/`: Pacote contendo as regras de negócio e modelagem.
  * `mercado.py`: Gerenciamento geral das listas de clientes e produtos.
  * `pessoa.py` e `cliente.py`: Representação dos usuários do sistema com Herança.
  * `produto.py`: Representação dos itens do mercado.
  * `carrinho.py`: Classe responsável por calcular o subtotal e agregar itens de uma compra.

---
*Desenvolvido para a Entrega 1 da disciplina de Orientação a Objetos.*
