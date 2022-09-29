
from PIL import Image, ImageDraw
import settings

#マップサイズ読込
xMax = settings.xMax
yMax = settings.yMax
cellSize = 100
xSize = xMax * cellSize
ySize = yMax * cellSize
lineWidth = 5

im = Image.new('RGB', (xSize, ySize), (255, 255, 255))
draw = ImageDraw.Draw(im)

#升目描画
for x in range(xMax + 1):
    x_zahyo = x * cellSize
    draw.line((x_zahyo, 0, x_zahyo, ySize), fill=(0, 0, 0), width=lineWidth)

for y in range(yMax + 1):
    y_zahyo = y * cellSize
    draw.line((0, y_zahyo, xSize, y_zahyo), fill=(0, 0, 0), width=lineWidth)

im.save('imagedraw.png')
