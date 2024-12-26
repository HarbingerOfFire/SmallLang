import sys

def small_interpreter(code):
    counter = 0
    output = []

    for char in code:
        if char == '+':
            counter = (counter + 1) % 250
        elif char == '.':
            output.append(chr(counter))
        elif char == '/':
            counter = 0
    return ''.join(output)

def shell():
    while True:
        print(small_interpreter(input(">> ")))

def execute_file(filename:str):
    code=open(filename, "r")

    run=""
    for line in code:
        run+=line

    print(small_interpreter(run))

if __name__ == "__main__":
    if len(sys.argv) < 2: shell()
    else: execute_file(sys.argv[1])
