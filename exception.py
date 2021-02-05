def main():
    try:
        print(calc_total('sale.txt'))
    except FileNotFoundError:
        print('Make sure you have the correct file')
    except ValueError:
        print('Make file has all numbers')
def calc_total(file_name):
    input_file = open(file_name, 'r')
    total = 0
    for line in input_file:
        line = float(line)
        total += line
    return total

if __name__ == '__main__':
    main()
