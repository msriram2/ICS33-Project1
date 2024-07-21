

def read_calls(file: open) -> {(str, str): int}:

    tuples_list = []
    with open(file) as my_file:
        contents = []
        for line in my_file:
            line = line.strip()
            contents.append(line)

        print(contents)
            










def call1to2(calls: {(str, str): int}) -> {str: {str: int}}:
    pass
