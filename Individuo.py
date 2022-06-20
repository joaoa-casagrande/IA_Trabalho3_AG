from random import randint
import numpy as np
from util import MIN_VAL, MAX_VAL, NUM_BITS


class Individuo:
    numBits:int
    bits:str
    __bits:str
    fitness:float
    x:int
    xNormalizado:int

    def __init__(self, numBits:int, bits:str = None) -> None:
        self.numBits = numBits
        self.bits = bits if bits else self.GerarBits()
        

    def GerarBits(self):
        return "".join([str(randint(0,1)) for i in range(self.numBits)])

    def CalcularX(self)->int:
        return int(self.__bits, 2)

    def CalcX_Normalizado(self)->int:
        return MIN_VAL + (MAX_VAL - MIN_VAL) * (self.x / (2 ** NUM_BITS - 1))

    def CalcularFitness(self)->None:
        return np.cos(self.xNormalizado)*self.xNormalizado +2


    @property
    def bits(self) -> str:
        return self.__bits

    @bits.setter
    def bits(self, valor: str):
        self.__bits = valor
        self.x = self.CalcularX()
        self.xNormalizado = self.CalcX_Normalizado()
        self.fitness = self.CalcularFitness()

    def __repr__(self):
        return f'Bits = {self.bits};X = {self.x};X_normalizado = {self.xNormalizado};Fitness = {self.fitness}'

    def __eq__(self, item):
        return item.bits == self.bits