import os
import sys
import os.path as osp
import cv2
from glob import glob

imgs = glob(osp.join(sys.argv[1], '*'))

kvs = {}

for name, im in enumerate(imgs):
    img = cv2.imread(im)
    h, w = img.shape[:2]
    kvs[im] = float(h/w)

print(kvs)
kvs = sorted(kvs, key=lambda x:kvs[x])
print(kvs)
for name, k in enumerate(kvs):
    cv2.imwrite(f'img/{name + 1}.webp', cv2.imread(k))
