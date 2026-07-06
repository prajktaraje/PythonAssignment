def add(no1,no2):
    return no1+no2
        
def sub(no1,no2):
    return no1-no2

def mul(no1,no2):
    return no1*no2

def div(no1,no2):
    return no1/no2

def main():
    no1,no2 = int(input("enter first no")),int(input("enter second no"))
    print(add(no1,no2))
    print(sub(no1,no2))
    print(mul(no1,no2))
    print(div(no1,no2))

if __name__ == "__main__":
    main()