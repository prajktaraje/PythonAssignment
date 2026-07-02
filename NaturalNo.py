def NN(val):
    sum = 0
    for i in range(1,val+1):
        sum = sum + i
    print(sum)

def main():
    val = int(input("enter no"))
    NN(val)

if __name__ == "__main__":
    main()