# #Part I
# students = [                                                # "students" => list
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},    # index 0
#      {'first_name' : 'John', 'last_name' : 'Rosales'},      # index 1
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},      # index 2
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}           # index 3
# ]

# def FirstLast(lst):
#     dic = {}
#     for i in lst:   #for each index in the variable "lst"
#         dic = i     #variable dic will contain each item of the array
#         print dic['first_name'], dic['last_name']   # this calls each index with the key so that it prints the data
# FirstLast(students)


# #Alternative Part I
# def show_students(arr):
#     for student in students:
#         print student['first_name'], student['last_name']
# show_students(studnets)



# sudo
# keys** = first_name, last_name
# values** = first (Michael, John, Mark, KB); last (Jordan, Rosales, Guillen, Tonel)
# print students[0]['first_name'] , students[0]['last_name']


#Part II
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def nameCount(data):
    for i in data:          # index is accessing the "users dictionary"
        print i             # print the key "Students, Instructors"
        count = 1           # count on the left, numerical order

        for x in data[i]:   # x is now accessing the data at whatever [i]. Which goes to the key that is associated to each value.
            namelen = len(x['first_name']) + len(x['last_name'])       #taking the character length of each value 
            print count, "-", x['first_name'], x['last_name'], "-", namelen
            count += 1
nameCount(users)