class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.colors = [(0.2, 0.2, 0.3, 1)
                       (0.5, 0.3, 0.0, 1)
                       (0.5, 0.5, 0.2, 1)
                       (0.0, 0.6, 0.0, 1)]
        self.addBlock((0, 10, 0))
    def startNew(self):
        self.land = render.attachNewNode('Land')
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.getColor(position[1])
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
    def loadLand(self, filename):
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in file:
                    for z0 in range(int(x)+1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1
    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]