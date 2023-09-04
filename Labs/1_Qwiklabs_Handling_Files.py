"""
For this lab, imagine you are an IT Specialist at a medium-sized company.
The Human Resources Department at your company wants you to find out how many people are in each department.
You need to write a Python script that reads a CSV file containing a list of the employees in the organization,
counts how many people are in each department, and then generates a report using this information.
The output of this script will be a plain text file.

Save the file by clicking Ctrl-o, Enter, and Ctrl-x.
chmod +x generate_report.py
./generate_report.py
cd ~/data
"""
import csv
import os


csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
# csv_location = os.path.abspath('employees.csv')
# print(csv_location)

# The skipinitialspace=True parameter specifies that any leading spaces after a delimiter should be ignored.
# For example, if a CSV file has a value like " John,Smith", with skipinitialspace=True, the leading spaces
# before "John" will be ignored.
# csv module in Python does not have a built-in parameter that specifically ignores trailing spaces before a delimiter.
# do it with .rstrip()
def read_employees(csv_location):
    with open(csv_location) as read:
        reader = csv.DictReader(read, dialect='empDialect')
        empl_list = []
        for row in reader:
            empl_list.append(row)
            # print(f"{row['Username']} in: {row['Department']}")
        return empl_list


employees_list = read_employees('employees.csv')


def count_empl_in_dep(employees_list: list):
    departments = []
    empl_in_departm = {}
    for empl in employees_list:
        departments.append(empl['Department'])

    for depart in set(departments):
        empl_in_departm[depart] = departments.count(depart)
    return empl_in_departm


result_dict = count_empl_in_dep(employees_list)


def report_to_txt(result_dict, where_to_write):
    with open(where_to_write, 'w+') as report:
        for i in sorted(result_dict):
            report.write(f'{str(i)}: {result_dict[i]}\n')
        report.close()


report_to_txt(result_dict, r'C:\pythonProject\Automation with Python\report.txt')


# def read_employees(csv_file_location):
#     csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
#     employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
#     employee_list = []
#     for data in employee_file:
#         employee_list.append(data)
#     return employee_list


# employee_list = read_employees('/home/student-04-43a9f3e08bcb/data/employees.csv')
# # print(employee_list)
#
#
# def process_data(employee_list):
#     department_list = []
#     for employee_data in employee_list:
#         department_list.append(employee_data['Department'])
#     department_data = {}
#     for department_name in set(department_list):
#         department_data[department_name] = department_list.count(department_name)
#     return department_data
#
#
# dictionary = process_data(employee_list)
# # print(dictionary)
#
#
# def write_report(dictionary, report_file):
#     with open(report_file, "w+") as f:
#         for k in sorted(dictionary):
#             f.write(str(k) + ':' + str(dictionary[k]) + '\n')
#         f.close()
#
#
# write_report(dictionary, '/home/student-04-43a9f3e08bcb/data/report.txt')

"""
student-04-43a9f3e08bcb@linux-instance:~/data$ cat employees.csv
Full Name, Username, Department
Audrey Miller, audrey, Development
Arden Garcia, ardeng, Sales
Bailey Thomas, baileyt, Human Resources
Blake Sousa, sousa, IT infrastructure
Cameron Nguyen, nguyen, Marketing
Charlie Grey, greyc, Development
Chris Black, chrisb, User Experience Research
Courtney Silva, silva, IT infrastructure
Darcy Johnsonn, darcy, IT infrastructure
Elliot Lamb, elliotl, Development
Emery Halls, halls, Sales
Flynn McMillan, flynn, Marketing
Harley Klose, harley, Human Resources
Jean May Coy, jeanm, Vendor operations
Kay Stevens, kstev, Sales
Lio Nelson, lion, User Experience Research
Logan Tillas, tillas, Vendor operations
Micah Lopes, micah, Development
Sol Mansi, solm, IT infrastructure
"""