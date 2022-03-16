import base64
import os
from PIL import Image
from stegano import lsb


def partsize(imgname):
    width, height = Image.open(imgname).size
    numOfPixels = height*width
    size = numOfPixels/4

    return int(size)


def splitFile(fileName, dir):

    file = open(fileName, 'rb')
    isEmpty = False
    parts = []
    imgs = os.listdir(dir)
    imgs.sort()
    index = 0
    while isEmpty == False:
        datasize = partsize(dir+"/"+imgs[index])

        index += 1
        encodedPart = base64.b64encode(file.read(datasize))
        part = encodedPart.decode()
        if not part:
            isEmpty = True
        else:
            parts.append(part)

    return parts


def hide(data: list, dir):
    imgs = os.listdir(dir)
    imgs.sort()

    for i in range(0, len(data)):

        secret = lsb.hide(dir+"/"+imgs[i], data[i])
        secret.save("./secret/"+imgs[i])


def reveal(dirOfImgs, revealedFN):
    imgs = os.listdir(dirOfImgs)
    imgs.sort()

    secret = open(revealedFN, "wb")
    for img in imgs:

        message = lsb.reveal(dirOfImgs+"/"+img)
        message += "==="
        message = base64.b64decode(message)
        secret.write(message)
