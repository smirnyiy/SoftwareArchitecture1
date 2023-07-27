import inspect
import PoligonalModel

class Id:
    def __init__(self, number):
        self.num = int(number)
        return self.num

class Models:
    def model(self, point):
        if inspect.isclass(PoligonalModel.Poligon) == True:
            poligon = PoligonalModel.Poligon.poligon(PoligonalModel, point)
            texture = PoligonalModel.Texture
            return poligon
        else:
            return False

class Flash:
    def __init__(self):
        import Flash
        flash = Flash
        return flash