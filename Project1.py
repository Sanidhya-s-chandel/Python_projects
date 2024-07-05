import json 
import string
import random

class R12:
    def randomId(self):
        alpha = random.choices(string.ascii_letters, k = 2)
        num = random.choices(string.digits, k = 4)
        symbol = random.choices("@#$%&*", k = 2)
        id = alpha + num + symbol
        random.shuffle(id)
        return "".join(id)

    def __init__(self,name,age,hobbies):
        self.id = self.randomId()
        self.name = name
        self.age = age
        self.hobbies = hobbies

    def dictionary(self):
        return {"id" : self.id,
        "name" : self.name,
        "age" : self.age,
        "hobbies" : self.hobbies}

class R10(R12):
    def __init__(self,name,age,hobbies):
        super().__init__(name,age,hobbies)

x = int(input("Enter the class in which u have to register : "))

if x == 12:
    y = int(input("Enter the age to check eligibilty : "))
    
    if 16 <= y <= 20:
        name = input("Enter the name : ")
        age = y
        hobbies = input("Enter the hobbies : ")
        obj = R12(name,age,hobbies)
        data = obj.dictionary()

        with open("Students_12.json",'a') as file_12:
            json.dump(data,file_12)
            file_12.write('\n')
    
    else:
        print("You are not eligible for this class...!!")

elif x == 10: 
    y = int(input("Enter the age : "))
    
    if 14 <= y <= 18:
        name = input("Enter the name : ")
        age = y
        hobbies = input("Enter the hobbies : ")
        obj2 = R10(name,age,hobbies)
        data = obj2.dictionary()

        with open("Students_10.json",'a') as file_10:
            json.dump(data,file_10)
            file_10.write("\n")
    
    else:
        print("You are not eligible for this class.....!!")

else:
    print("Please Enter the valid class")