students =  [
    ("Ali", ["Fizika", "Matematika"]),
     ("Laylo", ["Ingliz tili"]), 
     ("Jasur", ["Matematika", "Informatika"])
]

subject = input()

count = 0
for student in students:
    if subject in student[1]:
        count += 1

print(count)