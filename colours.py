class ColourConverter:
    def __init__(self):

        self.col_num_dict = {
            "wall": (0, 0, 0),
            "empty": (230, 230, 230),
            "end": (255, 0, 0),
            "start": (0, 0, 255),
            "checking": (0, 255, 0),
            "checked": (255, 255, 0),
            "path": (255, 0, 255),
        }
        self.num_col_dict = {v: k for k, v in self.col_num_dict.items()}

    def get_colour(self, num):
        if num in self.num_col_dict:
            return self.num_col_dict[num]
        else:
            return self.num_col_dict[(0, 0, 0)]

    def get_num(self, col):
        if col in self.col_num_dict:
            return self.col_num_dict[col]
        else:
            return self.col_num_dict["wall"]
