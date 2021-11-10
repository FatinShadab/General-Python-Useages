from logic import KCODE

file_path = input()

def encript(file_path):
    with open(file_path, 'r') as source:
        with open('Kencoded.txt', 'w') as output:
            for line in source.readlines():
                output.write(KCODE.encode(line))

def decrypt(file_path):
    with open(file_path, 'r') as source:
        with open('Kdecoded.txt', 'w') as output:
            for line in source.readlines():
                output.write(KCODE.decode(line))