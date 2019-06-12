class Product:
    number = 0
    def __init__(self):
        Product.number = Product.number+1
    def showNumberOfObjects(self):
        print(Product.number)
p1 = Product()
p2 = Product()
p3 = Product()
p4=p1
p5=p3

p5.showNumberOfObjects()
