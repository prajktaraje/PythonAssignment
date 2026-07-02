def Div(val):
    if val%3 == 0 and val%5==0:
        print("Divisible by 3 and 5")

def main():
    val = int(input("enter no"))
    Div(val)

if __name__ == "__main__":
    main()