from Import.get_person_info import get_person_info
from Import.write_to_phonebook import write_to_book


def import_person():
    person = get_person_info()
    write_to_book(person=person)

