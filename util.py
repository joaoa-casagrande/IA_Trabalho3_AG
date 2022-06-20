import os
import glob
import time

## CONSTANTES
NUM_BITS = 16
MAX_VAL = 20
MIN_VAL = -20
NUM_INDIVIDUOS = 10
NUM_EXECUCOES = 10
GERACOES = [10, 20]

FULL_PATH = os.path.realpath(__file__)
OUTPUT_PATH = os.path.dirname(FULL_PATH)+"\\output\\"
##

## FUNCOES
def LimparPastaSaida():
    files = glob.glob(OUTPUT_PATH+"*")
    for f in files:
        os.remove(f)

def GerarPastaSaida():
    if os.path.exists(OUTPUT_PATH): LimparPastaSaida()
    else: os.makedirs(OUTPUT_PATH)
    time.sleep(1)

##