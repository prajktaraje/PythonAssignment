def Perfect(r):
    sum = 0
    for i in range(1,r):
        if r%i == 0:
            sum = sum + i
    if sum == r:
        return True

def main():
    r = int(input("enter radius no"))
    f = Perfect(r)
    if f:
        print("perfect no")

if __name__ == "__main__":
    main()