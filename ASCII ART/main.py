import PIL.Image

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]


def resize(image, new_width=600):
    width, height = image.size
    new_height = new_width * height //  (3*width)
    return image.resize((new_width, new_height))


def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str


def converting(path):
    try:
        image = PIL.Image.open(path)
    except:
        print("Couldn't find image")

    image = resize(image)
    grayscale_image = image.convert("L")
    ascii_str = pixel_to_ascii(grayscale_image)

    image_width = grayscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_image = ""

    for i in range(0, ascii_str_len, image_width):
        ascii_image += ascii_str[i:i + image_width] + '\n'

    with open("ascii image.txt", "w") as f:
        f.write(ascii_image)

if __name__ == "__main__":
    path = 'C:\\Users\\tankh\\Downloads\\240131163_890296151617974_1249777102311268015_n.jpg'
    converting(path)
