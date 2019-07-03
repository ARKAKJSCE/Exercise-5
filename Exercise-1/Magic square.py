N = int(input("Enter a number: "))
print(N)
   
while N%2==0:
    N= int(input("We can take only odd numbers: "))
    
import numpy as np
magicsquare = np.zeros((N,N), dtype=int)

n = 1
a, b = 0, N//2

while n <= N*N:
    magicsquare[a, b] = n
    n=n+1
    Na, Nb = (a-1)%N, (b+1)%N
    if magicsquare[Na, Nb]:
        a=a+1
    else:
        a, b = Na, Nb

print(magicsquare)