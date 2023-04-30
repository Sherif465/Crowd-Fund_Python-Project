import re
import menu
class User:
    is_active = ""
    def __init__(self, first_name=None, last_name=None, email=None, password=None, confirm_password=None, mobile_number=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.mobile_number = mobile_number
    
    def is_valid_mobile_number(self):
        return bool(re.match(r'^(010|011|012|015)\d{8}$', self.mobile_number)) # validate against Egyptian phone numbers
    
    def is_valid_email(self):
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email)) # validate email address format

class AuthenticationSystem:
    def __init__(self, file_path):
        self.users = []
        self.file_path = file_path
        self.load_users_from_file()
    
    def register(self):
        first_name = ""
        while not first_name:
            first_name = input("Enter your first name: ")
            if not first_name:
                print("First name is required.")
            elif not isinstance(first_name, str):
                print("Invalid first name format.")
                first_name = ""
            elif len(first_name) < 3:
                print("First name should be at least 3 characters.")
                first_name = ""

        last_name = ""
        while not last_name:
            last_name = input("Enter your last name: ")
            if not last_name:
                print("Last name is required.")
            elif not isinstance(last_name, str):
                print("Invalid last name format.")
                last_name = ""
            elif len(last_name) < 3:
                print("Last name should be at least 3 characters.")
                last_name = ""
                
        email = ""
        while not email:
            email = input("Enter your email: ")
            if not email:
                print("Email is required.")
            elif not User(email=email).is_valid_email():
                print("Invalid email format.")
            elif any(u['email'] == email for u in self.users):
                print("Email already exists.")
                email = ""
                
        password = ""
        while not password:
            password = input("Enter your password (minimum 8 characters): ")
            if not password:
                print("Password is required.")
            elif len(password) < 8:
                print("Password should be at least 8 characters.")
                password = ""

        confirm_password = ""
        while not confirm_password:
            confirm_password = input("Confirm your password: ")
            if not confirm_password:
                print("Confirmation is required.")
            elif password != confirm_password:
                print("Passwords do not match.")
                confirm_password = ""

        mobile_number = ""
        while not mobile_number:
            mobile_number = input("Enter your mobile number (11 digits starting with 010, 011, 012, or 015): ")
            if not mobile_number:
                print("Mobile number is required.")
            elif not User(mobile_number=mobile_number).is_valid_mobile_number():
                print("Invalid mobile number format.")
                mobile_number = ""

        user = User(first_name, last_name, email, password, confirm_password, mobile_number)
        self.users.append({
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "password": user.password,
            "mobile_number": user.mobile_number
        })
        self.save_users_to_file()
        print("Registration successful.")


    def save_users_to_file(self):
        with open(self.file_path, "w") as f:
            for user in self.users:
                line = ",".join([user["first_name"], user["last_name"], user["email"], user["password"], user["mobile_number"]])
                f.write(line + "\n")
    
    def load_users_from_file(self):
        try:
            with open(self.file_path, "r") as f:
                lines = f.readlines()
                for line in lines:
                    user_data = line.strip().split(",")
                    if len(user_data) == 5:
                        self.users.append({
                            "first_name": user_data[0],
                            "last_name": user_data[1],
                            "email": user_data[2],
                            "password": user_data[3],
                            "mobile_number": user_data[4]
                        })
        except FileNotFoundError:
            pass
    
    def print_users(self):
        for user in self.users:
            print(f"{user['first_name']} {user['last_name']}, {user['email']}, {user['mobile_number']}")

    def print_user_data(self, email):
        for user in self.users:
            if user["email"] == email:
                print("First name: ", user["first_name"])
                print("Last name: ", user["last_name"])
                print("Email: ", user["email"])
                print("Mobile number: ", user["mobile_number"])
                break
            else:
                print("User not found.")

    def login(self):

        if User.is_active:
            print("Another user is already logged in. Please log out first.")
            return
    
        email = input("Enter your email: ")
        for user in self.users:
            if user["email"] == email:
                password = input("Enter your password: ")
                if user["password"] == password:
                    print("Login successful.")
                    User.is_active = email
                    print(f"Current user is: {User.is_active}")
                    return
        print("Login failed.")

    def logout(self):
        if User.is_active:
            reply = input("Do you want to log out? (y/n)" )
            if reply == "y":
                print("You have been logged out")
                User.is_active = ""
                menu.second_menu()
        else: print("no user is logged ")
        
### Running program ###        
auth_sys = AuthenticationSystem("users.txt")

