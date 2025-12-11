from PIL import Image

"""
úkol: udělat for cyklus nad x obrázky a pro všechny udělat thumb (malá varianta)
- mužete vzít pole cest
- nebo lépe: zadat složku a zní vytáhnout všechny jpg, png obrázky

volitelně: get_thumb_path by mohlo obsahovat informaci o velikosti
"""

DEFAULT_SIZE = 320
DEFAULT_THUMB_SIZE = (DEFAULT_SIZE, DEFAULT_SIZE)


def resize_image(path, save_to, size=DEFAULT_THUMB_SIZE):
    image = Image.open(path)
    image.thumbnail(size)
    image.save(save_to)


def get_thumb_path(path, size=DEFAULT_THUMB_SIZE):
    index = path.rindex('.')
    extra_name = '-' + str(size[0]) + 'x' + str(size[1])
    return path[:index] + extra_name + path[index:]


if __name__ == '__main__':
    def main():
        resize_to = (500, 500)

        path = r"C:\Users\suche\Downloads\pexels-stefanstefancik-91227.jpg"
        thumb_path = get_thumb_path(path, resize_to)

        resize_image(path, thumb_path, size=resize_to)
        print('thumb saved into', thumb_path)
        resize_image(path, thumb_path, size=(400, 400))
        resize_image(path, thumb_path, size=(800, 800))
    

    main()

