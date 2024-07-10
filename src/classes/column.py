
class Column:
    def __init__(self, name, tasks=None):
        self.name = name[:30]
        self.tasks = tasks if tasks else []
