
def main():
    no1 = int(input("enter no1"))
    no2 = int(input("enter no2"))
    no3 = int(input("enter no2"))

    ret = lambda no1,no2,no3: max(no1,no2,no3)
    print(ret(no1,no2,no3))

if __name__ == "__main__":
    main() 