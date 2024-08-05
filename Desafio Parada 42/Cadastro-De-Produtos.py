# Faça um programa no qual o usuário precisa cadastrar as informações de um produto: código, nome, quantidade e preço. No final o programa deve mostrar as informações cadastradas e exibir o valor total da compra. 
def main():
    # Solicitação das informações do produto ao usuário
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))

    # Calculando o valor total da compra
    valor_total = quantidade * preco

    # Exibindo as informações do produto
    print("\nInformações do Produto Cadastrado:")
    print(f"Código: {codigo}")
    print(f"Nome: {nome}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço: R${preco:.2f}")
    print(f"Valor Total da Compra: R${valor_total:.2f}")

# Executando o programa
if __name__ == "__main__":
    main()