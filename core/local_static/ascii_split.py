import os

def split_file(filename):
    lines_per_file = 3000
    lines_per_chunk = lines_per_file - (lines_per_file % 69)
    chunk_num = 1
    with open(filename, 'r', encoding='UTF-8') as input_file:
        while True:
            output_filename = f'{os.path.splitext(filename)[0]}_part{chunk_num}'
            with open(output_filename, 'w', encoding='UTF-8') as output_file:
                for i in range(lines_per_chunk):
                    line = input_file.readline()
                    if not line:
                        return
                    output_file.write(line)
            chunk_num += 1


split_file('ascii_file_new')