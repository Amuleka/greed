from game.casting.actor import Actor
# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    def __init__(self):
        super().__init__()

    def calculate_points(self):
        points = 0

        if (self.get_text() == '*'):
            points = 1
        else:
            points = -1

        return points
    
