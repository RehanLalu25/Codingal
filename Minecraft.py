from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform

app = Ursina()

window.title = "Elemental Survival"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

# ---- PLAYER ----
player = FirstPersonController()
player.gravity = 1
player.cursor.visible = False

Sky()

mouse.locked = True
mouse.visible = False

# ---- CROSSHAIR ----
crosshair = Entity(parent=camera.ui)
Entity(parent=crosshair, model='quad', color=color.white, scale=(0.002, 0.02))
Entity(parent=crosshair, model='quad', color=color.white, scale=(0.02, 0.002))

# ---- WEAPON MODE ----
weapon_mode = "fist"

# ---- FIST ----
fist = Entity(parent=camera.ui,
              model='cube',
              color=color.rgb(255,200,170),
              scale=(0.15,0.2,0.15),
              position=(0.6,-0.5),
              rotation=(0,0,15))

# ---- SWORD ----
sword = Entity(parent=camera.ui,
               position=(0.55,-0.35),
               rotation=(10,-15,25),
               scale=0.9,
               enabled=False)

Entity(parent=sword, model='cube',
       color=color.rgb(120,60,30),
       scale=(0.06,0.25,0.08),
       position=(0,-0.3,0))
Entity(parent=sword, model='cube',
       color=color.dark_gray,
       scale=(0.22,0.05,0.1),
       position=(0,-0.15,0))
Entity(parent=sword, model='cube',
       color=color.light_gray,
       scale=(0.08,0.8,0.1),
       position=(0,0.3,0))

swinging = False

# ---- ENEMY ----
class Enemy(Entity):
    def __init__(self, position=(0,1,5)):
        super().__init__(model='cube', color=color.green, scale=(1,2,1),
                         position=position, collider='box')
        self.health = 60
    def update(self):
        self.look_at(player.position)
        self.position += self.forward * time.dt * 2
        if self.y > 1:
            self.y -= 5 * time.dt
    def take_damage(self, amount):
        self.health -= amount
        self.color = color.red
        invoke(self.reset_color, delay=0.1)
        if self.health <= 0:
            destroy(self)
    def reset_color(self):
        self.color = color.green

enemy = Enemy(position=(5,1,5))

# ---- FIREBALL ----
class Fireball(Entity):
    def __init__(self, position, direction):
        super().__init__(model='sphere', color=color.orange,
                         scale=0.5, position=position, collider='sphere')
        self.direction = direction
        self.speed = 15
        self.life = 3
    def update(self):
        self.position += self.direction * self.speed * time.dt
        self.life -= time.dt
        if self.life <= 0:
            destroy(self)
        if enemy and enemy.enabled:
            if distance(self.position, enemy.position) < 1.5:
                enemy.take_damage(30)
                destroy(self)

# ---- LIGHTNING ----
class Lightning(Entity):
    def __init__(self, position, direction):
        super().__init__(
            model='cube',
            color=color.cyan,
            scale=(0.2,0.2,5),   # long thin bolt
            position=position,
            collider='box'
        )
        self.direction = direction.normalized()
        self.speed = 25
        self.life = 0.2  # short-lived
    def update(self):
        self.position += self.direction * self.speed * time.dt
        self.life -= time.dt
        if self.life <= 0:
            destroy(self)
        if enemy and enemy.enabled:
            if distance(self.position, enemy.position) < 1.5:
                enemy.take_damage(50)
                destroy(self)

# ---- BLOCK TYPES ----
block_types = {'1':'grass.png','2':'stone.png','3':'brick.png','4':'wood.png'}
current_block = block_types['1']
boxes = []

# ---- GROUND ----
for z in range(20):
    for x in range(20):
        box = Button(color=color.white, model='cube', position=(x,0,z),
                     texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(box)

# ---- INPUT ----
def input(key):
    global weapon_mode, swinging
    if key=='escape':
        mouse.locked = not mouse.locked
        mouse.visible = not mouse.visible
    # Switch weapon
    if key=='e':
        if weapon_mode=="fist":
            weapon_mode="sword"
            fist.enabled=False
            sword.enabled=True
        else:
            weapon_mode="fist"
            fist.enabled=True
            sword.enabled=False
    # Fireball
    if key=='f':
        Fireball(position=player.position+Vec3(0,1.5,0),
                 direction=camera.forward)
    # Lightning
    if key=='l':
        Lightning(position=player.position+Vec3(0,1.5,0),
                  direction=camera.forward)
    # LEFT CLICK
    if key=='left mouse down' and not swinging:
        if weapon_mode=="fist":
            if mouse.hovered_entity in boxes:
                box=mouse.hovered_entity
                boxes.remove(box)
                destroy(box)
        if weapon_mode=="sword":
            swinging=True
            sword.animate_rotation((25,-10,-40), duration=0.1)
            invoke(reset_sword, delay=0.15)
            if mouse.hovered_entity==enemy:
                enemy.take_damage(20)
    # PLACE BLOCK
    if mouse.hovered_entity and key=='right mouse down':
        box=mouse.hovered_entity
        new=Button(color=color.white, model='cube',
                   position=box.position+mouse.normal,
                   texture=current_block, parent=scene, origin_y=0.5)
        boxes.append(new)

def reset_sword():
    global swinging
    sword.animate_rotation((10,-15,25), duration=0.1)
    swinging=False

app.run()
