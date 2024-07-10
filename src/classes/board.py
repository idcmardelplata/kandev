class BoardConfiguration:
    def __init__(self):
        pass

class Board:
    def __init__(self, name, columns=None, config=None):
        self.name = name
        self.columns = columns if columns else []
        self.config = config if config else BoardConfiguration()
