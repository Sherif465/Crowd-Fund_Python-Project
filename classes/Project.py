import os
from datetime import datetime
from colorama import Fore,  Style


projects_directory = "All Projects"

class User_Options:
    def __init__(self, uEmail):       
        self.uEmail = uEmail + ".txt"

    def add_record_in_file(self, record):
        path = projects_directory + '/' + self.uEmail
        userFile = os.path.exists(path)
        f = ""
        if userFile:
            f = open(path, 'a')
        else:
            f = open(path, 'w')

        rec = []
        for val in record:
            rec.append(str(val))
        rec = ";".join(rec)
        f.write(rec)
        f.close()


    def validate_date(self, date):
        dateFormat = '%Y-%m-%d'
        try:
            date = datetime.strptime(date, dateFormat)
            return date
        except:
            print("Invalid date format")
            return False


    def validate(self, field, val):
        if field == "start_date" or field == "end_date":
            valid = self.validate_date(val)
            while not valid:
                val = input(f"Enter project {field}: ")
                valid = self.validate_date(val)
            
        if field == "target":
            valid = self.validate_target(val)
            while not valid:
                val = input(f"Enter project {field}: ")
                valid = self.validate_target(val)

            val = str(val) + " EGP"

        return val


    def validate_target(self, val):
        try:
            num = int(val)
            return True
        except ValueError:
            print("Invalid target format")


    def view_all_projects(self):
        for filename in os.scandir(projects_directory):
            if filename.is_file():
                fname = filename.name
                print(Fore.BLUE + '{:30s}'.format("|" + fname + " Projects"))
                print(Fore.GREEN)
                self.view_user_projects(fname, False)
        print(Style.RESET_ALL)
                    

    def view_user_projects(self, email, save):
        allRecords = []
        path = projects_directory + '/' + email
        userFile = os.path.exists(path)
        if userFile:
            userfile = open(path, 'r')
            print("_" * 140)
            print('{:1s}'.format(""), end="")
            
            
            for field in Project.info:
                print('|{:30s}'.format(field), end="")
            print("\n")
            print("_" * 140)
            print("\n")


            ind = 1
            for record in userfile:
                tempPro = []
                print(Fore.GREEN)
                record = record.split(";")
                print('{:1s}'.format(str(ind)), end="")
                
                for val in record:
                    print('|{:30s}'.format(val), end="")
                    if save: tempPro.append(val)

                print("")
                if save:
                    tempPro_Obj = Project(tempPro)
                    allRecords.append(tempPro_Obj)
                ind += 1
                
            print("_" * 140)
            print("\n")
            print(Style.RESET_ALL)
            if save: 
                return allRecords
            
        else:
            print("User has no projects.")


    def edit_project(self):
        records = self.view_user_projects(self.uEmail, True)
        ans = int(input("Enter number of project to edit: "))
        if ans > len(records) or ans < 1:
            print("Invalid project number!")
        else:
            field = input("Enter field you want to edit: ")
            if field not in Project.info:
                print("This field is not found")
            else:
                newVal = input(f"Enter new {field}: ")
                if field == "start_date" or field == "target":
                    newVal = self.validate(field, newVal)
                if field == "end_date":
                    newVal = self.validate(field, newVal)
                    while newVal < records[ans - 1].Info["start_date"]: 
                        print("Invalid as end date should be after start date.")
                        newVal = input(f"Enter project {field}: ")
                        newVal = self.validate(field, newVal)
                    newVal = newVal + '\n'

                # print(Project.info[-1])
                records[ans - 1].Info[field] = newVal
                self.projects_update(records, False, -1)
                print("Records updated successfully!")


    def add_new_project(self):
        record = []
        for field in Project.info:
            entry = input(f"Enter project {field}: ")
            if field == "start_date" or field == "target":
                    entry = self.validate(field, entry)
            if field == "end_date":
                entry = self.validate(field, entry)
                print(entry + " " + record[-1])
                while entry < record[-1]: 
                    print("Invalid as end date should be after start date.")
                    entry = input(f"Enter project {field}: ")
                    entry = self.validate(field, entry)
                entry = entry + '\n'
            record.append(entry)
        self.add_record_in_file(record)
        print("New Project added successfully!")


    def projects_update(self, rec, delete, index):
        path = projects_directory + '/' + self.uEmail
        f = open(path, 'w')
        f.close()
        ind = 0
        for i in rec:
            if delete and (ind+1) == index:
                ind += 1
                continue
            temp = []
            for item in Project.info:
                temp.append(rec[ind].Info[item])
            ind += 1
            self.add_record_in_file(temp)


    def delete_project(self):
        records = self.view_user_projects(self.uEmail, True)
        ans = int(input("Enter number of project you want to delete: "))
        if ans > len(records) or ans < 1:
            print("Invalid project number!")
        else:
            confirm = input(f"Are you sure you want to delete project number {ans}? (y/n): ")
            if confirm == "y":
                self.projects_update(records, True, ans)
                print("Records deleted successfully!")
            else:
                print("Process cancelled.")


class Project():
    info = ["title", "details", "target", "start_date", "end_date"]
    #INFO = ["pro", "no details", 23314, "09-09-1998", "10-10-2010"]
    def __init__(self, INFO):
        self.Info = {}
        for ind, field in enumerate(self.info):
            self.Info[field] = INFO[ind]

    
# pro = Project(["myTitile", "My_Description", 134314, "02-23-1993", "02-23-1993"])
# print(pro.Info)


# obj = User_Options("assem@email.com")
# obj = User_Options(["Building musque", "Amal khairy", 230000, "01-05-2020", "01-10-2021"], "janedoe@example.com")
# obj = User_Options(["Building be2r", "help people find water", 37000, "01-05-2012", "01-10-2013"], "man@example.com")
# obj = User_Options(["Blood donation", "good project", 2000, "01-05-2016", "01-10-2018"], "janedoe@example.com")
# obj = User_Options(["Charity support", "nive project", 3000, "01-05-2005", "01-10-2013"], "man@example.com")
# obj.validate_date("23-03-1998")
# obj.view_all_projects()
# obj.edit_project()

# obj.add_new_project()
# obj.add_new_project()
# obj.add_new_project()
# x = obj.view_user_projects("assem@email.com.txt", True)
# obj.edit_project()
# x = obj.view_user_projects("assem@email.com.txt", True)
# obj.add_new_project()
# x = obj.view_user_projects("assem@email.com.txt", True)
# obj.delete_project()
# x = obj.view_user_projects("assem@email.com.txt", True)

# obj = User_Options(["title", "no details", 250000, "23-02-1988", "23-02-1999"], "marwan@example.com")
# print(x[0].Info["title"])
# x = "alot alot to say, but i am just testing it's length, and now, i test a new method i just found on stack over flow, to insert new line every fixed n chars"
# x = '\n'.join(x[i:i+15] for i in range(0, len(x), 15))
# print(x)

