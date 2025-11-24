class Student_list:
    def __init__(self):
        self.list_of_dict_about_students = []
        self.set_of_students_name = []

    @classmethod
    def check_of_number(self,number: int):
        ''' This program check true is number or not'''
        while True:
            if isinstance(number,str) and number=='stop':
                return 'stop'
            try:
                return int(number)
            except ValueError:
                number = input('Enter number please ')

    @classmethod
    def check_of_two_words(self,string: str):
        ''' This program check true is string (two words) or not (for name of students)'''

        while True:
            if len(string.split()) == 2:
                return string
            else:
                string = input('Enter two words please ')

    def add_new_student_in_list_of_students(self):
        new_students = self.check_of_two_words(input('Enter ferst and second name of student '))
        grade = self.check_of_number(input('Enter one grade or enter stop '))
        list_of_number = []
        while isinstance(grade,int):
            list_of_number.append(grade)

            grade = self.check_of_number(input('Enter one grade or enter stop '))

        self.list_of_dict_about_students.append({'name': new_students, 'grapes': list_of_number})
        self.set_of_students_name.append(new_students)

    def add_extra_grape_students(self, name_student):
        self.check_of_two_words(name_student)
        if name_student in self.set_of_students_name:
            grade = self.check_of_number(input('Enter one grade or enter stop '))
            list_of_number = []
            while grade.lower() != 'stop':
                list_of_number.append(grade)

                grade = self.check_of_number(input('Enter one grade or enter stop '))

            for i in self.list_of_dict_about_students:
                if i['name']==name_student:
                    i['grapes'].update(grade)
        else:
            print('This student not in list ')

    def showe_Student_and_his_grapes_all(self):

        for i in self.list_of_dict_about_students:
            try:
                print(f'* {i.keys()} - {sum(i.values()) / len(i.values())}')
            except ZeroDivisionError:
                print(f'* {i.keys()} - None')

    def max_grabe_students(self):
        print(list(map(lambda i:{i['name']:sum(i.values()) / len(i.values())}, self.list_of_dict_about_students)))


class menu:
    def __init__(self):
        self.menu={1:'add new student',2:'Add grapes for student',3:'Show report (all students)',4:' Find top perfoment',5:'Exit'}
        self.list_st=Student_list()
    def shove_menu(self):
        for i in self.menu:
            print(f'{i}. {self.menu[i]}')


def check_of_number(number: int):
    ''' This program check true is number or not'''
    while True:

        try:
            return int(number) and 1<=int(number)<=5
        except ValueError:
            number = input('Enter number please ')


print('Hello this program about student ')
print('Work menu ')
work1=menu()
work1.shove_menu()
choise_user=int(input('Enter number 1-5 Your choise '))
while choise_user!=5:
    if choise_user==1:
        work1.list_st.add_new_student_in_list_of_students()

    if choise_user==2:
        work1.list_st.add_extra_grape_students(input('Enter name student how you wont add grapes '))

    if choise_user==3:
        work1.list_st.showe_Student_and_his_grapes_all()

    if choise_user==4:
        work1.list_st.showe_Student_and_his_grapes_all()
    work1.shove_menu()
    choise_user = int(input('Enter number 1-5 Your choise '))
print('Good bay naise to meet you :) ')



