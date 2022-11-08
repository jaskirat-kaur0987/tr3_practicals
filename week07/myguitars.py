from guitar import Guitar

# constants
CSV_FILE = 'guitars.csv'


def load_file(csv_file):
    """Read file of guitar details, and return a list of guitars"""
    guitars = []
    # Open the file for reading
    in_file = open(CSV_FILE, 'r')

    # File format is like: name, year, cost
    for line in in_file:
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')

        # construct a guitar object
        # year should be an int, cost is a float
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))

        # Add the guitar to the list
        guitars.append(guitar)

    # Close the file as soon as we've finished reading it
    in_file.close()
    return guitars


def input_non_empty_string(prompt):
    """above prompt will return a non-empty string from user input"""
    input_str = input(prompt).strip()
    while len(input_str) == 0:
        print("Input can not be blank")
        input_str = input(prompt).strip()
    return input_str


def input_positive_int(prompt):
    """ return positive int with a given prompt"""
    valid_input = False
    input_num = -1
    while not valid_input:
        try:
            input_num = int(input(prompt))
            if input_num > 0:
                valid_input = True
            else:
                print("Number must be >= 1")
        except ValueError:
            print(f"Invalid input; enter a valid number")
    return input_num


def input_positive_float(prompt):
    """ return positive int with a given prompt"""
    valid_input = False
    input_num = -1
    while not valid_input:
        try:
            input_num = float(input(prompt))
            if input_num > 0.0:
                valid_input = True
            else:
                print("Number must be > 0.0")
        except ValueError:
            print(f"Invalid input; enter a valid number")
    return input_num


def save_guitars(csv_file, guitars):
    try:
        outfile = open(csv_file, 'w')
        for guitar in guitars:
            print(guitar.name + ',' + str(guitar.year) + ',' + str(guitar.cost), file=outfile)
        print(f'{len(guitars)} guitars saved to {csv_file}')

        outfile.close
    except IOError:
        print('Error: can not open file')


def main():
    guitars = load_file(CSV_FILE)
    for guitar in guitars:
        print(guitar)
        # sort by year
    guitars.sort()
    print()
    print('Sort by year:')
    for guitar in guitars:
        print(guitar)

    # add a new guitar
    name = input_non_empty_string('Enter guitar name:')
    year = input_positive_int('Enter a year:')
    cost = input_positive_float('Enter cost:')
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)

    # sort by year
    guitars.sort()
    print()
    print('Sort by year:')
    for guitar in guitars:
        print(guitar)

    save_guitars(CSV_FILE, guitars)


if __name__ == '__main__':
    main()
