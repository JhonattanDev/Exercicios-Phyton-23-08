def main():

    def mostrar_resultado():
        print("==================================")
        print("Banco: {} - {}".format(codigo_banco, nome_banco))
        print("Valor: {}".format(valor_despesa))
        print("Descrição: {}".format(descricao))
        print("Data do registro: {:02}/{:02}/{:04}".format(dia, mes, ano))
        print("==================================")

    pagamentos = int(input("Quantos pagamentos deseja lançar? "))

    for i in range(1, pagamentos + 1):
        print("Pagamento {} de {}.".format(i, pagamentos))
        codigo_banco = input("Insira o código do banco referente: ")
        nome_banco = input("Insira o código do banco referente: ")
        valor_despesa = input("Insira o valor da despesa: ")
        descricao = input("Referente à: ")
        dia = int(input("Insira o dia da despesa: "))
        mes = int(input("Insira o mes da despesa: "))
        ano = int(input("Insira o ano da despesa: "))
        mostrar_resultado()


if (__name__ == "__main__"):
    main()
