person={"First name": "Aditya","Last Name": "Malode","Born in":"Nashik","curruntly doing":"Student"}
type(person)
print(person["First name"])      #print function is not necessary
print(person["curruntly doing"])

#adding new thing to dictionary
person["Birth year"]="2001"
print(person)

#adding new entity in dict which is a list
person["Skills"]=["Electrical Engineer","Programming","English"]
print(person)

#adding something to a list which is inside the Dict
person["Skills"].append("Java")
print(person)

#what happens if we try to get property which doesnt exists
person.get("College","Not found 404")

#variable associaltion
key="Last Name"
print(person[key])
