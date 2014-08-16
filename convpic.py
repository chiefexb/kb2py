#!/usr/bin/python
import pygame,sys
from pygame.locals import *
masks=0b00000001,0b00000010,0b00000100,0b00001000,0b00010000,0b00100000,0b01000000,0b10000000
#pal16=0xFFFF00,0x800000 	#FF0000 	#FF00FF 	#800080 	#0000FF 	#000080 	#00FFFF 	#008080 	#00FF00 	#008000 	#808000 	#FFFFFF 	#C0C0C0 	#808080 	#000000
palega=  0x000000,0x0000AA,0x00AA00,0x00AAAA,0xAA0000,0xAA00AA,0xAAAA00,0xAAAAAA,0x000055,0x0000FF,0x00AA55,0x00AAFF,0xAA0055,0xAA00FF,0xAAAA55,0xAAAAFF,0x005500,0x0055AA,0x00FF00,0x00FFAA,0xAA5500,0xAA55AA,0xAAFF00,0xAAFFAA,0x005555,0x0055FF,0x00FF55,0x00FFFF,0xAA5555,0xAA55FF,0xAAFF55,0xAAFFFF,0x550000,0x5500AA,0x55AA00,0x55AAAA,0xFF0000,0xFF00AA,0xFFAA00,0xFFAAAA,0x550055,0x5500FF,0x55AA55,0x55AAFF,0xFF0055,0xFF00FF,0xFFAA55,0xFFAAFF,0x555500,0x5555AA,0x55FFAA,0x55FFAA,0xFF5500,0xFF55AA,0xFFFF00,0xFFFFAA,0x555555,0x5555FF,0x55FF55,0x55FFFF,0xFF5555,0xFF55FF,0xFFFF55,0xFFFFFF
def getbit(num,bit):
 a=int(num & masks[bit]>bit)
 return a
def setbit(num,bit):
 a=num | masks[bit]
 return a

def main():
 #a=238
 #print bin (a)
 #for i in range (8,0):
 # print bin(getbit(a,i))
 wood=file('./ENEMY.PIC') #('./MONEY.PIC')  #('./ENEMY.PIC')
 ba=[]
 c=0b00000000
 a=wood.read()
 for j in range(0,len(a)):
  b=ord(a[j])
  for i in range(0,8):
   ba.append(getbit(b,7-i))
  #print 8-i
 print len (ba), ba
 #for
 bc=[]
 for i in range (0,len(ba),6):
  c=0b00000000
  for j in range(0,6):
   print i+j
   if ba[i+j]==1:
    c=setbit(c,j)
  bc.append(c)
 print 'bc',len(bc),'ba',len(ba)
 pygame.init()
 win=pygame.display.set_mode((640,480))
 pixArr=pygame.PixelArray(win)
 print len(a),len(palega),hex(palega[1]),len(bc),bc[45]
 for y in range(0,384):
  for x in range (0,120):
   #print bc[y*60+x]
   if int(ba[y*120+x])>0:
    pixArr[x][y]=(0xFFFFFF) #(pygame.Color(palega[bc[y*80+x] ]))
    #print x,y
  
 while True:
  for event in pygame.event.get():
   if event.type==QUIT:
    pygame.quit()
    sys.exit()
  pygame.display.update()
if __name__ == "__main__":
    main()
