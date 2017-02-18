#home/ljwxman116/miniconda2/bin/python

import argparse
import math
parser = argparse.ArgumentParser()
parser.add_argument("wind")
parser.add_argument("deg")
args = parser.parse_args()
wind=args.wind
deg=args.deg
sin=math.sin
cos=math.cos
'''
def u(speed,deg):
    uc=-speed*sin((pi/180)*deg)
    return uc
def v(speed,deg):
    vc=-speed*cos((pi/180)*deg)
    return vc
'''
def uv(speed,deg):
    uc=-speed*sin((pi/180)*deg)
    vc=-speed*cos((pi/180)*deg)
    return uc,vc
#print u(13,215)
#print v(13,215)
print uv(wind,deg)