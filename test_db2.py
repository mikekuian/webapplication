import collections
import time

start_time = time.time()

students = [{'id': 1200, 'first_name': 'John', 'last_name': 'Doe', 'age': 23},
            {'id': 1201, 'first_name': 'Ivan', 'last_name': 'Petrov', 'age': 33},
            {'id': 1202, 'first_name': 'Tom', 'last_name': 'Sawyer', 'age': 18},
            {'id': 1203, 'first_name': 'Joe', 'last_name': 'Diestel', 'age': 22},
            {'id': 1204, 'first_name': 'John', 'last_name': 'Nash', 'age': 21},
            {'id': 1205, 'first_name': 'Tom', 'last_name': 'Cat', 'age': 24},
            {'id': 1206, 'first_name': 'Oliver', 'last_name': 'Sawyer', 'age': 25}]

# declare variable with index data

def open(key):
    global students
    students_collection = collections.defaultdict(list)
    for _s in students:
        tmp_s = _s[key]
        students_collection[tmp_s].append(_s)

    my_students = {}
    for i, s in students_collection.items():
        my_students[i] = s
    try:
        return my_students
    except KeyError:
        return "identification key error!"


def search(**params):
    global students
    s = collections.defaultdict(list)
    for key, value in params.items():
        for _s in students:
            tmp_s = _s[key]
            s[tmp_s].append(_s)
    my_students = {}
    for i, s in s.items():
        my_students[i] = s
    try:
        return my_students[value]

    except KeyError:
        return "student not found"

def fibonacci(n):

    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fib(N):
    cache = {}
    def recur_fib(N):
        if N in cache:
            return cache[N]

        if N < 2:
            result = N
        else:
            result = recur_fib(N-1) + recur_fib(N-2)

        # put result in cache for later reference.
        cache[N] = result
        return result

    return recur_fib(N)

print("----------------------------------")

print(fibonacci(50))

print("--- %s seconds ---" % (time.time() - start_time))
