''' This program collects information about the client'''
from datetime import datetime


def check_of_number(number):
    ''' This program check true is number or not'''
    while True:
        try:
            return int(number)
        except ValueError:
            number = input('Enter number please ')


def check_of_one_words(string):
    ''' This program check true is string (one words) or not'''

    while True:
        if len(string.split()) == 1:
            return string
        else:
            string = input('Enter one words please ')


def function_of_decaid_how_old_category_is_customer():
    yeras_of_customer = year_at_today - berth_year
    if 0 <= yeras_of_customer <= 12:
        return 'Child'
    elif 13 <= yeras_of_customer <= 19:
        return 'Teenager'
    elif 20 <= yeras_of_customer:
        return 'Adult'


def function_list_of_hobby():
    list_of_hobby = []
    hobby_of_customer = check_of_one_words(input('Enter yor hobby (one words) ').lower().strip())
    while hobby_of_customer != 'stop':
        list_of_hobby.append(hobby_of_customer)
        hobby_of_customer = check_of_one_words(input('Enter else yor hobby (one words) or not (stop)').lower().strip())
    return list_of_hobby

print('Hellow this program collect information about you)')
year_at_today = datetime.now().year
last_name = input('Please enter please your last name ')
first_name = input('Please enter your first name ')
middle_name = input('Please enter your middle name ')
berth_year = check_of_number(input('Enter please your berth year (may be number) '))
hobby = function_list_of_hobby()
#dict_of_cluent = {'name': [last_name.title(), first_name.title(), middle_name.title()],'ago': year_at_today - berth_year, 'groop': function_of_decaid_how_old_category_is_customer,'hobby': hobby}

print(f'Name : {last_name.title()} {first_name.title()} {middle_name.title()}')
print('Age :', year_at_today - berth_year)
print('Life stage', function_of_decaid_how_old_category_is_customer())
if len(hobby) == 0:
    print("You didn't mention any hobbies")
else:
    print(f'number of hobby ', len(hobby))
    for i in hobby:
        print(f'- ', i)