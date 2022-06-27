class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def perimetr(self):
        return 2 * (self.length + self.width)
    
    def area(self):
        return self.length * self.width
    
    def show_info(self):
        print(f'Length of rectangle is: {self.length}')
        print(f'Width of rectangle is: {self.width}')
        print(f'Perimetr is: {self.perimetr()}')
        print(f'Area of rectangle is: {self.area()}')

class Paralelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height
        
    def volume(self):
        return self.length*self.width*self.height
            
        
my_rectangle = Rectangle(2, 5)
my_rectangle. show_info()
my_paralelepiped = Paralelepiped(2, 5, 10)
print(f'Volume of papalelepiped is: {my_paralelepiped.volume()}')