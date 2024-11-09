# OO code using turtle graphics
- From the starting code, polygon_art.py, you are to write an OO program that generates different pieces of art works
- Fork, then, clone this repo
- Read the instructions given in the course's Google Classroom and start coding
- Once you are done, push your final code to your Github repo and modify this README to report on the work you have done

Report what I done,

Shape Class: Represents a geometric shape with methods to draw it normally (draw()) and draw concentric layers (draw_concentric()).
ArtGenerator Class: Contains methods to create random shapes, generate a set of shapes based on user input, and draw them using turtle graphics.
The draw() method in the Shape class handles single-shape drawing.
The draw_concentric() method handles drawing the shape with multiple concentric layers.
Shapes have properties like the number of sides, size, orientation, location, color, and border size.
Choice 1 to 4: Draws 30 shapes with 3, 4, 5, or random sides (between 3 to 5).
Choice 5 to 8: Draws 30 shapes with concentric layers (triangles, squares, pentagons, or random-sided shapes).
Choice 9: Draws 30 shapes with a variable number of concentric layers randomized between 1 to 4 and random sides between 3 to 5.
The program prompts the user to choose a type of artwork to generate, allowing customization of the shapes and their arrangement.
The generate_stacked_shape() method creates a list of shapes, either of specific types (triangles, squares, pentagons) or with random sides.
The generate_art() method processes the user choice and instructs the Shape instances to draw themselves using the turtle library.
