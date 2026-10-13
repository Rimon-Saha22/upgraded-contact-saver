#this file contains file functions of the program
def save_contact(name, phn_number) :
    try :
        with open("name_contact.txt", "a") as d :
            d.write(f"{name} - {phn_number}\n")
    except Exception:
        print("Something went wrong!")

    return



def read_file() :
    try :
        lines = []
        with open("name_contact.txt", "r") as f:
            for line in f :
                lines.append(line)
            lines.sort(key = lambda line: line.lower())
            return lines
    except FileNotFoundError :
        return []



def search_contact_name(name) :
    try:
        with open("name_contact.txt", "r") as f :
            lines = f.readlines()
    except FileNotFoundError:
        return None

    line_list = []

    for line in lines :
        if not line.strip() :#this ensures that no empty string is passed to the condition, otherwise the program will crash
            continue

        name_part, number_part = line.strip().split(" - ")

        if name.lower() in name_part.lower() :
            line_list.append(line)

    return line_list
        


def search_contact_number(phn_number) :
    try :
        with open("name_contact.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return None
    
    phn_number_list = []
    for line in lines :
        if not line.strip() :
            continue
        
        _, contact_part = line.strip().split(" - ")
        if phn_number in contact_part:
           phn_number_list.append(line)

    return phn_number_list

def delete_contact(name) :
    try :
        with open("name_contact.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError :
        return None, False

    contact_list = []
    deleted = False

    for line in lines :

        # parts = line.strip().split()
        # if not parts :
        #     continue
        # if parts[0].lower() != name.lower() :
        #     contact_list.append(line)

        if not line.strip() :
            continue

        name_part, contact_part = line.strip().split(" - ")
        if name_part.lower() != name.lower() :
            contact_list.append(line)
        else :
            deleted = True

    with open("name_contact.txt", "w") as f :
        f.writelines(contact_list)

    return contact_list, deleted



def contact_exist_checker(name, phn_number) :
    try:
        with open("name_contact.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return False
    
    for line in lines:
        if not line.strip() :
            continue

        name_part, contact_part = line.strip().split(" - ")

        if name_part.lower() == name.lower() and contact_part == phn_number:
            return True
        
    return False



def update_contact(return_string, phn_number) :
    try:
        with open("name_contact.txt", "r") as f :
            lines = f.readlines()
    except FileNotFoundError:
        return False
    
    contact_list = []
    for line in lines :
        if not line.strip() :
            contact_list.append(line)
            continue

        if line == return_string :
            name_part, _ = line.strip().split(" - ")
            contact_list.append(f"{name_part} - {phn_number}\n")
        else :
            contact_list.append(line)

    with open("name_contact.txt", "w") as d :
        d.writelines(contact_list)

    return True
