class Item:
    def __int__(self):
        self.id = None
        self.descr = None
        self.quantity = None
        self.price = None

    def calculate_discounted_price(self):
        if self.quantity == 2:
            self.price = (self.price - 0.1 * self.price)*self.quantity
            print("Final Price:", self.price)

        elif 3 <= self.quantity <= 5:
            self.price = (self.price - 0.15 * self.price)*self.quantity
            print("Final Price:", self.price)

        elif self.quantity > 5:
            self.price = (self.price - 0.25 * self.price)*self.quantity
            print("Final Price:", self.price)








