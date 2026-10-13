## this contains the main body of the whole program
from utils import valid_contact_number, choice_func, search_util
from file_ops import save_contact, read_file, search_contact_name, search_contact_number, delete_contact, contact_exist_checker, update_contact

#this function same as before saves details
def details() :
    while True :
        name = input("Enter the name here: ")
        # if name.lower() == "stop" :
        #     break
        # name_list.append(name)
        phn_number = valid_contact_number()

        if contact_exist_checker(name, phn_number): 
            print("Contact already exist")
        else :
            save_contact(name, phn_number)
            print("Contact added!")

        print("Do you want to keep entering new contact? (Yes/No)")
        choice = choice_func()
        if choice.lower() == "no" :
            break

#this special function for view and search contact, printing everything there in the list
def display_contacts(lines) :
    for line in lines:
            print(line.strip())

#this function to check what user wants to do
def menu_checker() :
        print("Do you want to continue back to the menu?")
        return choice_func()

#just a message before exiting the program
def exit_msg() :
    print("Exiting the program")

#for showing the search result
def final_contact_search(line_list):
    if line_list is None :
        print("No file exists!")
    elif not line_list :
        print("No such contact esxists")
    elif len(line_list) == 1 :
        display_contacts(line_list)
    else :
        print("Multiple contacts found")
        display_contacts(line_list)

#Calling the update contact
def update_confirmation(return_list, updated_number):
    if return_list is None:
            print("No such file exist!")

    elif not return_list :
        print("No contact with that name is found!")

    elif len(return_list) == 1 :
        update_contact(return_list[0], updated_number)
        print("Contact updated!")

    elif len(return_list) > 1:
        print("Multiple person found")
        for i, return_line in enumerate(return_list):
            print(f"{i+1}. {return_line.strip()}")

        while True:
            try :
                index_choice = int(input(f"Enter the index number (1 to {len(return_list)}): ")) - 1
            except ValueError :
                print("Invalid input. Enter a number")
            
            
            if index_choice > 0 and index_choice <= len(return_list):
                name_line = return_list[index_choice]
                update_contact(name_line, updated_number)
                print("Contact updated!")
                break
            else:
                print("Invalid input! Enter a valid index number")
            


print("This is a contact saver. You can add and read your contacts.")
while True :
    menu_option =input("Press 1: To add a contact\nPress 2: viewing contacts\nPress 3: to search a contact by name\nPress 4: to search a contact by number\nPress 5: to delete a contact\nPress 6: to update a contact\nPress 7: To exit\n")
    if menu_option == "1" :
        details()
        
        if menu_checker() == "no" :
            break
    elif menu_option == "2" :
        lines = read_file()
        if not lines:
            print("No such file exist!")
        display_contacts(lines)

        if menu_checker() == "no" :
            break
    elif menu_option == "3" :
        search_name = input("Enter a name you want to search: ")

        status, line_list = search_contact_name(search_name)
        final_contact_search(line_list)

        if menu_checker() == "no" :
            break
    elif menu_option == "4" :
        search_number = valid_contact_number()
        received_contact = search_contact_number(search_number)
        if received_contact is None :
            print("No such file exists")
        elif not received_contact :
            print("There is no such contact number in the contact list")
        else :
            display_contacts(received_contact)
        
        if menu_checker() == "no" :
            break
    elif menu_option == "5" :
        delete_name = input("Enter the name of the contact you want to delete : ")

        contact_list, deleted = delete_contact(delete_name)

        if not contact_list:
            print("No such file exist!")

        if deleted :
            print("Contact is deleted")
        else :
            print("No such contact is found!")

        if menu_checker() == "no" :
            break
    elif menu_option == "6" :
        name = input("Enter the name you want to update: ")
        updated_number = valid_contact_number()
        return_list = search_contact_name(name)
        update_confirmation(return_list, updated_number)
        
        if menu_checker() == "no" :
            break
    elif menu_option == "7" :
        break
    else :
        print("Invalid input. Choose an option from the menu")

exit_msg()