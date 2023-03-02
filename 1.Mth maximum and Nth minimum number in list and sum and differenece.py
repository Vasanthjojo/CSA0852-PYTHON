L = []
n = int(input("Enter number of elements in the list : "))
for i in range(0,n):
    num = int(input("Enter element : "))
    L.append(num)
print("L =",L)
M = int(input("M = "))
N = int(input("N = "))
L.sort()
print(M,"maximum number =",L[-M])
print(N,"minimum number =",L[N-1])
print("Sum =",L[-M]+L[N-1])
print("Difference =",L[-M]-L[N-1])
