print("\nOBRIGADO POR ESCOLHER NOSSOS SERVIÇOS\n")
print("Escolha a baixo um método de pagamento!\n")

print("\nOpções disponiveis:\n \n1 - MB Way\n2 - Cartão de Débito\n3 - Cartão de Crédito\n")

pagamento = input("Esolha uma das opções: ")
if pagamento == "1":
    int(input("Insira o número associado ao serviço MbWay:"))
    print("\nObrigado!, a sua compra foi concluída com sucesso!\n")
if pagamento == "2":
    input("Nome do titular do cartão: ")
    int(input("Número cartão: "))
    int(input("código de seguranção: "))
    print("\nObrigado!, a sua compra foi concluída com sucesso!\n")
if pagamento == "3":
    input("Nome do titular do cartão: ")
    int(input("Número cartão: "))
    int(input("código de seguranção: "))
    print("\nObrigado!, a sua compra foi concluída com sucesso!\n")