import os
import pickle
from typing import Dict
import collections
from collections import defaultdict


DB_FILE_NAME = 'students.mkdb'
ID_INDEX_FILE_NAME = 'students_id.mkindex'
EMAIL_INDEX_FILE_NAME = 'students_email.mkindex'

students = []
index = {'id': defaultdict(list), 'email': defaultdict(list)}

# save students' database in collection


def open_id_index():
    try:
        index['id'] = pickle.load(open(ID_INDEX_FILE_NAME, 'rb'))
    except FileNotFoundError:
        save_id_index()


def open_email_index():
    try:
        index['email'] = pickle.load(open(EMAIL_INDEX_FILE_NAME, 'rb'))
    except FileNotFoundError:
        save_id_index()


def open_database() :
    global students
    try:
        students = pickle.load(open(DB_FILE_NAME, 'rb'))
    except FileNotFoundError:
        save_database()


def save_database():
    global students
    pickle.dump(students, open(DB_FILE_NAME, 'wb'))


def save_id_index():
    pickle.dump(index['id'], open(ID_INDEX_FILE_NAME, 'wb'))


def save_email_index():
    pickle.dump(index['email'], open(EMAIL_INDEX_FILE_NAME, 'wb'))


def update(newdata, params):
    for student in students:
        if all([student[param] == params[param] for param in params]):
            index['id'][student['id']].remove(student)
            index['email'][student['email']].remove(student)
            for i in newdata:
                student[i] = newdata[i]

            index['id'][student['id']].append(student)
            index['email'][student['email']].append(student)

    save_database()
    save_id_index()
    save_email_index()

def search(**params):

    if not params:
        return students
    result = []

    for key, value in params.items():
        if key in index:
            result += index[key][value]
            del params[key]
            break

    result2 = result[:]

    for element in result:
        for key, value in params.items():
            if element[key] != value:
                print("removed:", key, value)
                result2.remove(element)

    return result2



def delete(**params):
    lst = []
    for student in students:
        if all([student[param] == params[param] for param in params]):
            lst.append(student)
    for student in lst:
        students.remove(student)

        index['id'][student['id']].remove(student)
        index['email'][student['email']].remove(student)



    save_id_index()
    save_email_index()
    save_database()


def insert(**params):

    students.append(params)
    save_database()
    index['id'][params['id']].append(params)
    index['email'][params['email']].append(params)

    save_id_index()
    save_email_index()



open_id_index()
open_email_index()
open_database()

#insert(id=1240, name= 'Ivan Us', email='usivan@yahoo.com')

#print(new_search(id=1239, email='a.shevch@yahoo.com'))
