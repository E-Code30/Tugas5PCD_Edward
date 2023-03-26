import colorsys

R, G, B = 255, 165, 0

H, S, V = colorsys.rgb_to_hsv(R/255.0, G/255.0, B/255.0)

print("Warna RGB ({}, {}, {}) diubah menjadi HSV ({:.2f}, {:.2f}, {:.2f})".format(R, G, B, H, S, V))
