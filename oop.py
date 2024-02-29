class Human:
    def __init__(self, nm, age, h,w ,g, country ):
        self.name = nm
        self.age = age
        self.height = h
        self.weight = w
        self.gender = g
        self.country = country
    def show(self):
        print(f'name:{self.name}')
        print(f'age:{self.age}')
        print(f'height:{self.height}')
        print(f'weight:{self.weight}')

#making objects
        
h1 = Human('ram', 23, 5.6 ,67 ,'m', 'nepal')

h2 = Human('shyam', 25 , 5.5 , 65, 'm', 'india')
print(h1.name)
print(h2.name)
h1.show()
print('_'*15)