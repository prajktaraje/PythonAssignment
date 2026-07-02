def GreaterNo(no1,no2):
    if no1>no2:
        print(no1," is greater")
    else:
        print(no2," is greater")
        

def main():
    no1,no2 = int(input("enter first no")),int(input("enter second no"))
    GreaterNo(no1,no2)

if __name__ == "__main__":
    main()