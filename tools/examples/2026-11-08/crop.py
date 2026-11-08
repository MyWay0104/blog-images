# 캡처 자르기: python3 crop.py <원본> <출력> <top> <bottom> [left right]
import sys
from PIL import Image
src,out,top,bot=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
im=Image.open(src); w,h=im.size
left=int(sys.argv[5]) if len(sys.argv)>5 else 0
right=int(sys.argv[6]) if len(sys.argv)>6 else w-15
im.crop((left,top,right,bot)).save(out); print(out, right-left, bot-top)
