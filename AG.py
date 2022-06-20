from typing import List
from Populacao  import Populacao
from Individuo import Individuo
from matplotlib import pyplot
from util import NUM_INDIVIDUOS, NUM_BITS, OUTPUT_PATH, GerarPastaSaida, NUM_EXECUCOES, GERACOES

def main():
    melhores = [] 

    GerarPastaSaida()

    melhorX = {geracao: None for geracao in GERACOES}

    for exec in range(1, NUM_EXECUCOES + 1):

        melhores.append({geracao: [] for geracao in GERACOES})

        for totalGeracoes in GERACOES:

            arq = open(f"{OUTPUT_PATH}/{NUM_INDIVIDUOS}i_{totalGeracoes}g_{exec}exec.csv", "wt")

            populacao = Populacao()

            for i in range(totalGeracoes):
                populacao.SelecionarPorTorneio()
                populacao.FazerCrossover()
                populacao.AplicarMutacao()

                melhor = Individuo(NUM_BITS, populacao.elite.bits)

                if not melhorX[totalGeracoes] or melhorX[totalGeracoes][0].fitness > melhor.fitness:
                    melhorX[totalGeracoes] = (melhor, exec)

                arq.write(f"{i+1};{melhor}\n")
                melhores[-1][totalGeracoes].append(melhor.xNormalizado)
            arq.close()

    xNormSoma = {geracao: [0] * geracao for geracao in GERACOES}

    for melhorExec in melhores:
        for geracao in GERACOES:
            for i in range(geracao):
                xNormSoma[geracao][i] += melhorExec[geracao][i]

    for qtdMaxGeracoes in GERACOES:
        media = []

        for i in range(qtdMaxGeracoes):
            media.append(xNormSoma[qtdMaxGeracoes][i] / NUM_EXECUCOES)

        valEixoX = [i for i in range(1, qtdMaxGeracoes + 1)]

        pyplot.plot(valEixoX, media, marker='o')

        pyplot.xlabel("Número da geração")
        pyplot.ylabel("X Normalizado i-ésimo individuo")
        pyplot.xticks([x for x in range(1,qtdMaxGeracoes+1)])
        pyplot.text(1, media[-1], f"{melhorX[qtdMaxGeracoes][0].xNormalizado}", color="blue", fontsize=10)

        pyplot.title(f"Gráfico para {qtdMaxGeracoes} gerações")

        print("Melhor x para {} gerações no arquivo = {}i_{}g_{}exec.csv".format(qtdMaxGeracoes, NUM_INDIVIDUOS, qtdMaxGeracoes, melhorX[qtdMaxGeracoes][1]))

        pyplot.show()

    return 0
main()
