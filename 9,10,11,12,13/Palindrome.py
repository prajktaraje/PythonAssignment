def Palindrome(val):
    val = str(val)
    if val == val[::-1]:
        print("palindrome")

def main():
    val = int(input("enter no"))
    Palindrome(val)

if __name__ == "__main__":
    main()