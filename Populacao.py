from ast import In
from typing import List
from Individuo import Individuo
from random import choice, randint
from util import NUM_BITS, NUM_INDIVIDUOS


class Populacao:
    ## CONSTANTES
    
    TAXA_MUTACAO = 1
    TAXA_CROSSOVER = 60
    ##

    elite:Individuo
    populacao:List[Individuo]


    def __init__(self) -> None:
        self.individuos: List[Individuo] = [Individuo(numBits=NUM_BITS) for i in range(NUM_INDIVIDUOS)]
        self.elite = Individuo(NUM_BITS, self.GetIndividuoElite().bits)
        

    def GetIndividuoElite(self) -> Individuo:
        
        melhorIndiv = self.individuos[0]

        for individuo in self.individuos[1:]:
            if individuo.fitness <= melhorIndiv.fitness:
                melhorIndiv = individuo

        return melhorIndiv

    def SetIndividuoElite(self)->None:
        novoElite = self.GetIndividuoElite()

        if novoElite.fitness <= self.elite.fitness:
            self.elite = Individuo(NUM_BITS, novoElite.bits)


    def SelecionarPorTorneio(self)->List[Individuo]:

        indivSelecionados:List[Individuo] = []

        for i in range(NUM_INDIVIDUOS):
            primeiroIndividuo = choice(self.individuos)
            segundoIndividuo = choice(self.individuos)

            indivSelecionados.append(primeiroIndividuo if primeiroIndividuo.fitness <= segundoIndividuo.fitness else segundoIndividuo)

        self.individuos = indivSelecionados

        self.GetIndividuoElite()

    def FazerCrossover(self)->None:

        individuosFilhos:List[Individuo] = []

        while len(individuosFilhos) != NUM_INDIVIDUOS:
            taxaCrossover = randint(0,100)

            primeiroIndividuo:Individuo = choice(self.individuos)
            segundoIndividuo:Individuo = choice(self.individuos)

            if taxaCrossover <= self.TAXA_CROSSOVER:

                posicaoCorte = randint(1, NUM_BITS - 2)

                novosBitsPrimeiro = primeiroIndividuo.bits[:posicaoCorte] + segundoIndividuo.bits[posicaoCorte:]
                novosBitsSegundo = segundoIndividuo.bits[:posicaoCorte] + primeiroIndividuo.bits[posicaoCorte:]

                individuosFilhos.append(Individuo(NUM_BITS, novosBitsPrimeiro))
                individuosFilhos.append(Individuo(NUM_BITS, novosBitsSegundo))
            else:
                individuosFilhos.append(primeiroIndividuo)
                individuosFilhos.append(segundoIndividuo)
        
        self.individuos = individuosFilhos

        self.SetIndividuoElite()

    def MutarBit(self, bit: str):
        return ("0" if bit == "1" else "1") if randint(1, 100) <= self.TAXA_MUTACAO else bit

    def AplicarMutacao(self):
        for individuo in self.individuos:
            novosBitsIndividuo = "".join([self.MutarBit(bit) for bit in individuo.bits])

            individuo.bits = novosBitsIndividuo

        self.SetIndividuoElite()



