import PoligonalModel
import Flash
import Scene
import Camera

class Models:
    def model(self):
        texture = PoligonalModel.Texture
        poligonal = PoligonalModel.Poligon


class Flashes:
    def flash(self):
        flash = Flash


class Scenes:
    def GetScena(self, point):
        id = Scene.Id
        model = Scene.Models.model(PoligonalModel, point)
        flash = Scene.Flash

class Cameras:
    def camera(self):
        camera = Camera

class changeObservers:
    import IModelChangedObserver
    __change = IModelChangedObserver

    def __init__(self, change):
        self.__change = change

    def __displayDetails(self):
        return self.__change

    def accessPrivateFunction(self):
        self.__displayDetails()