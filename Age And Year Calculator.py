print("Hello! Welcome")

Name = input("What's Your Name?    ")

Age = int(input("What is your Age?    "))

print("Your Name Is ", Name, "And Your Age is", Age)




# print(input("What's Your Name  :"))

from datetime import datetime

def find_year_of_birth():
    try:
        age = int(input("Enter your current age: "))
        current_year = datetime.now().year
        birth_year = current_year - age
        print(f"You were born in the year: {birth_year}")
    except ValueError:
        print("Error: Please enter a valid integer for age.")

def find_how_old_are_you():
    try:
        birth_year = int(input("Enter your birth year: "))
        current_year = datetime.now().year
        age = current_year - birth_year
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