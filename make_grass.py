from PIL import Image
import random

size = 64
img = Image.new("RGB", (size, size))
pixels = img.load()

for y in range(size):
    for x in range(size):

        if y < 16:
            # Grass top (with pixel variation)
            r = random.randint(30, 60)
            g = random.randint(140, 200)
            b = random.randint(30, 60)
            pixels[x, y] = (r, g, b)
        else:
            # Dirt (with pixel variation)
            r = random.randint(90, 140)
            g = random.randint(50, 90)
            b = random.randint(0, 30)
            pixels[x, y] = (r, g, b)

img.save("grass.png")
print("Textured grass created!")