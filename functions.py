def print_employee_data(name:str,year_of_birth:int,actual_year:int):
    print("Name:", name)
    print("Birth:", year_of_birth)
    print("This year: ", actual_year)
    print("age:", actual_year-year_of_birth)

print_employee_data("John Doe",1970,2022)
#print_employee_data(input(),input())
#print_employee_data("Jane Doe",10)


def calculate_age(year_of_birth:int,actual_year:int):
    return actual_year-year_of_birth

print(calculate_age(2012,2022))

result = calculate_age(2012,2022)
print(f"A gyerek {result} éves.")