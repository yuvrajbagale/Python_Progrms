#python context manager
with open("simple.txt", 'r') as file:
    for line in file:
        if 'values' in line.lower():
            print(line, end='')