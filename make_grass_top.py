from PIL import Image
import random

size = 64
img = Image.new("RGB", (size, size))
pixels = img.load()

for y in range(size):
    for x in range(size):
        # Base green
        r = random.randint(20, 60)
        g = random.randint(120, 200)
        b = random.randint(20, 60)

        # Add darker pixel noise
        if random.random() < 0.1:
            r -= 20
            g -= 30
            b -= 20

        pixels[x, y] = (r, g, b)

img.save("grass_top.png")
print("grass_top.png created!")