def Vowel(val):
    char = val.lower()
    if char == 'a' or char=='e' or char == 'i' or char == 'o' or char=='u':
        print("Vowel")
    else:
        print("consonent")

def main():
    val = input("enter no")
    Vowel(val)

if __name__ == "__main__":
    main()