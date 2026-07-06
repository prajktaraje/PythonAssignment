
def main():
    no1 = int(input("enter no1"))

    ret = lambda no1: "True" if no1 %5==0 else "False"
    print(ret(no1))

if __name__ == "__main__":
    main() 