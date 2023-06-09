class Wave:
    def __init__(self):
        from Visualizer import matrix
        self.matrix = matrix
        self.cur_x = 0
        self.direction = "Right"

    def update(self):
        
        col = self.cur_x

        # Draw a line of Pixels
        for row in range(40):
            light_grey = (200,200,200)
            blue = (0,0,255)
            pos = (col, row)

            # Check the color of the pixel at pos and return the opposite.
            if self.matrix.matrix[row][self.cur_x] == light_grey:
                color = blue
            else:
                color = light_grey

            self.matrix.set_pixel_color(pos, color)
            self.matrix.draw_pixel(pos)

        # Update the column which the next iteration of update will redraw

        if self.direction == "Right":
            if self.cur_x < 59:
                self.cur_x += 1
            else:
                self.direction = "Left"
        else:
            if self.cur_x > 0:
                self.cur_x -= 1
            else:
                self.direction = "Right"
    