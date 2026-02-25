from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from opensimplex import OpenSimplex
import random

app = Ursina()

noise = OpenSimplex(seed=random.randint(1, 1000))

player = FirstPersonController()

grass_texture = load_texture('grass_block.png')  # 3x2 atlas
# OR whatever your atlas file is called

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=grass_texture,
            color=color.white,
            highlight_color=color.lime
        )

# Generate terrain
for z in range(20):
    for x in range(20):
        height = int(noise.noise2(x*0.1, z*0.1) * 5)

        for y in range(height):
            Voxel(position=(x,y,z))

app.run()