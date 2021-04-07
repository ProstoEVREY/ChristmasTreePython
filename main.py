while(1):
    n = input()        #code to print out a christmas tree to a number of steps (infinite)
    if(n.lower()=="q"):
        break;
    try:
        n=int(n)
    except:
        print("Only integers!")
        continue
    for i in range(1,2*n,2):
        for k in reversed(range(n-1)):
            print(" ",end="")
        for j in range(1,i+1):
            print("*", end="")
        n-=1
        print()