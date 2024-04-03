class DogRex:
    def __init__(self):
        self.name = 'Rex'
        self.voice = 'bow-wow'
        self.hungry = True

    def feed(self):
        self.hungry = False
    def walk(self):
        self.hungry = True

my_dog = DogRex()   

print('my dog name:', my_dog.name)   
print('my dog voice:', my_dog.voice)  
print('my dog is hungry:', my_dog.hungry)  
my_dog.feed()
print('my dog is hungry:', my_dog.hungry) 
my_dog.walk()
print('my dog is hungry:', my_dog.hungry)  