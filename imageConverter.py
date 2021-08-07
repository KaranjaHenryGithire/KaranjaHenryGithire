from PIL import Image
#pip install Pillow

img= Image.open("IMG_7019")
blackAndWhite = img.convert("L")
blackAndWhite.show()