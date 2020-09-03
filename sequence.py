n = int(input("Enter the length of the sequence: ")) # Do not change this line
n = n - 4
runs = 0
int1,int2,int3,newInt = 1,2,3,0
print(int1)
print(int2)
print(int3)
while runs <= n:
    newInt = int1 + int2 + int3
    print(newInt)
    int1 = int2
    int2 = int3
    int3 = newInt
    runs = runs + 1
