import sys

def gen_code(line):
    result = []
    counter = 0
    
    for char in line:
        target_value = ord(char)
        if counter > target_value or 250 < target_value:
            result.append('/')
            counter = 0
            
        while counter < target_value:
            result.append('+')
            counter = (counter + 1) % 250
            
        result.append('.')
        
    return print(''.join(result))

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
    else: 
        print(f"[{" ".join(sys.argv[1:])}]")
        gen_file(" ".join(sys.argv[1:]))
