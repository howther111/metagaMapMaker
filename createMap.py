from PIL import Image, ImageDraw, ImageFont
import settings
import numToAlpha
import csv


def draw_transparent_text(src_canvas, text, pos, font, fill, alpha):
    mask = Image.new("L", src_canvas.size, 1)
    text_canvas = Image.new("RGB", src_canvas.size, "#000000")
    text_canvas.putalpha(mask)

    draw = ImageDraw.Draw(text_canvas)
    draw.text(pos, text, font=font, fill=fill)
    del draw

    src_canvas.putalpha(mask)
    return Image.blend(src_canvas, text_canvas, alpha).convert("RGB")


if __name__ == '__main__':
    print("Program Start")

    csvFlg = settings.csvFlg

    # マップサイズ読込
    l = None
    xMax = settings.noCsvXMax
    yMax = settings.noCsvYMax
    if csvFlg:
        with open(settings.mapFile, encoding="utf_8") as f:
            reader = csv.reader(f)
            l = [row for row in reader]
            # print(len(l))
            # print(len(l[0]))
            xMax = len(l[0])
            yMax = len(l)

    cellSize = settings.pixelSize * settings.cellNum
    midashiSize = (settings.pixelSize // 4) * settings.cellNum
    xSize = xMax * cellSize + midashiSize
    ySize = yMax * cellSize + midashiSize
    lineWidth = (settings.pixelSize // 40) * settings.cellNum
    fontsize = (settings.pixelSize // 5) * settings.cellNum

    im = Image.new('RGB', (xSize, ySize), settings.mainColor)
    backgrouwnIm = Image.open(settings.backgroundImg)
    im.paste(backgrouwnIm, (midashiSize, midashiSize))
    draw = ImageDraw.Draw(im)
    draw.line((0, 0, 0, ySize), fill=settings.lineColor, width=lineWidth)
    draw.line((0, 0, xSize, 0), fill=settings.lineColor, width=lineWidth)
    font = ImageFont.truetype('C:/Windows/Fonts/meiryo.ttc', fontsize)

    # 升目描画
    for x in range(xMax + 1):
        xZahyo = x * cellSize + midashiSize
        draw.line((xZahyo, 0, xZahyo, ySize), fill=settings.lineColor, width=lineWidth)

    for y in range(yMax + 1):
        yZahyo = y * cellSize + midashiSize
        draw.line((0, yZahyo, xSize, yZahyo), fill=settings.lineColor, width=lineWidth)

    # 文字描画
    num = 1
    for x in range(xMax):
        xPoint = midashiSize + (cellSize / 2) + (x * cellSize)
        yPoint = midashiSize / 2
        w, h = draw.textsize(str(num), font)
        # print(w)
        # print(h)
        draw.text((xPoint - (w / 2), yPoint - (h / 2) - (4 * settings.cellNum)), str(num), fill=settings.lineColor, font=font)
        num = num + 1

    num = 1
    for y in range(yMax):
        xPoint = (midashiSize / 2)
        yPoint = midashiSize + (cellSize / 2) + (y * cellSize)
        alphaNum = numToAlpha.numToAlphaOne(num)
        w, h = draw.textsize(alphaNum, font)
        draw.text((xPoint - (w / 2), yPoint - (h / 2) - (4 * settings.cellNum)), alphaNum, fill=settings.lineColor, font=font)
        num = num + 1

    # 地形読込
    if csvFlg:
        for y in range(yMax):
            for x in range(xMax):
                cellFontsize = cellSize
                font = ImageFont.truetype('C:/Windows/Fonts/meiryo.ttc', cellFontsize)
                mapText = l[y][x]
                w, h = draw.textsize(mapText, font)
                xPoint = midashiSize + (cellSize / 2) + (x * cellSize)
                yPoint = midashiSize + (cellSize / 2) + (y * cellSize)
                xPoint2 = xPoint - (w / 2)
                yPoint2 = yPoint - (h / 2) - (30 * settings.cellNum)
                draw.text((xPoint - (w / 2), yPoint - (h / 2) - (30 * settings.cellNum)), mapText,
                          fill=settings.lineColor, font=font)

    im.save(settings.outputImg)
    print("Program End")