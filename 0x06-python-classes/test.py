class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = person("Zakaria", 23)
print(person.name)
print(person.age)

person.country = "Morocco"
person.job = "Softwarengenyuring"
print(person.country)
print(person.job)