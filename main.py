class computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

c = computer()
c.sell()

c.maxprice = 1000
c.sell()

c.setMaxPrice(1000)
c.sell()