m=int(input('please enter m: '))
n=int(input('please enter n: '))

def mul(m,n):
    for i in range(1,m+1):
        for j in range(1,n+1):
            print(i*j,end='\t')
        print()

mul(m,n)
