def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' added to the shopping list.")
        
        elif choice == '2':
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")
        
        elif choice == '3':
            if shopping_list:
                print("\nCurrent Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Shopping list is empty.")
        
        elif choice == '4':
            print("Exiting the Shopping List Manager.")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
