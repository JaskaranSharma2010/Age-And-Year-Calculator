from datetime import datetime

def find_year_of_birth():
    try:
        age = int(input("Enter your current age: "))
        birthday_gone = input("Has your birthday already occurred this year? (yes/no): ").strip().lower()
        current_year = datetime.now().year
        if birthday_gone == 'yes':
            birth_year = current_year - age
        else:
            birth_year = current_year - age - 1
        print(f"You were born in the year: {birth_year}")
    except ValueError:
        print("Error: Please enter a valid integer for age.")

def find_how_old_are_you():
    try:
        birth_year = int(input("Enter your birth year: "))
        birthday_gone = input("Has your birthday already occurred this year? (yes/no): ").strip().lower()
        current_year = datetime.now().year
        if birthday_gone == 'yes':
            age = current_year - birth_year
        else:
            age = current_year - birth_year - 1
        print(f"You are {age} years old.")
    except ValueError:
        print("Error: Please enter a valid integer for birth year.")

def main():
    while True:
        print("\nWelcome! Please select an option:")
        print("1. Find Year Of Birth")
        print("2. Find How Old Are You?")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            find_year_of_birth()
        elif choice == '2':
            find_how_old_are_you()
        else:
            print("Invalid choice. Please select 1 or 2.")
        
        again = input("\nDo you want to do it again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
