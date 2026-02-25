#create class
class Parrot:
    #class attribute
    species = "bird"
# instance attibutes
    def __init__(self,name,age):
        self.name = name
        self.age = age
blublu = Parrot("blublu ", 10)
woowoo = Parrot("woowoo ", 15)
#access the class attributes
print("blublu is a {}". format(blublu.species))
print("woowoo is a {}". format(woowoo.species))
#access the instance attributes
print("{} is {} years old!".format(blublu.name,blublu.age))
print("{} is {} years old!".format(woowoo.name,woowoo.age))