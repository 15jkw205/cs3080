class Car:
    
    wheels = 4
    # color = 'blue'
    
    
    def __init__(self, custom_color='black', cylinders=8):
        
        self.__color = custom_color
        # self.set_cylinders(cylinders)
        
    
    def set_color(self, color):
        self.color = color
        
        
    def report(self):
        print("The car's color is", self.__color)
        print("The car has", Car.wheels, "wheels.")
        print()
        
        
    def Car():
       self.color = 'black'
       
       
    def __str__(self):
        
        s = 'VEHICLE REPORT\n'
        s += "COLOR: %s\n" % (self.__color)
        s += "WHEELS: %s\n" % (Car.wheels)
       # s += "CYLINDERS: %s\n" % (self.get_cylinders()) 
        s += '\n'
        return s
        
        
if __name__ == '__main__':
    
    moms_car = Car('green')
    moms_car.report()

    moms_car.set_color('red')
    moms_car.report()

    dads_car = Car()
    dads_car.report()
