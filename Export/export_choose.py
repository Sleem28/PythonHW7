from get_option import get_export_choose_option
from Export.export_file_to_html import export_file_to_html
from Export.print_csv import print_csv

def export_choose():
    
    what_to_do = get_export_choose_option()
    
    if what_to_do == 1:
        export_file_to_html()
    elif what_to_do == 2:
            print_csv()
            # Закончил здесь. Нужно описать експорт в хтмл и сделать выбор вывода на экран
            # Сделать модуль вывода на экран csv
