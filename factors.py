#!/usr/bin/python3
def factorize(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return i, number // i
    return None


def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            num = int(line.strip())
            result = factorize(num)
            if result:
                factor1, factor2 = result
                print("{}={}*{}".format(num, factor1, factor2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    file_path = sys.argv[1]

    try:
        process_file(file_path)
    except FileNotFoundError:
        print("Error: File {} not found".format(file_path))
        sys.exit(1)
    except ValueError:
        print("Error: Invalid content in he file {}".format(file_path))
        sys.exit(1)
