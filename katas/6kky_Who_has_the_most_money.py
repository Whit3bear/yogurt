""" You're going on a trip with some students and it's up to you to keep track of how much money each Student has. A student is defined like this:

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. If every student has the same amount, then return "all".

Notes:

    Each student will have a unique name
    There will always be a clear winner: either one person has the most, or everyone has the same amount
    If there is only one student, then that student has the most money

 """
import operator

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

def most_money(students):
    
    d = {x.name: (x.fives * 5 + x.tens * 10 + x.twenties * 20) for x in students}              
    v = list(d.values())    
    if v.count(max(v)) > 1:
        return "all"
    return max(d, key=lambda key: d[key]) 

phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)

#Test.assert_equals(most_money([cam, geoff, phil]), "Phil")
print(most_money([cam, geoff]))
# "all"
#Test.assert_equals(most_money([geoff]), "Geoff")