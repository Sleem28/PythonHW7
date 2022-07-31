from Import.get_info import * 

def get_person_info() -> str:
    
    first_name = get_first_name()
    last_name = get_last_name()
    phone_number = get_phone_number()
    address = get_address()

    return  first_name + '; ' + last_name + '; ' + phone_number + '; ' + address
    