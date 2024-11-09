from time import time
from PIL import Image

class Screen:
    def __init__(self):
        self.updated = None
        self.array = None
    
    def update(self, array):
        self.updated = time()
        self.array = array.copy()
    
    def get_stable(self):
        while not self.updated or self.updated + 0.5 > time():
            pass
        return self.array
    
    def save_stable(self, filename):
        with open(filename, 'wb') as f:
            Image.fromarray(self.get_stable(), 'RGB').save(f, 'BMP')