#importing the random module
import random

#creates a list with all the students from 204
students = ["Jannette",
"Jason",
"Matthew",
"Tamjidur",
"Sarah",
"Solmaz",
"Tasnim",
"Victorita",
"Yasmina",
"Jonathan",
"Aakash",
"Abdullah",
"Ekaterina",
"Faiz",
"James"]

#creates a new list where the random order will be assigned to
order = []

while len(students) != len(order):      #this checks that the length of order is equal to the length of students
    a = random.choice(students)         #generates a random student from our list
    if a in order:                      # if student already in order pass
        pass
    else:
        order.append(a)                 #if student not in order then add them to our list

print(order)                            #print the list


#created by Jonathan, Aakash, James, Faiz and Sarah


