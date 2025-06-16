from PIL import Image

img = Image.open("a.jpg")
img.show()

print('Image size:', img.size)
print('Image Format:', img.format)
print('Image mode:', img.mode)

resized = img.resize((200, 200))
resized.show()

rotated = img.rotate(90)
rotated.show()

gray = img.convert('L')
gray.show()

gray.save('gray_sample.jpg')