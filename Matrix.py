import pygame

class Matrix:

    def __init__(self):
        self.width = 60
        self.height = 40
        self.matrix = []
        self.create_matrix()
        print("Mat Initialized!")

    def create_matrix(self):
        for row in range(self.height):
            new_row = []
            for col in range(self.width):
                new_row.append((100,100,100))
            self.matrix.append(new_row)

    def draw_whole_matrix(self):
        from Visualizer import screen
        for row in range(self.height):
            for col in range(self.width):
                print(f"({col},{row})")
                circle_center = (10 + col * 640 / 61, 10 + row * 480 / 41)
                pygame.draw.circle(screen, self.matrix[row][col], circle_center, 2)