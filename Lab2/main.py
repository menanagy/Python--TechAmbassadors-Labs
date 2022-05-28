import re
import json
import datetime

CURRENT_USER = None

def main():
    print_main_menu()


def print_main_menu():
    print("Choose an option: ")
    print("1 - Register")
    print("2 - Login")
    print("3 - Exit")
    choice = input("Pick option: ")
    while not choice.isdigit() or int(choice) > 3 or int(choice) < 0:#Error input {Characters or Number -ve , greater Than 3}
        choice = input("Please pick a valid option: ")
    if choice == "1":
        return register()
    if choice == "2":
        return login()
    if choice == "3":
        exit()


def print_project_menu():
    print("Choose an option: ")
    print("1 - add project")
    print("2 - edit a project of your own")
    print("3 - delete a project of your own")
    print("4 - view all projects")
    print("5 - search using date")
    print("6 - Back")
    print("7 - Exit")
    choice = input("Pick option: ")
    while not choice.isdigit() or int(choice) > 7 or int(choice) < 0:
        choice = input("Pick a valid option: ")
    if choice == "1":
        return add_project()
    if choice == "2":
        return edit_project()
    if choice == "3":
        return delete_project()
    if choice == "4":
        return view_all()
    if choice == "5":
        return search_using_date()
    if choice == "6":
        return print_main_menu()
    if choice == "7":
        exit()

def add_project():
    global CURRENT_USER
    title = input("project title: ")
    details = input("project details: ")
    total_target = input("your target: ")
    start_date = input("Start time year-month-day: ")
    year_regex = r'\b^202[0-5](.|-|)([1-9]|1[0-2])(.|-)([1-9]|1[0-9]|2[0-9]|3[0-1])$\b'#year from 2020-->2025
    # r'\b^01[0125][0-9]{8}$\b'
    while not re.fullmatch(year_regex, start_date):
        start_date = input("Invalid, enter valid start time year-month-day: ")
    # start_date = start_date.split("-")
    # actual_start_date = datetime.date(int(start_date[0]), int(start_date[1]), int(start_date[2]))
    end_date = input("End time year-month-day: ")
    while not re.fullmatch(year_regex, end_date):
        end_date = input("Invalid, enter valid end time year-month-day: ")
    project = {
        "title": title,
        "details": details,
        "Target": total_target,
        "start date": start_date,
        "end date": end_date,
        "user": CURRENT_USER["name"]
    }
    file = open("users.txt", "r")
    whole_file = file.read()
    file.close()
    whole_file = json.loads(whole_file)
    whole_file["projects"].append(project)
    file = open("users.txt", "w")
    file.write(json.dumps(whole_file))
    file.close()
    return print_project_menu()


def edit_project():
    found = False
    title = input("name of project you want to edit: ")
    file = open("users.txt", "r")
    whole_file = file.read()
    file.close()
    whole_file = json.loads(whole_file)
    for project in whole_file["projects"]:
        if project["title"] == title and project["user"] == CURRENT_USER["name"]:
            title = input("project title: ")
            details = input("project details: ")
            total_target = input("your target: ")
            start_date = input("Start time year-month-day: ")
            year_regex = r'\b^202[0-5](.|-|)([1-9]|1[0-2])(.|-)([1-9]|1[0-9]|2[0-9]|3[0-1])$\b'
            # r'\b^01[0125][0-9]{8}$\b'
            while not re.fullmatch(year_regex, start_date):
                start_date = input("Invalid, enter valid start time year-month-day: ")
            # start_date = start_date.split("-")
            # actual_start_date = datetime.date(int(start_date[0]), int(start_date[1]), int(start_date[2]))
            end_date = input("End time year-month-day: ")
            while not re.fullmatch(year_regex, end_date):
                end_date = input("Invalid, enter valid end time year-month-day: ")
            project["title"] = title
            project["details"] = details
            project["Target"] = total_target
            project["start date"] = start_date
            project["end date"] = end_date
            found = True
            file = open("users.txt", "w")
            file.write(json.dumps(whole_file))
            file.close()
            break
    if not found:
        print("project not found")
    return print_project_menu()

def delete_project():
    title = input("name of project you want to edit: ")
    file = open("users.txt", "r")
    whole_file = file.read()
    file.close()
    whole_file = json.loads(whole_file)
    for index, project in enumerate(whole_file["projects"]):
        if project["title"] == title and project["user"] == CURRENT_USER["name"]:
            whole_file["projects"].pop(index)
    file = open("users.txt", "w")
    file.write(json.dumps(whole_file))
    file.close()
    return print_project_menu()


def search_using_date():
    date = input("Date year-month-day: ")
    year_regex = r'\b^202[0-5](.|-|)([1-9]|1[0-2])(.|-)([1-9]|1[0-9]|2[0-9]|3[0-1])$\b'
    while not re.fullmatch(year_regex, date):
        date = input("Invalid, enter valid date year-month-day: ")
    file = open("users.txt", "r")
    whole_file = file.read()
    file.close()
    whole_file = json.loads(whole_file)
    projects = []
    for project in whole_file["projects"]:
        if project["start date"] == date:
            projects.append(project)
    for project in projects:
        print(project)
    return print_project_menu()


def view_all():
    file = open("users.txt", "r")
    whole = file.read()
    file.close()
    whole = json.loads(whole)
    for project in whole["projects"]:
        print(f"Project: {project['title']}, Details: {project['details']}, Total target:{project['Target']}")
    return print_project_menu()



def register():
    name = input("Enter name: ")
    while not name or name.isdigit():
        name = input("Enter a valid name: ")
    email = input("Enter Email: ")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while not re.fullmatch(regex, email):
        email = input("Please enter valid Email: ")
    password = input("Enter password: ")
    while not password:
        password = input("Please enter a valid password: ")
    second_password = input("Confirm password: ")
    while password != second_password or not second_password:
        second_password = input("password not matching, Confirm password: ")
    second_regex = r'\b^01[0125][0-9]{8}$\b'
    mobile_phone = input("Enter phone: ")
    while not re.fullmatch(second_regex, mobile_phone):
        mobile_phone = input("Enter valid phone: ")
    user = {
        "name": name,
        "email": email,
        "password": password,
        "phone": mobile_phone
    }
    file = open("users.txt", "r")
    object = file.read()
    file.close()
    object = json.loads(object)
    object["users"].append(user)
    file = open("users.txt", "w")
    file.write(json.dumps(object))
    file.close()
    return print_main_menu()


def login():
    global CURRENT_USER
    email = input("Enter Email: ")
    password = input("Enter password: ")
    file = open("users.txt", "r")
    object = file.read()
    file.close()
    object = json.loads(object)
    for user in object["users"]:
        if user["email"] == email and user["password"] == password:
            CURRENT_USER = user
            return print_project_menu()
    print("invalid combination")
    return login()

if __name__=='__main__':
    main()
