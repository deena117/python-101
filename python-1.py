#name= "Deena"
#print(name)

#books= [1,2,3]
#print(books[0])

# dictionary

student= {"name": "Deena", "age": 35, "subject": "law"}
print(student)
type(student)

person = dict(name= "Charlie", age= 30, city= "London")
print(person)
print(person["city"])

type(person["age"])

person.get("age")
print(person.get("age"))

person["age"]= 32
print(person["age"])

del person["age"]
print(person)

print(student)

x= student.pop("name")
print(x)


