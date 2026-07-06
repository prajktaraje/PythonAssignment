def Even(val):
    for i in range(1,val+1):
        if i%2 != 0:
            print(i)

def main():
    val = int(input("enter no"))
    Even(val)

if __name__ == "__main__":
    main()