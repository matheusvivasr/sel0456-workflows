def fatorial(n):
    n = int(n)
    if n == 1:
        return n
    else:
        return n*fatorial(n-1)

def fibonacci(n):
    n = int(n)
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#           wLines = esse["#"].iat[i] for i in range(bino.shape[0]) if not (bino.iloc[i].iat[1] and bino.iloc[i].iat[2])
