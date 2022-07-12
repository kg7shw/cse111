





def main():
    
    provinces_list = read_list("provinces.txt")
    
    print(provinces_list)

    provinces_list.pop(0)

    provinces_list.pop()

    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"
    
    number_count_of_alberta = provinces_list.count("Alberta")

    print()
    print(f"Alberta occurs {number_count_of_alberta} times in the modified list.")


def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
   
    provinces_text_list = []

    
    with open(filename, "rt") as text_file:

        
        for line in text_file:

           
            clean_line = line.strip()

            
            provinces_text_list.append(clean_line)

    
    return provinces_text_list


if __name__ == "__main__":
    main()






