from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager

class Game(ShowBase):
    ShowBase.__init__(self)
    self.land = Mapmanager()
    base.camLens.setFov(90)
    self.land.loadLand('land.txt')
    self.hero = Hero((x, y, z), self.land)




game = Game()
game.run()