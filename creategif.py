from PIL import Image
import os, sys

if len(sys.argv) > 1:
    pattern = sys.argv[1]
else:
    pattern = ".png"

start = 0
end = 230
step = 1
duration = 75
loop = 0
dst = "result.gif"


i = 0
frames = []
for fn in os.listdir("./"):
    if pattern in fn:
        if start <= i <= end:
            if i%step == 0:
                print(i, fn)
                frames.append(Image.open(fn))
            i += 1

frames[0].save(dst, format='GIF', append_images=frames[1:],
                save_all=True, duration=duration, loop=loop)
