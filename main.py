#Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
from get_option import get_option
from Import.import_person import import_person
from Export.export_choose import export_choose

is_work = True

while is_work:

    what_to_do = get_option()

    if what_to_do == 1:
        print('Добавляем нового абонента в записную книгу.')
        import_person()
    elif what_to_do == 2:
        export_choose()

    is_work =  True if input('Если хотите продолжить нажмите "y" и ввод. Если хотите выйти, нажмите любую клавишу и ввод.: ') == 'y' else False