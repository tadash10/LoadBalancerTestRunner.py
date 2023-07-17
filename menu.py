import sys
from load_test import run_load_test
from report import generate_report
from cleanup import cleanup

def print_menu():
    print("==== Load Balancer Test Menu ====")
    print("1. Run Load Test")
    print("2. Generate Report")
    print("3. Cleanup")
    print("4. Exit")

def menu_choice():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            run_load_test()
        elif choice == "2":
            generate_report()
        elif choice == "3":
            cleanup()
        elif choice == "4":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu_choice()
