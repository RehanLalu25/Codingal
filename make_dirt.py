from PIL import Image
import random

size = 64
img = Image.new("RGB", (size, size))
pixels = img.load()

for y in range(size):
    for x in range(size):
        r = random.randint(90, 130)
        g = random.randint(50, 80)
        b = random.randint(20, 40)

        if random.random() < 0.15:
            r -= 20
            g -= 10

        pixels[x, y] = (r, g, b)

img.save("dirt.png")
print("dirt.png created!")