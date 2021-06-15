import re

def read_lines(file):
    with open(file) as f:
        lines = f.readlines()
    #print(lines)
    return lines

def check_if_email(line):
    #pattern = r"^\w+@\w+\.\w+$"
    pattern = r"^([a-z_]+\.)*[a-z_]+@([a-z_]+\.)+[a-z]+$"
    p = re.compile(pattern, re.IGNORECASE)
    #if p.search(line):
    #    return True
    #return False
    return p.search(line)

def main():
    print("Looking for email addresses")
    file = "regex.txt"
    addresses = read_lines(file)
    for address in addresses:
        if(check_if_email(address)):
            print("EMAIL OK!:",address)
        else:
            print("NO EMAIL!:", address)

main()
