from PIL import Image

def make_opaque(filename):
    img = Image.open(filename)

    if img.mode == "RGBA":
        background = Image.new("RGB", img.size, (255, 255, 255))  # white background
        background.paste(img, mask=img.split()[3])  # use alpha channel
        new_name = filename.replace(".png", "_fixed.png")
        background.save(new_name)
        print(f"Saved fixed file as {new_name}")
    else:
        print(f"{filename} has no transparency.")

# Fix your textures
make_opaque("brick.png")
#make_opaque("grass.png")
#make_opaque("stone.png")
#make_opaque("wood.png")