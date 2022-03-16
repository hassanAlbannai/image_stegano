from functions import splitFile, hide, reveal


data = splitFile("slide.ppt", "./original")
hide(data, "./original")
reveal("./secret", "revealed.ppt")
