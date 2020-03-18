# class game:  #class类
#     def __init__(self,name,sex,age,power):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.power = power
# A = game("仓",'F',18,1000)
# print(A.name,A.sex,A.age,A.power)
#
# B = game('东','M',99,1800)
# print(B.name,B.sex,B.age,B.power)
#
#
# C = game('波','F',19,2500)
# print(C.name,C.sex,C.age,C.power)
#
# class scenes:
#     def __init__(self,fight,consumption):
#         self.fight = fight
#         self.consumption =consumption
#
# study = scenes('class',-200)
# read  = scenes('library',+100)
# writing = scenes('lab',-500)

class Person:
    def __init__(self,na,gen,age,fig):
        self.name = na
        self.gender = gen
        self.age = age
        self.fight = fig

    def grassland(self):
        self.fight = self.fight - 200

    def practice(self):
        self.fight = self.fight + 200

    def incest(self):
        self.fight = self.fight - 500

    def detail(self):




