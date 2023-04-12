import pygame

class Matrix:

    def __init__(self):
        from Visualizer import screen
        self.width = 60
        self.height = 40
        self.matrix = []
        self.screen = screen
        self.create_matrix()
        print("Mat Initialized!")

    def create_matrix(self):
        for row in range(self.height):
            new_row = []
            for col in range(self.width):
                new_row.append((200,200,200))
            self.matrix.append(new_row)

    def set_pixel_color(self, pos, color):
        col = pos[0]
        row = pos[1]
        self.matrix[row][col] = color

    def draw_whole_matrix(self):
        for row in range(self.height):
            for col in range(self.width):
                print(f"({col},{row})")
                circle_center = (10 + col * 640 / 61, 10 + row * 480 / 41)
                pygame.draw.circle(self.screen, self.matrix[row][col], circle_center, 2)

    def draw_pixel(self, pos):
        col = pos[0]
        row = pos[1]
        circle_center = (10 + col * 640 / 61, 10 + row * 480 / 41)
        pygame.draw.circle(self.screen, self.matrix[row][col], circle_center, 2)