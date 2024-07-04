file_path = 'sample.txt'

def line_read(file_path):
    with open(file_path , 'r') as file:
        for line in file:
            yield line.strip()

for line in line_read(file_path):
    print(f"{line}")