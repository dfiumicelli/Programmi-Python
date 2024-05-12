import numpy as np
from scipy import ndimage, misc
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# Visualizzazione di un'immagine
f_rgb = misc.face()
print("Shape: ", f_rgb.shape)
print("Type: ", type(f_rgb))
plt.imshow(f_rgb)
plt.show()

# Indexing e Slicing su Immagini
f = misc.face(gray=True).astype(float)
plt.imshow(f, cmap=plt.cm.gray)
plt.show()
plt.imshow(f[20:150, 30:300], cmap=plt.cm.gray)
plt.show()
f_modified = f.copy()
f_modified[20:150, 30:300] = 255
plt.imshow(f_modified, cmap=plt.cm.gray)
plt.show()

# Trasformazioni su immagini
fig, ax = plt.subplots(5)
ax[0].imshow(f, cmap=plt.cm.gray)
ax[0].set(title="Immagine originale")
ax[1].imshow(f[20:200, 40:400], cmap=plt.cm.gray)
ax[1].set(title="Immagine croppata")
f_flipped = np.flip(f)
ax[2].imshow(f_flipped, cmap=plt.cm.gray)
ax[2].set(title="Mirror rispetto all'asse x")
ax[3].imshow(ndimage.rotate(f, 45), cmap=plt.cm.gray)
ax[3].set(title="Rotazione di 45°")
ax[4].imshow(ndimage.rotate(f, 45, reshape=False),
             cmap=plt.cm.gray)
ax[4].set(title="Rotazione di 45° (senza reshape)")
plt.show()

# Istogramma di un'immagine
istogramma = np.histogram(f, bins=np.arange(256))
plt.bar(istogramma[1][:-1], istogramma[0])
plt.show()

# Applicazione di operatori puntuali su immagini
fig2, ax2 = plt.subplots(4)
ax2[0].imshow(f, cmap=plt.cm.gray)
ax2[0].set(title="Immagine originale")
f_light = f.copy().astype("int32")
f_light +=40
np.clip(f_light, 0, 255, out=f_light)
f_light = f_light.astype("uint8")
ax2[1].imshow(f_light, cmap=plt.cm.gray)
ax2[1].set(title="Immagine con intensità +40")
f_dark = f.copy().astype("int32")
f_dark -=40
np.clip(f_dark, 0, 255, out=f_dark)
f_dark = f_dark.astype("uint8")
ax2[2].imshow(f_dark, cmap=plt.cm.gray)
ax2[2].set(title="Immagine con intensità -40")
f_contrasto = f.copy().astype("float32")
f_contrasto *=1.2
np.clip(f_contrasto, 0, 255, out=f_contrasto)
f_contrasto = f_contrasto.astype("uint8")
ax2[3].imshow(f_contrasto, cmap=plt.cm.gray)
ax2[3].set(title="Immagin con contrasto *1.2")
plt.show()

# Operatori locali: blurring
fig3, ax3 = plt.subplots(2)
blurred_image = ndimage.gaussian_filter(f, sigma=7)
ax3[0].imshow(f, cmap=plt.cm.gray)
ax3[0].set(title="Immagine originale")
ax3[1].imshow(blurred_image, cmap=plt.cm.gray)
ax3[1].set(title="Immagine Blurred")
plt.show()

# Operatori locali: sharpening
fig4, ax4 = plt.subplots(3)
ax4[0].imshow(f, cmap=plt.cm.gray)
ax4[0].set(title="Immagine originale")
blurred_image = ndimage.gaussian_filter(f, sigma=5)
ax4[1].imshow(blurred_image, cmap=plt.cm.gray)
ax4[1].set(title="Immagine Blurred")
blurred_image_sigma_1 = ndimage.gaussian_filter(blurred_image, sigma=1)
alpha = 30
sharp = blurred_image + alpha*(blurred_image - blurred_image_sigma_1)
ax4[2].imshow(sharp, cmap=plt.cm.gray)
ax4[2].set(title="Immagine Sharpened")
plt.show()

# Operatori locali: denoising
fig5, ax5 = plt.subplots(3)
ax5[0].imshow(f, cmap=plt.cm.gray)
ax5[0].set(title="Immagine originale")
f_with_noise = f + 0.9 *f.std()*np.random.random(f.shape)
ax5[1].imshow(f_with_noise, cmap=plt.cm.gray)
ax5[1].set(title="Immagine con rumore")
image_denoised = ndimage.gaussian_filter(f_with_noise, sigma=2)
ax5[2].imshow(image_denoised, cmap=plt.cm.gray)
ax5[2].set(title="Immagine Denoised")
plt.show()

# Operatori locali: edge detection
fig6, ax6 = plt.subplots(2)
ax6[0].imshow(f, cmap=plt.cm.gray)
ax6[0].set(title="immagine originale")
x = ndimage.sobel(f, axis=0, mode='constant')
y = ndimage.sobel(f, axis=1, mode='constant')
Sobel = np.hypot(x, y)
ax6[1].imshow(Sobel, cmap=plt.cm.gray)
ax6[1].set(title="Edge dell'immagine")
plt.show()






