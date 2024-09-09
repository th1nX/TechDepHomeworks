class Person:
    def __init__(self, name: str, age: int, profession: str):
        self.name = name
        self.age = age
        self.profession = profession

    def display_info(self):
        return f"\nPerson name:{self.name}\nPerson age:{self.age}\nPerson profession:{self.profession}"
def main():
    person1 = Person('Jack', 25, 'Programmeer')
    person2 = Person('Amily', 23, 'Web-Designeer')
    print(person1.display_info(), person2.display_info())

if __name__ == "__main__":
    main()

