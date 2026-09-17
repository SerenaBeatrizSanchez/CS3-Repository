class Glassware:
    def __init__(self,kindofglassware):
        self.kindofglassware = kindofglassware
        
class Beaker(Glassware):
    def __init__(self,kindofglassware):
        super().__init__(kindofglassware)
        print("I have five beakers.")
    def __del__(self):
        print("The five beakers are gone.")
        
class Tray:
    def __init__(self):
        print("Tray is existing.")
        self.beaker = Beaker(Glassware)
    def __del__(self):
        print("Tray is gone.")
        del self.beaker

tray = Tray()
del tray
