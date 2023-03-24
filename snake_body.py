class snake:
    def __init__(self):
        self.pos_x_1 = 400
        self.pos_y_1 = 400
    @property
    def pos_x_2(self):
        return self.pos_x_1 + 10
    @property
    def pos_y_2(self):
        return self.pos_y_1 + 10
    



