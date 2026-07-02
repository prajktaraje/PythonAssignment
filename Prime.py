def Prime(val):
    for i in range(2,val):
        if val%i==0:
            break
    else:
        print("Prime Number")


def main():
    val = int(input("enter no"))
    Prime(val)

if __name__ == "__main__":
    main()