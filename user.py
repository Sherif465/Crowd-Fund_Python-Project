import re

class User:
    is_active = ""
    def __init__(self, first_name, last_name, email, password, confirm_password, mobile_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.mobile_number = mobile_number
    
    def is_valid_password(self):
        if len(self.password) < 8:
            return False
        if self.password != self.confirm_password:
            return False
        return True
    
    def is_valid_mobile_number(self):
        return bool(re.match(r'^(010|011|012|015)\d{8}$', self.mobile_number)) # validate against Egyptian phone numbers
    
    def is_valid_email(self):
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email)) # validate email address format

class AuthenticationSystem:
    def __init__(self, file_path):
        self.users = []
        self.file_path = file_path
        self.load_users_from_file()
    
    def register(self, first_name, last_name, email, password, confirm_password, mobile_number):
        user = User(first_name, last_name, email, password, confirm_password, mobile_number)
        if user.is_valid_password() and user.is_valid_mobile_number() and user.is_valid_email():
            if not any(u['email'] == email for u in self.users):
                self.users.append({
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "password": user.password,
                "mobile_number": user.mobile_number
                })
                self.save_users_to_file()
                print("Registration successful.")

            else: print("Email already exists.")
        else:
            print("Registration failed.")

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

    def login(self, email, password):
        for user in self.users:
            if user["email"] == email and user["password"] == password and User.is_active == "":
                print("Login successful.")
                User.is_active = email
                return
        print("Login failed.")

    def logout(self):
        reply = input("Do you want to log out? (y/n)" )
        if reply == "y":
            print("You have been logged out")
            User.is_active = ""
        


auth_sys = AuthenticationSystem("users.txt")

# Register multiple users
auth_sys.register("John", "Doe", "johe@example.com", "password123", "password123", "01912345678")
auth_sys.register("marwan", "Doe", "man@example.com", "password456", "password456", "01012345678")
auth_sys.register("Bob", "Smith", "bobsmith@example.com", "password789", "password789", "01212345678")

# Retrieve the list of registered users
auth_sys.print_users()
