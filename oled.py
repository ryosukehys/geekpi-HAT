import Adafruit_SSD1306 as ssd1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

BUS = 1 
ADDR = 0x3C
RST = None

font = ImageFont.load_default()
font_ttf = '/usr/share/fonts/truetype/kochi/kochi-mincho.ttf'
font = ImageFont.truetype(font_ttf, 15)
oled = ssd1306.SSD1306_128_32(rst=RST, i2c_address=ADDR)

oled.begin()
oled.clear()
oled.display()

width = oled.width
height = oled.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.text((0, 0), "動け!mosaicHAT", font=font, fill=1)

oled.image(image)
oled.display()
