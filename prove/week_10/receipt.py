import csv
from datetime import datetime

def main():
    try:
        # The column headings and indexes.
        PRODUCT_NUMBER_INDEX = 0
        PRODUCT_NAME_INDEX = 1
        PRODUCT_PRICE_INDEX = 2
        PRODUCT_QUAANTITY_INDEX = 1
        discount_rate = 0.10
        sales_tax_rate = .06
        total_items = 0
        subtotal = 0
        discount = 0



        store_name = "Inkom Emporium"

        # Call the now() method to get the current
        # date and time as a datetime object from
        # the computer's operating system.
        current_date_and_time = datetime.now()


        # Read the contents of a CSV file named students.csv
        # into a dictionary named students_dict. Use the Product Number
        # as the key in the dictionary.
        products_dict = read_dict("CSE111/prove/week_10/products.csv", PRODUCT_NUMBER_INDEX)

        
        # print(products_dict)
        # print()
        print(f"{store_name}")
        print()
        
        with open("CSE111/prove/week_10/request.csv", "rt") as csv_file:

            product_requests = csv.reader(csv_file)

            next(product_requests)

            for item in product_requests:

                key = item[PRODUCT_NUMBER_INDEX]

                quanity = item[PRODUCT_QUAANTITY_INDEX]

                product_info = products_dict[key]
                
                product_name = product_info[1]
                price = product_info[2]

                multiplied_price = float(price) * int(quanity)
                subtotal += multiplied_price
                total_items += int(quanity)

                

                # wheat bread: 2 @ 2.55

                print(f"{product_name}: {quanity} @ {price}")

        

        # Call the weekday() method to get the day of the
        # week from the current_date_and_time object.
        weekday = current_date_and_time.weekday()
        # print()
        # print(weekday)
        # print()
        # if the subtotal is greater than 50 and today is
        # Tuesday or Wednesday, compute the discount amount.
        if weekday == 1 or weekday == 2:
            
            discount = round(subtotal * discount_rate, 2)
            
            subtotal -= discount

        sales_tax = subtotal * sales_tax_rate
        total = subtotal + sales_tax

        
        print()
        print(f"Number of Items: {total_items}")
        print(f"Discount amount: {discount:.2f}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print()
        print(f"Thank you for shopping at the {store_name}")
        print(f"{current_date_and_time:%A %b %d %H:%M:%S %Y}")
    

    except FileNotFoundError as not_found_err:
        print(not_found_err)
        print(f"Error: cannot open file"
                " because it doesn't exist.")

    except PermissionError as perm_err:
        print(f"Error: cannot read from file"
                " because you don't have permission.")
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

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
     # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:
    # csv_file = open(filename, "rt")

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list
            # dictionary.put(key, row_list) Java
            # dictionary.key = row_list
            # dictionary[key] = row_list

    # Return the dictionary.
    return dictionary



if __name__ == "__main__":
    main()