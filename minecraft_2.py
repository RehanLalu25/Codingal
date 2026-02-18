# import libraries
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from opensimplex import OpenSimplex
import random
import math

# create noise generator
noise = OpenSimplex(seed=random.randint(1, 1000))

# create app
app = Ursina()

selected_block = "grass"

# create player
player = FirstPersonController(
    mouse_sensitivity=Vec2(100, 100),
    position=(0, 20, 0)
)

# textures
block_textures = {
    "grass": load_texture("assets/textures/groundEarth.png"),
    "dirt": load_texture("assets/textures/groundMud.png"),
    "stone": load_texture("assets/textures/wallStone.png"),
    "bedrock": load_texture("assets/textures/stone07.png")
}

# block class
class Block(Entity):
    def __init__(self, position, block_type):
        super().__init__(
            position=position,
            model="assets/models/block_model",
            scale=1,
            origin_y=-0.5,
            texture=block_textures.get(block_type),
            collider="box"
        )
        self.block_type = block_type


# mini block preview
mini_block = Entity(
    parent=camera,
    model="assets/models/block_model",
    scale=0.2,
    texture=block_textures.get(selected_block),
    position=(0.35, -0.25, 0.5),
    rotation=(-15, -30, -5)
)

# generate terrain
min_height = -5
terrain_size = 20

for x in range(-terrain_size, terrain_size):
    for z in range(-terrain_size, terrain_size):

        nx = x * 0.05
        nz = z * 0.05

        # 3-octave noise
        height = (
            noise.noise2(nx, nz) * 1 +
            noise.noise2(nx * 2, nz * 2) * 0.5 +
            noise.noise2(nx * 4, nz * 4) * 0.25
        )

        height = math.floor(height * 8)

        for y in range(height, min_height - 1, -1):

            world_y = y

            if y == min_height:
                Block((x, world_y, z), "bedrock")
            elif y == height:
                Block((x, world_y, z), "grass")
            elif height - y > 2:
                Block((x, world_y, z), "stone")
            else:
                Block((x, world_y, z), "dirt")


# input system
def input(key):
    global selected_block

    # place block
    if key == "left mouse down":
        hit_info = raycast(camera.world_position, camera.forward, distance=8)
        if hit_info.hit:
            Block(hit_info.entity.position + hit_info.normal, selected_block)

    # delete block
    if key == "right mouse down" and mouse.hovered_entity:
        if mouse.hovered_entity.block_type != "bedrock":
            destroy(mouse.hovered_entity)

    # change block type
    if key == "1":
        selected_block = "grass"
    if key == "2":
        selected_block = "dirt"
    if key == "3":
        selected_block = "stone"


def update():
    mini_block.texture = block_textures.get(selected_block)


app.run()
