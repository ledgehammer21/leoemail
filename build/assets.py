import sys, os
from PIL import Image, ImageDraw
Image.MAX_IMAGE_PIXELS = None
MOCK = '/mnt/user-data/uploads/LEO026_See_You_Tomorrow_Email_2.png'
SRC = '/root/.claude/uploads/bcd9105b-c598-5d83-99ff-3d739647c6a6/'
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
m = Image.open(MOCK).convert('RGB')

def save(im, name, q=86):
    im.save(os.path.join(OUT, name), 'JPEG', quality=q, optimize=True, progressive=True)

# straight crops from the approved mockup (2x)
crops = {
    'header.jpg': (0, 0, 1200, 552),
    'exterior-entry.jpg': (200, 1077, 1000, 1509),
    'kitchen.jpg': (200, 1554, 578, 1986),
    'pool-aerial.jpg': (621, 1554, 999, 1986),
    'friends-campus.jpg': (200, 2718, 1000, 3150),
    'friends-pickleball.jpg': (200, 3194, 578, 3626),
    'friends-selfie.jpg': (621, 3194, 999, 3626),
}
for n, b in crops.items():
    save(m.crop(b), n, 88)
m.crop((0, 2076, 200, 2276)).save(os.path.join(OUT, 'pattern-teal.png'), optimize=True)
m.crop((0, 3717, 200, 3917)).save(os.path.join(OUT, 'pattern-pink.png'), optimize=True)

# new crops from the renderings, with the same leaf-corner treatment baked in
def leaf(src, name, w, h, cx=0.5, cy=0.5, r=70):
    f = [p for p in os.listdir(SRC) if p.endswith(src)][0]
    im = Image.open(SRC + f).convert('RGB')
    s = max(w / im.width, h / im.height)
    cw, ch = w / s, h / s
    x0 = min(max(im.width * cx - cw / 2, 0), im.width - cw)
    y0 = min(max(im.height * cy - ch / 2, 0), im.height - ch)
    im = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((w, h), Image.LANCZOS)
    k = 4
    mask = Image.new('L', (w * k, h * k), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w * k - 1, h * k - 1), r * k, fill=255,
                                           corners=(True, False, True, False))
    mask = mask.resize((w, h), Image.LANCZOS)
    bg = Image.new('RGB', (w, h), 'white')
    bg.paste(im, (0, 0), mask)
    save(bg, name, 88)

leaf('H__POOL1.jpg', 'rooftop-pool.jpg', 800, 432, 0.5, 0.62)
leaf('Sanibel_PH__Living_Room.jpg', 'living-room.jpg', 378, 432, 0.45, 0.6)
leaf('C__PICKLE_BALL_COURT.jpg', 'pickleball-court.jpg', 378, 432, 0.62, 0.6)

# Still Interested lifestyle set (client-supplied photos)
leaf('59e5ef8c-image.jpg', 'friends-gameday-selfie.jpg', 800, 432, 0.5, 0.47)
leaf('d82d6a3f-image.jpg', 'friends-coffee.jpg', 378, 432, 0.5, 0.5515)
leaf('dc506566-image.jpg', 'poolside.jpg', 378, 432, 0.5, 0.45)
