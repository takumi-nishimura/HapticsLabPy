from math import sqrt

from PIL import Image, ImageDraw


def length(a):
    x, y = 0, 0
    for (dx, dy) in a:
        x += dx
        y += dy
    return sqrt(x**2 + y**2)


def convert(a, b):
    ax, ay = a
    alen = sqrt(ax**2+ay**2)
    c = ax/alen
    s = ay/alen
    scale = alen/length(b)
    r = []
    for (bx, by) in b:
        bx *= scale
        by *= scale
        nx = c * bx - s * by
        ny = s * bx + c*by
        r.append((nx, ny))
    return r


def apply(a, b):
    r = []
    for i in a:
        r += convert(i, b)
    return r


def draw_line(draw, a, s=(0, 0)):
    x1, y1 = s
    for (dx, dy) in a:
        x2 = x1 + dx
        y2 = y1 + dy
        draw.line((x1, y1, x2, y2), fill=(255, 255, 255))
        x1, y1 = x2, y2


def main():
    size = 512
    im = Image.new("RGB", (size, size))
    draw = ImageDraw.Draw(im)
    # a = [(size, 0)]
    sx = size/3
    sy = sx * sqrt(3)
    a = [(sx, sy), (sx, -sy), (-2*sx, 0)]
    # b = [(1, 0), (0.5, sqrt(3.0)/2), (0.5, -sqrt(3.0)/2), (1, 0)]
    # b = [(1, 0), (0, 1), (1, 0), (0, -1), (1, 0)]
    b = [(1, 1), (1, -1)]
    for _ in range(5):
        a = apply(a, b)
    draw_line(draw, a)
    im.save("test.png")


main()