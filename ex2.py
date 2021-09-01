import math


def main():
    def calcular_quantidade_inimigos(value):
        convertido = value / 100
        resultado = math.ceil(math.log(1 - convertido) / math.log(1 - chance))
        return resultado

    denominador = int(input("Qual a probabilidade do item ser obtido? Uma em: "))
    inimigos_derrotados = int(input("Quantas vezes você derrotou o inimigo para tentar conseguir o item? "))

    chance = 1 / denominador
    probabilidade = 1 - ((1 - chance) ** inimigos_derrotados)

    print("Após você eliminar {} inimigo(s), a chance de você dropar o item será de aproximadamente {:.2f}%."
          .format(inimigos_derrotados, probabilidade * 100))

    # IMPRIMINDO RESULTADO
    trinta_porcento = calcular_quantidade_inimigos(30)
    print("Para você ter 30% de chances de conseguir o item você deverá matar {} inimigos no jogo."
          .format(trinta_porcento))

    quarenta_porcento = calcular_quantidade_inimigos(40)
    print("Para você ter 40% de chances de conseguir o item você deverá matar {} inimigos no jogo."
          .format(quarenta_porcento))

    cinquenta_porcento = calcular_quantidade_inimigos(50)
    print("Para você ter 50% de chances de conseguir o item você deverá matar {} inimigos no jogo."
          .format(cinquenta_porcento))

    sessenta_porcento = calcular_quantidade_inimigos(60)
    print("Para você ter 60% de chances de conseguir o item você deverá matar {} inimigos no jogo."
          .format(sessenta_porcento))

    setenta_porcento = calcular_quantidade_inimigos(70)
    print("Para você ter 70% de chances de conseguir o item você deverá matar {} inimigos no jogo."
          .format(setenta_porcento))

    oitenta_porcento = calcular_quantidade_inimigos(80)
    print("Para você ter 80% de chances de conseguir o item você deverá matar {} inimigos no jogo."
          .format(oitenta_porcento))

    noventa_porcento = calcular_quantidade_inimigos(90)
    print("Para você ter 90% de chances de conseguir o item você deverá matar {} inimigos no jogo."
          .format(noventa_porcento))

    noventa_cinco_porcento = calcular_quantidade_inimigos(95)
    print("Para você ter 95% de chances de conseguir o item você deverá matar {} inimigos no jogo."
          .format(noventa_cinco_porcento))

    noventa_sete_porcento = calcular_quantidade_inimigos(97)
    print("Para você ter 97% de chances de conseguir o item você deverá matar {} inimigos no jogo."
          .format(noventa_sete_porcento))


if(__name__ == "__main__"):
    main()
