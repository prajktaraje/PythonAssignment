def SD(num):
    reversed_num = 0

    while num > 0:
        remainder = num % 10          # Get the last digit
        reversed_num = reversed_num  + remainder  # Move digits left and add new digit
        num = num // 10                # Remove the last digit from original number

    print(reversed_num)  


def main():
    val = int(input("enter no"))
    SD(val)

if __name__ == "__main__":
    main()