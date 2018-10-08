class Car():
    def __init__(self, name, model, makeyear):
        self.name = name
        self.model = model
        self.makeyear = makeyear
        assert self.makeyear <= 2018

    def get_descrptn(self):
     print (self.name, self.model,  self.makeyear)

    @property
    def car_condition(self):

        if self.makeyear > 2016:
            return "Car is in New Condition" + str(self.makeyear) + 'It is smoking hot car'

        elif self.makeyear <= 2016 and self.makeyear >= 2013:
            return 'Car is in good condition ' ,self.makeyear

        elif self.makeyear < 2012 :
            return 'Car is more than 6 years old', self.makeyear

        else:
            return "car is very old", self.makeyear





my_car = Car("Car Info:" + 'Maruti', 'Swift Dzire', 2016)

print(my_car.makeyear)
print(my_car.get_descrptn())

print(my_car.car_condition)
