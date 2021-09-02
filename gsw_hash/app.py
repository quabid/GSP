from custom_classes.ImageEncryptor import ImageEncryptor as IE
from pathlib import PurePath

ie = IE()

image = 'images/PNGs/female_wizard.png'
fake_path = 'images/JPGs/wizard3.jpg'
image_path = PurePath(image)

results = ie.set_image_path(image)

if results['status']:
    results = ie.encrypt()

    print(results)
else:
    print(results['cause'])
