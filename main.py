# Inversion srting
def reverse_string(string):
    return string[::-1]


print(reverse_string("change Of Direction"))


# Year and age
def get_age(year):
    century = (year + 99) // 100
    return century


print(get_age(2023))


# sum variables
def sum_variables(varibles):
    summer = 0
    for var in varibles:
        summer += var
    return summer


print(sum_variables([10, 20, 30, 40, 50, 60]))
