#! /bin/python3

# A thief breaks into a spice shop and finds four pounds of saffron, 
# three pounds of vanilla, and five pounds of cinnamon. 
# His backpack fits at most nine pounds, therefore he cannot take everything. 
# Assuming that the prices of saffron, vanilla, and cinnamon are $5000, $200, 
# and $10 per pound, respectively, what is the most valuable loot in this case?


class LootProblem:
    backpack_limit: int
    saffron_pounds: int
    vanilla_pounds: int
    cinnamon_pounds: int

    saffron_price: int
    vanilla_price: int
    cinnamon_price: int

    def __init__(
        self, 
        backpack_limit: int,
        saffron_pounds: int,
        vanilla_pounds: int,
        cinnamon_pounds: int,
        saffron_price: int,
        vanilla_price: int,
        cinnamon_price: int
    ):
        self.backpack_limit = backpack_limit
        self.saffron_pounds = saffron_pounds
        self.vanilla_pounds = vanilla_pounds
        self.cinnamon_pounds = cinnamon_pounds
        self.saffron_price = saffron_price
        self.vanilla_price = vanilla_price
        self.cinnamon_price = cinnamon_price
    
    def take_saffron(self):
        saffron_taken = 0
        while self.saffron_pounds > 0 and self.backpack_limit > 0:
            saffron_taken += 1
            self.backpack_limit -= 1
            self.saffron_pounds -= 1
        return saffron_taken

    def take_vanilla(self):
        vanilla_taken = 0
        while self.vanilla_pounds > 0 and self.backpack_limit > 0:
            vanilla_taken += 1
            self.backpack_limit -= 1
            self.vanilla_pounds -= 1
        return vanilla_taken

    def take_cinnamon(self):
        cinnamon_taken = 0
        while self.cinnamon_pounds > 0 and self.backpack_limit > 0:
            cinnamon_taken += 1
            self.backpack_limit -= 1
            self.cinnamon_pounds -= 1
        return cinnamon_taken

    @property
    def calc_profit(self):
        return (self.take_saffron() * self.saffron_price) + (self.take_vanilla() * self.vanilla_price) + (self.take_cinnamon() * self.cinnamon_price)

    def __str__(self) -> str:
        return f'''
        '''

test = LootProblem(9, 4, 3, 5, 5000, 200, 10)
print(test.calc_profit)

