def divide():
    try:
        num = int(input("Give num: "))
        den = int(input("Give den: "))
        result = num/den
        print(num, "/", den, "=", result)
    except ValueError:
        print("must be an int")
        divide()
    except ZeroDivisionError:
        print("can't divide by 0")
        divide()
    except Exception as ex:
        print("Unknown Error")
        print(ex)


def main():
    divide()

main()
