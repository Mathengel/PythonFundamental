students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def printNames(a):      
    for data in a:
        print data['first_name'], data['last_name']

# printNames(students)

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


def printNamesWithLength(a):      
    
    count = 0;
    for key, data in a.items():
        print key
        for value in data:
            count+=1
            length = len(value['first_name']) + len(value['last_name'])
            print "{} - {} {} - {}".format(count, value['first_name'], value['last_name'], length)


printNamesWithLength(users)

