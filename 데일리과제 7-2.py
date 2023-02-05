# class Doggy():
#     num_of_dogs = 0
#     birth_of_dogs = 0

#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#         Doggy.num_of_dogs += 1
#         Doggy.birth_of_dogs += 1

#     def __del__(self):
#         Doggy.num_of_dogs -= 1
#         print(f'{self.name}(이)가 별로 돌아갔습니다.')

#     def bark(self):
#         print('멍멍 으르릉 왈왈')

#     def get_status(self):
#         return Doggy.num_of_dogs, Doggy.birth_of_dogs
    
# p1 = Doggy('치와와','리트리버')
# p2 = Doggy('얼룩이','시츄')
# p1.bark()
# print(p1.get_status())
# del p2
# print(p1.get_status())

class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
        print(f'{self.name}({self.breed}) 태어남')

    def __del__(self):
        Doggy.num_of_dogs -= 1 
        return f'{self.name} 하늘나라로 ㅠㅠㅠ'

    def bark(self):
        print(f'{self.name} 멍멍 으르릉 왈왈')

    @classmethod
    def get_status(cls):
        print(f'태어남 : {cls.birth_of_dogs}, 현재 : {Doggy.num_of_dogs}')

d1 = Doggy('감자','말티즈')
d2 = Doggy('고구마','똥개')
Doggy.get_status()
# d1.bark()
# d2.bark()
del d2
Doggy.get_status()
d3 = Doggy('옥수수','불독')
Doggy.get_status()
