from PIL import Image, ImageEnhance
#import docker

class imageman:

    def __init__(self) -> None:
        pass

if __name__ == '__main__':
    #im = imageman()
    img = Image.open(".\images\HD-wallpaper-nature-beautiful.jpg")
    newsize = (500, 1000) 
    img = img.resize(newsize) 
    enhancer = ImageEnhance.Brightness(img) 
    img_light = enhancer.enhance(1.7) 
    img_light.save("images/a.jpg")

    changesize = (300, 600)

    img1 = Image.open(".\images\download.jpg").resize(changesize)
    img2 = Image.open(".\images\download2.jpg").resize(changesize)

    img = Image.blend(im1 = img1, im2 = img2, alpha = 0.5)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.5)

    img.save("images/combo.png")




