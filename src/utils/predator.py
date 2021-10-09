class Predator:
    def __init__(self, a, b, c, d, name):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.name = name
        self.target_data = None

    def initialize_target_data(self, target_data):
        self.target_data = target_data

    def preprocess_target_data(self):
        if self.target_data is None:
            raise AttributeError("Target data is not initialized.")

        print("Preprocessing .. (transpose)")
        self.target_data = self.target_data.T
