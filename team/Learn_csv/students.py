
import csv


def main():
    
    INUMBER_INDEX = 0

    user_input = input("Please enter an I-Number: ")

    user_input = user_input.replace("-","")

    
    length = len(user_input)
    if user_input.isdigit() == False:
        print("Invalid I-Number")
    elif length < 9:
        print("Invalid I-Number: too few digits")
    elif length > 9:
        print("Invalid I-Number: too many digits")
    else:
        
        student_dict = read_dict("students.csv", INUMBER_INDEX)

        print(user_input)

        # print(student_dict)

        

        if user_input in student_dict:
            name = student_dict[user_input][1]
            print(name)
        else:
            print("No such student")

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    
    dictionary = {}

    
    with open(filename, "rt") as csv_file:

        
        reader = csv.reader(csv_file)

       
        next(reader)

        
        for row_list in reader:

            
            if len(row_list) != 0:

                
                key = row_list[key_column_index]

                
                dictionary[key] = row_list

    
    return dictionary



if __name__ == "__main__":
    main()