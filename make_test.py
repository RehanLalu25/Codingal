from PIL import Image, ImageDraw

# Create base dirt texture
img = Image.new("RGB", (64, 64), (120, 72, 0))  # brown dirt
draw = ImageDraw.Draw(img)

# Draw green grass on the top portion
draw.rectangle([0, 0, 63, 15], fill=(50, 200, 50))  # top strip green

# Optional: add darker grass line for detail
draw.line((0, 15, 63, 15), fill=(30, 150, 30), width=2)

img.save("grass.png")

print("Grass texture created!")