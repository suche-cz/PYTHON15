# image_resizer.py

from PIL import Image # python -m pip install pillow


class ImageResizer:
    def __init__(self, path):
        self.path = path
        self.image = Image.open(path)
    
    def resize_to(self, size: int):
        thumb = self.image.copy()
        thumb.thumbnail((size, size))
        path = self.get_path(size)
        thumb.save(path)
    
    def get_path(self, size: int):
        index = self.path.rindex('.')
        extra_name = '-' + str(size)
        # \pexels-stefanstefancik-91227.jpg
        # \pexels-stefanstefancik-91227-400.jpg
        # \pexels-stefanstefancik-91227-500.jpg
        # \pexels-stefanstefancik-91227-800.jpg
        return self.path[:index] + extra_name + self.path[index:]


image_paths = [
    r"C:\Users\suche\Downloads\pexels-stefanstefancik-91227.jpg",
    r"C:\Users\suche\Downloads\Gemini_Generated_Image_ld8rgild8rgild8r.png",
]

for image_path in image_paths:
    my_image_resizer = ImageResizer(image_path)
    print(my_image_resizer.image)

    for size in range(100, 1000, 100):
        my_image_resizer.resize_to(size)

    # my_image_resizer.resize_to(500)
    # my_image_resizer.resize_to(800)



class ImageResizer2:
    pass


# takto to chci používat
image_resizer = ImageResizer2()
image_resizer.resize('image1.jpg', 200, 400, 600)
image_resizer.resize('image2.jpg', 400, 600, 800)


class CharCounter:
    """ třída umožní vypočítat počet znaků v txt souboru """


# takto to chci používat
counter = CharCounter('path.txt')
counter.print_info() # 7373 - path.txt

"""
2 způsoby

1. každý obrázek má vlastní ImageResizer

2. ImageResizer dokáže měnit velikost pro různé obrázky

3. WordCounter



"""

