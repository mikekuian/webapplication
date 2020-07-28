import collections
import time
start_time = time.time()

students = [{'first_name':'John','last_name': 'Doe','age': 23}, {'first_name':'Ivan','last_name':'Petrov','age': 33},
{'first_name':'Tom','last_name':'Sawyer','age': 18}, {'first_name':'Joe','last_name': 'Diestel','age': 22},
{'first_name':'John','last_name': 'Nash','age': 21},
{'first_name':'Tom','last_name': 'Cat','age': 24}, {'first_name':'Oliver','last_name': 'Sawyer','age': 25}]

# full scan

target_last_name = 'Cot'
for student in students:
    if student['last_name'] == target_last_name:
        break
else:
    print('not found')

print(student)

print("--- %s seconds ---" % (time.time() - start_time))