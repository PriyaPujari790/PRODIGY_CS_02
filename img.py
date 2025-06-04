from PIL import Image

# Create a small 100x100 red image
img = Image.new("RGB", (100, 100), color=(255, 0, 0))
img.save("original.png")

print("Test image 'original.png' created successfully.")
