import csv
import os

r_path = os.path.join('DataBase', 'phonebook.csv')

def print_csv():
    with open (r_path, encoding='utf-8') as r_file:
            reader = csv.reader(r_file, delimiter=';')
            counter = 0

            for row in reader:
                if counter == 0: 
                    f_name = row[0]
                    l_name = row[1]
                    phone  = row[2]
                    adr    = row[3]
                else:
                    print(f'{f_name} = {row[0]}, {l_name} = {row[1]}, {phone} = {row[2]}, {adr} = {row[3]}.\n' if len(row) >=4 else \
                            f'info_error!!!')

                counter += 1
        