def Fact(val):
    sum = 1
    for i in range(1,val+1):
        sum = sum * i
    print(sum)

def main():
    val = int(input("enter no"))
    Fact(val)

if __name__ == "__main__":
    main()