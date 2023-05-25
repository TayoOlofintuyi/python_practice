from PIL import Image, ImageEnhance

class imageman:

    def __init__(self) -> None:
        pass

if __name__ == '__main__':
    #im = imageman()
    img = Image.open(".\images\download.jpg")
    newsize = (300, 300) 
    img = img.resize(newsize) 
    enhancer = ImageEnhance.Brightness(img) 
    img_light = enhancer.enhance(1.8) 
    img_light.save("images/doesthiswork.jpg")




