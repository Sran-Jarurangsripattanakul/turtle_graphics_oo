import turtle
import random


class Shape:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def draw_concentric(self, layers=5, reduction_ratio=0.618):
        current_size = self.size
        current_location = self.location[:]

        for _ in range(layers):
            turtle.penup()
            turtle.goto(current_location[0], current_location[1])
            turtle.setheading(self.orientation)
            turtle.color(self.color)
            turtle.pensize(self.border_size)
            turtle.pendown()
            for _ in range(self.num_sides):
                turtle.forward(current_size)
                turtle.left(360 / self.num_sides)
            turtle.penup()
            turtle.forward(current_size * (1 - reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(current_size * (1 - reduction_ratio) / 2)
            turtle.right(90)
            current_location = [turtle.xcor(), turtle.ycor()]
            current_size *= reduction_ratio

class ArtGenerator:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def get_random_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def create_random_shape(self, num_sides):
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = self.get_random_color()
        border_size = random.randint(1, 3)
        return Shape(num_sides, size, orientation, location, color, border_size)

    def generate_stacked_shape(self, shapes, shape_count=20, sides=None):
        for _ in range(shape_count):
            num_sides = sides if sides else random.randint(3, 5)
            shape = self.create_random_shape(num_sides)
            shapes.append(shape)

    def generate_art(self, choice):
        shapes = []
        if choice == 1:
            self.generate_stacked_shape(shapes, 30, sides=3)
        elif choice == 2:
            self.generate_stacked_shape(shapes, 30, sides=4)
        elif choice == 3:
            self.generate_stacked_shape(shapes, 30, sides=5)
        elif choice == 4:
            self.generate_stacked_shape(shapes, 30)
        elif choice == 5:
            self.generate_stacked_shape(shapes, 30, sides=3)
        elif choice == 6:
            self.generate_stacked_shape(shapes, 30, sides=4)
        elif choice == 7:
            self.generate_stacked_shape(shapes, 30, sides=5)
        elif choice == 8:
            self.generate_stacked_shape(shapes, 30)
        elif choice == 9:
            self.generate_stacked_shape(shapes, 30)

        for shape in shapes:
            if choice == 5 or choice == 6 or choice == 7 or choice == 8:
                shape.draw_concentric(layers=3, reduction_ratio=0.618)
            else:
                shape.draw()
        
        for shape in shapes:
            if choice == 9:
                shape.draw_concentric(layers=random.randint(1,4), reduction_ratio=0.618)
            else:
                shape.draw()
                
        turtle.update()

    def run(self):
        choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
        self.generate_art(choice)
        turtle.done()


gen = ArtGenerator()
gen.run()
