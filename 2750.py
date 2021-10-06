N = int(input())
i = 0
j = 0        
if N<1 or N>1000: 
    exit()
else:
    lista = list(range(N))
    while i <= N-1:
            lista[i] = int(input())
            i=i+1
    lista.sort()
while j<=N-1:
    print(lista[j])
    j=j+1