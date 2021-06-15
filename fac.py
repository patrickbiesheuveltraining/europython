def faculty(n):
    if n <= 1:
        return 1
    else:
        return n * faculty(n-1)

#fac(5) = 5 * fac(4)
#fac(n) = n * fac(n-1)

def main():
    number = 5
    print(number,"! = ",faculty(number), sep="")

main()
