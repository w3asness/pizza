from PizzaStore import PizzaStore
from NYStyleCheesePizza import NYStyleCheesePizza


class NYPizzaStore(PizzaStore):
    def createPizza(self, item):
        if item == 'cheese':
            return NYStyleCheesePizza()
        else:
            return None
