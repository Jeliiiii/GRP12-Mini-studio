from ..Scene import Scene


class MPScene(Scene):

    def __init__(self, client=None):
        super().__init__()
        self.client = client
        self.data = None

    def updateScene(self, inputs, dt):
        self.client.send(self.client.socket, inputs)
        self.data = self.client.recv(self.client.socket)
