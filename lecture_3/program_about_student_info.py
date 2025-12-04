'''This program add students and they grapes and create report

    Support doing
        - add new stydent
        - add another grapes students from list
        - show report about all students
        = show best and worse student
        - show average grapes from all students
        - exit '''


class Student_list:
    '''this class discript information about student '''

    def __init__(self):
        '''ininiation list of dichenary with information about student'''
        self.list_of_dict_about_students = []
        self.set_of_students_name = []

    @classmethod
    def check_of_number(self, number: int):
        ''' This program check true is number or not'''
        while True:
            if isinstance(number, str) and number == 'stop':
                return 'stop'
            try:
                if 0<=int(number)<=100:
                    return int(number)
                else:
                    number = int(input('Enter number between 0 and 100 please '))
            except ValueError:
                number = input('Enter number please ')


    @classmethod
    def check_of_two_words(self, string: str):
        ''' This program check true is string (two words) or not (for name of students)'''

        while True:
            if len(string.split()) == 2:
                return string
            else:
                string = input('Enter two words please ')

    def add_new_student_in_list_of_students(self):
        '''This function add new student in list'''
        new_students = self.check_of_two_words(input('Enter ferst and second name of student '))
        grade = self.check_of_number(input('Enter one grade or enter stop '))
        list_of_number = []
        while isinstance(grade, int):
            list_of_number.append(grade)

            grade = self.check_of_number(input('Enter one grade or enter stop '))

        self.list_of_dict_about_students.append({'name': new_students, 'grapes': list_of_number})
        self.set_of_students_name.append(new_students)

    def add_extra_grape_students(self, name_student: str):
        '''Tgis function add extra grape students'''
        name_student = self.check_of_two_words(name_student)
        if name_student in self.set_of_students_name:
            grade = self.check_of_number(input('Enter one grade or enter stop '))
            list_of_number = []
            while isinstance(grade, (int, float)):
                list_of_number.append(grade)

                grade = self.check_of_number(input('Enter one grade or enter stop '))

            for i in self.list_of_dict_about_students:
                if i['name'] == name_student:
                    i['grapes'].extend(list_of_number)
        else:
            print('This student not in list ')

    def showe_Student_and_his_grapes_all(self):
        '''This function show report obaut students '''
        if self.list_of_dict_about_students == []:
            print(f'Not students ')
        for i in self.list_of_dict_about_students:

            if i['grapes'] == []:
                print(f'{i["name"]} - N/A')
            else:
                print(
                    f"{i['name']} - {round(sum(i['grapes']) / len(i['grapes']), 2)} - this is average raiting this student ")

    def max_grabe_students(self):
        '''This function show best and worse students and show average grape'''
        if self.list_of_dict_about_students == []:
            return (f'Not students ')
        else:
            all_grapers = []
            for i in self.list_of_dict_about_students:
                if len(i['grapes']) != 0:
                    all_grapers.extend(i['grapes'])
        print(f'Average grape for student groop {round(sum(all_grapers) / len(all_grapers), 2)}')

        new_dict_for_stydent = [
            {
                'name': x['name'],
                'average': round(sum(x['grapes']) / len(x['grapes']), 2)
            }
            for x in self.list_of_dict_about_students
            if len(x['grapes']) > 0
        ]

        best = max(new_dict_for_stydent, key=lambda x: x['average'])
        worst = min(new_dict_for_stydent, key=lambda x: x['average'])

        print(f"Best  - {best['name']}  - average {best['average']}")
        print(f"Worst - {worst['name']} - average {worst['average']}")
        return ('----')


def check_of_number(number: int):
    ''' This program check true is number or not'''
    while True:

        try:
            return int(number) and 1 <= int(number) <= 5
        except ValueError:
            number = input('Enter number please ')


class menu:
    '''This class create interfase for this program and doing all activites '''

    def __init__(self):
        self.menu = {1: 'add new student', 2: 'Add grapes for student', 3: 'Show report (all students)',
                     4: ' Find top perfoment', 5: 'Exit'}
        self.list_st = Student_list()

    def shove_menu(self):
        '''Show boss menu for this programm'''
        for i in self.menu:
            print(f'{i}. {self.menu[i]}')


def check_of_number(number: int):
    ''' This program check true is number or not'''
    while True:

        try:
            return int(number) and 1 <= int(number) <= 5
        except ValueError:
            number = input('Enter number please ')


print('Hello this program about student ')
print('Work menu ')
work1 = menu()
work1.shove_menu()
choise_user = check_of_number(input('Enter number 1-5 Your choise '))
while choise_user != 5:
    corect_choise = [1, 2, 3, 4, 5]
    if choise_user == 1:
        work1.list_st.add_new_student_in_list_of_students()
        print('---')

    if choise_user == 2:
        work1.list_st.add_extra_grape_students(input('Enter name student how you wont add grapes '))
        print('---')
    if choise_user == 3:
        work1.list_st.showe_Student_and_his_grapes_all()
        print('---')
    if choise_user == 4:
        print(work1.list_st.max_grabe_students())
        print('---')

    work1.shove_menu()
    choise_user = int(input('Enter number 1-5 Your choise '))
print('Good bay naise to meet you :) ')
