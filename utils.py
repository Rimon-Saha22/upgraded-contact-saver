## This file contains functions of validity and input handling

def valid_contact_number() :
    while True :
        phn_number = input("Enter the number here: ")
        if phn_number.isdigit() :
            return phn_number
        print("Invalid input. Enter number in correct format")



def choice_func():
     while True :
        choice = input("Enter yes or no: ")
        if choice.lower() in ["yes","no"] :
            return choice.lower()
        else :
            print("Enter yes or no!")

def search_util(name, line_list) :
    final_search_list = []
    for line in line_list :
        name_part, number_part = line.strip().split(" - ")

        if name_part.lower() == name.lower() :
            final_search_list.append(line)
    return final_search_list