# read file
import os
import re

# Sleepy Librarian Program
# Assumptions: 
# 1. The input for book titles and overdue days is valid.
# 2. The overdue data is stored in a file named "overdue_books.txt".
# 3. The output will be saved in a file named "fines_report.txt".
# 4. The program will calculate fines based on the number of overdue days.
# 5. The program will handle overdue days greater than 10 with a special message.
# 6. The program will display the book details and save them to a file.

# Constants for file paths
OVERDUE_DATA = "overdue_books.txt"
SAVED_DATA = "fines_report.txt"

# List to hold book details
book_details = []  # This will hold the book details

def calculate_fine(days):
    if days >= 1 and days <= 5:
        fine = days * 0.5
    elif days >= 6 and days <= 10:
        fine = days
    elif days > 10:
        fine = days * 1.5
    return fine

# read file
def read_data():
    with open(OVERDUE_DATA, "r") as file:
        lines = file.readlines()
        for line in lines:
            # split line and store in BOOK_DETAILS
            overdue_details = line.strip().split(";")
            # calculate the fine and add it to the details
            overdue_days = int(overdue_details[1])
            fine_amount = f"$ {calculate_fine(overdue_days)}"
            # handle angry librarian logic
            if overdue_days > 10:
                overdue_days = f"{fine_amount} -.-"
            overdue_details.append(fine_amount)
            # append the details to BOOK_DETAILS
            book_details.append(overdue_details)
        print(f"Total records read: {len(book_details)}")

def display_books():
    print("Overdue Books Details:")
    print("--" * 30)
    for book in book_details:
        print(f"{book[0]} {book[1]} - {book[2]}")

def write_data():
    with open(SAVED_DATA, "w") as file:
        for book in book_details:
            file.write(";".join(book) + "\n")
        print(f"Total records saved: {len(book_details)}")

def clear_console():
    # Clear the console for better readability
    os.system('cls' if os.name == 'nt' else 'clear')

def main_app():
    clear_console()
    print("Welcome to the Sleepy Librarian program!")
    print("--" * 30)
    read_data()
    while True:
        title_name = input("Enter the book title (type stop to save and quit): ").strip()
        print(f"Title: {title_name}")

        if title_name.lower() == "stop":
            clear_console()
            print("Saving data and exiting the program...")
            print("Thanks for using the Sleepy Librarian program!")
            break

        # convert to days, assume all inputs are valid integers
        days_overdue = int(input("Enter the number of days overdue: "))
        print(f"Days Overdue: {days_overdue}")

        fine_amount = f"$ {calculate_fine(days_overdue)}"

        if days_overdue > 10:
            days_overdue = f"{fine_amount} -.-"

        # Append the book details to BOOK_DETAILS
        book_details.append([title_name, str(days_overdue), fine_amount])
    #once the user is done entering data, write to file
    write_data()
    display_books()
    
# main app
main_app()