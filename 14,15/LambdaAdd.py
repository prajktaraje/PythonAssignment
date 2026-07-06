
def main():
    no1 = int(input("enter no1"))
    no2 = int(input("enter no2"))

    ret = lambda no1,no2: no1 + no2
    print(ret(no1,no2))

if __name__ == "__main__":
    main() 