import funcs as f
import pandas as pd

def tratamento(num):
    ft = f.fatorial(num)
    fb = f.fibonacci(num)
    tratados = [ft,fb]
    return tratados

with open("test.data","r") as test:
    arquivoTeste = test.readlines()

arquivoTeste = pd.DataFrame(arquivoTeste)
print(arquivoTeste)