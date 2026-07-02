def factor(val):
    for i in range(1,val+1):
        if val%i == 0:
            print(i)

def main():
    val = int(input("enter no"))
    factor(val)

if __name__ == "__main__":
    main()