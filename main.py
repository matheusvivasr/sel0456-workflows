import funcs as f
import pandas as pd

def tratamento(num):
    #simplifica o cálculo de cada linha.
    ft = f.fatorial(num)
    fb = f.fibonacci(num)
    return [int(num),ft,fb]

def comparar(esse:(pd.DataFrame), aquele:(pd.DataFrame)):
    # Compara os dados e devolve uma lista com 
    # os números para os quais os valores divergiram.
    wLines = []     
    if not esse.equals(aquele):
        bino = esse.eq(aquele)
        for i in range(bino.shape[0]):
            if not (bino.iloc[i].iat[1] and bino.iloc[i].iat[2]): wLines.append(esse["#"].iat[i])
    return wLines


fileName = "./test.data"    #Arquivo a ser testado.


# Transforma a entrada em pd.DataFrame.
inputFile = pd.DataFrame([linhas.strip().split() for linhas in open(fileName).readlines()])
if inputFile.loc[0].at[0].isnumeric():
    testFile = pd.DataFrame(inputFile.values,columns=["#","fact","fib"])
else:
    testFile = pd.DataFrame(inputFile[1:].values,columns=inputFile.iloc[0].values)


# Faz o arquivo de saída calculado com a funçao 'tratamento' definida acima.
outText = pd.DataFrame([tratamento(n) for n in testFile["#"].values],columns=testFile.columns.values)
with open("./outFile.data","w") as testOut:
    testOut.write(' '.join(["#","fact","fib"]))
    testOut.write('\n')
    for i in range(outText.shape[0]):   #escreve o arquivo de acordo com o modelo esperado.
        for j in range(outText.shape[1]):
            testOut.write(str(outText.iloc[i].values[j]))
            if j < outText.shape[1]-1: testOut.write(' ')
        if i < outText.shape[0]-1: testOut.write('\n')


#lê o arquivo de saída feito acima para poder comparar com a entrada a ser testada.
outputFile = pd.DataFrame([linhas.strip().split() for linhas in open("./outFile.data").readlines()])
outFile = pd.DataFrame(outputFile[1:].values,columns=outputFile.iloc[0].values)

linhas_erradas = comparar(testFile,outFile) #funçao definida no começo do programa.

if linhas_erradas==[]:print("Programa sem erros")
else:print("Os valores foram errados para as linhas: ",int(", ".join(linhas_erradas)))