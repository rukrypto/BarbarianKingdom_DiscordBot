#url = "https://assets.albiononline.com/assets/images/killboard/gear.png?u90a4772a"
url = "https://www.mediafire.com/convkey/fa3b/n1lw1ua3qrdthdnzg.jpg"

#color rgb((226, 191, 155))


from PIL import Image
import requests
from io import BytesIO

response = requests.get(url)
img = Image.open(BytesIO(response.content))
#img.show()



#img = Image.open('/path/to/file', 'r')
img_w, img_h = img.size
background = Image.new('RGBA', (480, 520), (226, 191, 155, 0))
bg_w, bg_h = background.size
offset = (0, 0)
background.paste(img, offset)
background.save('out.png')

