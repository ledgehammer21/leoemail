"""V3 mosaic images: one tall photo + a stacked pair, leaf corners baked in (2x for a 600px layout)."""
import sys, os
from PIL import Image, ImageDraw
Image.MAX_IMAGE_PIXELS = None
SRC = '/root/.claude/uploads/bcd9105b-c598-5d83-99ff-3d739647c6a6/'
OUT = sys.argv[1]

def load(name):
    if os.path.exists(os.path.join(OUT, name)):
        return Image.open(os.path.join(OUT, name)).convert('RGB')
    f = [p for p in os.listdir(SRC) if p.endswith(name)][0]
    return Image.open(SRC + f).convert('RGB')

def cover(im, w, h, cx=0.5, cy=0.5, zoom=1.0):
    s = max(w / im.width, h / im.height) * zoom
    cw, ch = w / s, h / s
    x0 = min(max(im.width * cx - cw / 2, 0), im.width - cw)
    y0 = min(max(im.height * cy - ch / 2, 0), im.height - ch)
    return im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((w, h), Image.LANCZOS)

def leaf(im, r):
    w, h = im.size; k = 4
    m = Image.new('L', (w * k, h * k), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, w * k - 1, h * k - 1), r * k, fill=255, corners=(True, False, True, False))
    bg = Image.new('RGB', (w, h), 'white'); bg.paste(im, (0, 0), m.resize((w, h), Image.LANCZOS)); return bg

def save(im, name):
    im.save(os.path.join(OUT, name), 'JPEG', quality=88, optimize=True, progressive=True)

def tall(src, name, **kw):
    save(leaf(cover(load(src), 498, 660, **kw), 84), name)

def stack(top, bottom, name):
    out = Image.new('RGB', (498, 660), 'white')
    out.paste(leaf(cover(load(top[0]), 498, 308, **top[1]), 64), (0, 0))
    out.paste(leaf(cover(load(bottom[0]), 498, 308, **bottom[1]), 64), (0, 352))
    save(out, name)

tall('H__POOL2.jpg', 'v3-tour-tall.jpg', cx=0.36, cy=0.5)
stack(('A__EXTERIOR_LOBBY_SIGNAGE.jpg', dict(cx=0.5, cy=0.56, zoom=1.25)),
      ('59e5ef8c-image.jpg', dict(cx=0.5, cy=0.42)), 'v3-tour-stack.jpg')
tall('d82d6a3f-image.jpg', 'v3-still-tall.jpg', cx=0.5, cy=0.56)
stack(('H__POOL1.jpg', dict(cx=0.5, cy=0.62)),
      ('dc506566-image.jpg', dict(cx=0.5, cy=0.3)), 'v3-still-stack.jpg')
