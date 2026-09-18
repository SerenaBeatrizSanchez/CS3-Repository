#COMPOSITION
class Nucleus:
    def __init__(self):
        print("Nucleus is created")
    def __del__(self):
        print("Nucleus is gone")
        
class Mitochondria:
    def __init__(self):
        print("Mitochondria is created")
    def providePower(self):
        print("Mitochondria is powering the cell")
    def __del__(self):
        print("Mitochondria is gone")

class Cell:
    def __init__(self):
        print("Cell is created")
        self.nucleus = Nucleus()
        self.mitochondria = Mitochondria()
    def exist(self):
        print("Cell is existing")
        self.mitochondria.providePower()
    def __del__(self):
        del self.nucleus
        del self.mitochondria
        print("Cell is gone")

cellAtWork = Cell()
cellAtWork.exist()
del cellAtWork
