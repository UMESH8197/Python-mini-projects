# Convert Image to Array using Python
from PIL import Image
image = Image.open('umesh.png')
from numpy import asarray
data = asarray(image)
print(data)