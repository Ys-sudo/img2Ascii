
# best with larger screen or phone sideways

import requests
from io import BytesIO


from PIL import Image

response = requests.get("https://66.media.tumblr.com/b412951f278ecbf5cffe39a6eeb12f57/tumblr_mhrl362GJt1s376ugo1_1280.jpg")
image_url = Image.open(BytesIO(response.content))



print(image_url)

ASCII_CHARS = ['0', '?', '%', '.', 'X', '+', '.', 'Z', ':', '1', '@']

def scale_image(image, new_width=100):
    """Resize image preserving the aspect ratio."""
    original_width, original_height = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=25):
    """Map each pixel to an ascii char.

    Based on the range in which the pixel lies. 0-255
    is divided into 11 ranges of 25 pixels each.
    """
    pixels_in_image = list(image.getdata())
    pixels_to_chars = [
        ASCII_CHARS[pixel_value // range_width]
        for pixel_value in pixels_in_image
    ]
    return "".join(pixels_to_chars)


def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image)
    image = convert_to_grayscale(image)
    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)
    image_ascii = [
        pixels_to_chars[index: index + new_width]
        for index in range(0, len_pixels_to_chars, new_width)
    ]
    return "\n".join(image_ascii)


local_image_filename = image_url


image = local_image_filename
image_ascii = convert_image_to_ascii(image)
print(image_ascii)
write: str = image_ascii
text_file = open("/Users/Y-S/Desktop/Output.txt", "w")
text_file.write(str(write))
text_file.close()
