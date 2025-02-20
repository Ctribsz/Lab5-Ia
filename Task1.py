import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import block_reduce

# Cargamos la imagen
image_path = "Test.bmp"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Por si no se logra cargar la imagen
if image is None:
    raise FileNotFoundError(f"No se pudo cargar la imagen en la ruta: {image_path}")

_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
block_size = 10
pixelated_image = block_reduce(binary_image, block_size=(block_size, block_size), func=np.mean)

# Aplicar umbral
pixelated_image = np.where(pixelated_image > 128, 255, 0).astype(np.uint8)

# Guardar la imagen pixelada
cv2.imwrite("pixelated_image.bmp", pixelated_image)

# Mostrar las imágenes originales y pixeladas
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].imshow(binary_image, cmap="gray")
axs[0].set_title("Imagen binarizada")
axs[0].axis("off")

axs[1].imshow(pixelated_image, cmap="gray", vmin=0, vmax=255)
axs[1].set_title("Imagen pixelada")
axs[1].axis("off")

plt.savefig("resultado.png")
