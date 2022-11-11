import funcs as f
import pandas as pd

def tratamento(num):
    ft = f.fatorial(num)
    fb = f.fibonacci(num)
    tratados = [ft,fb]
    return tratados

arquivoTeste = pd.DataFrame([linhas.strip().split() for linhas in open("./test.data").readlines()])


print(arquivoTeste)