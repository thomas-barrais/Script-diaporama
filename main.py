import os
import time
from PIL import Image

image_rigolote = r"C:\Users\Thoma\OneDrive\Images\Animeaux_Marrant"

image_filenames = os.listdir(image_rigolote)

# Créer une nouvelle image vide de la taille souhaitée
W, H = Image.open(f'{image_rigolote}/{image_filenames[0]}').size
diaporama = Image.new('RGB', (W * len(image_filenames), H))

for i, image_filename in enumerate(image_filenames):
    image = Image.open(f'{image_rigolote}/{image_filename}')
    diaporama.paste(image, (i * W, 0))

diaporama.show()

