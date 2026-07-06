def Grade(r):
    if r >=75:
        print("Distinction")
    elif r>=60:
        print("first class")
    elif r>=50:
        print("second class")
    elif r<50:
        print("fail")

def main():
    r = int(input("enter radius no"))
    Grade(r)

if __name__ == "__main__":
    main()