import sys

def gen_code(line):
    for char in line:
        print("+"*ord(char)+".")

def shell():
    while True:
        try:
            gen_code(input(">> "))
        except KeyboardInterrupt:
            exit()

def gen_file(filename:str):
    try:
        file=open(filename, "r+")
        string=""
        for line in file:
            string+=f"{line}\n"
        gen_code(string)
    except:
        gen_code(filename)


if __name__=='__main__':
    if len(sys.argv)<2: shell()
    else: gen_file(sys.argv[1])
