import pickle
import os


def read_entries():
    file_read = open("db.p", "rb")
    stud = pickle.load(file_read)
    for i in stud['students']:
        print('Stud number: %s Name: %s Group: %s Age: %d'%(stud['students'][i]['number'],
                                                            stud['students'][i]['name'],
                                                            stud['students'][i]['group'],
                                                            stud['students'][i]['age']))
    file_read.close()


def empty_file():
    if os.stat("db.p").st_size == 0:
        return True
    else:
        return False


def check_existence(id):
    if not empty_file():
        file_read = open("db.p", "rb")
        stud = pickle.load(file_read)
        file_read.close()
        count = 0
        for i in stud['students']:
            if stud['students'][i]['number'] == id:
                count+=1
        if count == 0:
            return False
        else:
            return True
    return False


def menu():
    choice = '0'
    while choice != '6':

        print()
        print("Main Choice: Choose 1 of 4 choices")
        print("1.Add students")
        print("2.Delete student")
        print("3.Find student")
        print("4.Display all students")

        choice = input("Please make a choice: ")
        print()

        if choice == "1":
            if empty_file():
                student_arr = {'students': {}}
                max_id = 0
            else:
                file_read = open("db.p", "rb")
                stud = pickle.load(file_read)
                student_arr = stud
                max_id = max(student_arr['students'].keys())
                file_read.close()

            n_students = int(input('Number of students: '))
            l_student_num = 0
            while 0 != n_students:
                max_id += 1
                temp = {}
                student = input("Student number: ")
                if check_existence(student) or student == l_student_num:
                    print('!!!Student number must be unique!!!')
                    break
                l_student_num = student
                temp.update({'number': student})
                student = input("Name: ")
                temp.update({'name': student})
                student = input("Group: ")
                temp.update({'group': student})
                student = int(input("Age: "))
                temp.update({'age': student})
                student_arr['students'][max_id] = temp
                n_students -= 1

            file_write = open("db.p", "wb")
            pickle.dump(student_arr, file_write)

            file_write.close()

            print('Success!')
            print()
            op = input('Wanna continue?')
            if op == 'N' or op == 'n':
                break
        elif choice == "2":
            if empty_file():
                print('There are no entries!')
            else:

                file_read = open("db.p", "rb")
                stud = pickle.load(file_read)
                number = input('Delete student with number: ')
                
                for id in stud['students']:
                    if stud['students'][id]['number'] == number:
                        del stud['students'][id]
                        print('Success!')
                        break

                file_write = open("db.p", "wb")
                pickle.dump(stud, file_write)
                file_read.close()
                file_write.close()

                print()
                op = input('Wanna continue?')
                if op == 'N' or op == 'n':
                    break
        elif choice == "3":

            if empty_file():
                print('There are no entries!')
            else:
                file_read = open("db.p", "rb")
                stud = pickle.load(file_read)
                file_read.close()
                number = input('Please enter student number: ')
                for i in stud['students']:
                    if stud['students'][i]['number'] == number:
                        print('Number: %s Name: %s Age: %d'%(stud['students'][i]['number'],
                                                            stud['students'][i]['name'],
                                                            stud['students'][i]['age']))
                        break

                print()
                op = input('Wanna continue?')
                if op == 'N' or op == 'n':
                    break
        elif choice == "4":
            if empty_file():
                print('There are no entries!')
            else:
                read_entries()
                print()
                op = input('Wanna continue?')
                if op == 'N' or op == 'n':
                    break
        else:
            print("EXIT")


menu()