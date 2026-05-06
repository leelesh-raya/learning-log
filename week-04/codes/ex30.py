import numpy as np

color = np.dtype([("r", np.ubyte),
                  ("g", np.ubyte),
                  ("b", np.ubyte),
                  ("a", np.ubyte)])

# create a single color
pixel = np.array((255, 128, 0, 255), dtype=color)
print(pixel)              # (255, 128, 0, 255)
print(pixel["r"])         # 255 — access by field name
print(pixel["g"])         # 128
print(pixel.itemsize)     # 4 bytes total

# create an image — array of pixels
image = np.zeros((100, 100), dtype=color)
image["r"] = 255          # set all red channels to 255
image["a"] = 255          # set all alpha channels to 255
print(image.shape)        # (100, 100)
print(image.dtype)        # shows all four fields