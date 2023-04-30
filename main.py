from classes.user import AuthenticationSystem
from classes.Project import User_Options
import getpass
import stdiomask
import sys

user = AuthenticationSystem("users.txt")
def menu():
    while True:
        print("1. Register")
        print("2. Log in")
        # print("3. Log out")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user.register()
        elif choice == "2":
            email = user.login()
            if email is not None:
                second_menu(email)
        elif choice == "3":
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def second_menu(userEmail):

    current_User = User_Options(userEmail)
    while True:
        print("1. Create a new project")
        print("2. View all porjects")
        print("3. View your projects")
        print("4. Edit your project")
        print("5. Delete from your project")
        # print("6. Search for a project using date")
        print("6. Logout")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            current_User.add_new_project()
        elif choice == "2":
            current_User.view_all_projects()
        elif choice == "3":
            current_User.view_user_projects(current_User.uEmail, False)
        elif choice == "4":
            current_User.edit_project()
        elif choice == "5":
            current_User.delete_project()
        elif choice == "6":
            user.logout()
            break
        elif choice == "7":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

menu()

