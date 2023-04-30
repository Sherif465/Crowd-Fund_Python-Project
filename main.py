from classes.user import AuthenticationSystem
from classes.Project import User_Options


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
            second_menu(email)
        # elif choice == "3":
        #     user.auth_sys.logout()
        elif choice == "3":
            print("Exiting...")
            break
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
        print("6. Search for a project using date")
        print("7. Logout")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            current_User.add_new_project()
        elif choice == "2":
            current_User.view_all_projects()
        elif choice == "3":
            current_User.view_user_projects(current_User.uEmail, False)
        if choice == "4":
            current_User.edit_project()
        elif choice == "5":
            current_User.delete_project()
        elif choice == "6":
            print("under construction")
        elif choice == "7":
            user.logout()
            menu()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
menu()