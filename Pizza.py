class Pizza:
    name: str
    dough: str
    sauce: str
    toppings = []

    def prepare(self):
        print('gotovim', self.name)
        print('Mesim testo...')
        print('Dobavim souse')
        print('dobavim nachinki')
        for t in self.toppings:
            print('\t', t)

            
    def bake(self):
        print('zapekaem 25 min pri 350 gradysah')

    def cut(self):
        print('narezaem pizzy treygolnikami')

    def box(self):
        print('pomeshaem pizzy v firmennyu ypakovky')

    def getName(self):
        return self.name
    
