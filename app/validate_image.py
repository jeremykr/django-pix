from PIL import Image

accepted_formats = ['BMP', 'JPEG', 'PNG']

def valid_image(f):
    try:
        img = Image.open(f)
        return img.format in accepted_formats
    except:
        return False