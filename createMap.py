from PIL import Image, ImageDraw, ImageFont
import settings
import numToAlpha
import csv

print("Program Start")
#マップサイズ読込
with open(settings.mapFile, encoding="utf_8") as f:
    reader = csv.reader(f)
    l = [row for row in reader]

#print(len(l))
#print(len(l[0]))
xMax = len(l[0])
yMax = len(l)
cellSize = 200
midashiSize = 50
xSize = xMax * cellSize + midashiSize
ySize = yMax * cellSize + midashiSize
lineWidth = 5
fontsize = 40

im = Image.new('RGB', (xSize, ySize), (255, 255, 255))
draw = ImageDraw.Draw(im)
draw.line((0, 0, 0, ySize), fill=(0, 0, 0), width=lineWidth)
draw.line((0, 0, xSize, 0), fill=(0, 0, 0), width=lineWidth)
font = ImageFont.truetype('C:/Windows/Fonts/meiryo.ttc', fontsize)

#升目描画
for x in range(xMax + 1):
    xZahyo = x * cellSize + midashiSize
    draw.line((xZahyo, 0, xZahyo, ySize), fill=(0, 0, 0), width=lineWidth)

for y in range(yMax + 1):
    yZahyo = y * cellSize + midashiSize
    draw.line((0, yZahyo, xSize, yZahyo), fill=(0, 0, 0), width=lineWidth)

#文字描画
num = 1
for x in range(xMax):
    xPoint = midashiSize + (cellSize / 2) + (x * cellSize)
    yPoint = midashiSize / 2
    w, h = draw.textsize(str(num), font)
    #print(w)
    #print(h)

    draw.text((xPoint - (w / 2), yPoint - (h / 2) - 4), str(num), fill=(0, 0, 0), font=font)
    num = num + 1

num = 1
for y in range(yMax):
    xPoint = (midashiSize / 2)
    yPoint = midashiSize + (cellSize / 2) + (y * cellSize)
    alphaNum = numToAlpha.numToAlphaOne(num)
    w, h = draw.textsize(alphaNum, font)
    draw.text((xPoint - (w / 2), yPoint - (h / 2) - 4), alphaNum, fill=(0, 0, 0), font=font)
    num = num + 1

#地形読込
for y in range(yMax):
    for x in range(xMax):
        w, h = draw.textsize(l[y][x], font)
        xPoint = midashiSize + (cellSize / 2) + (x * cellSize)
        yPoint = midashiSize + (cellSize / 2) + (y * cellSize)
        cellFontsize = 200
        font = ImageFont.truetype('C:/Windows/Fonts/meiryo.ttc', cellFontsize)
        draw.text((xPoint - (w / 2), yPoint - (h / 2) - 30), l[y][x], fill=(0, 0, 0), font=font)

im.save('imagedraw.png')
print("Program End")