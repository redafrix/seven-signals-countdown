#!/usr/bin/env python3
"""Seven Signals: generate coordinated, accurate daily lock screen wallpapers."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
from math import sin, cos, radians, pi
import random

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "wallpapers"
OUT.mkdir(exist_ok=True)
W, H = 1290, 2796
DAYS = [
    ("NOV 16", "CHOOSE THE DEADLINE", "Give the mission a real finish line."),
    ("NOV 17", "MAP THE SEVEN STEPS", "One useful action for each day."),
    ("NOV 18", "SKETCH THE SCREEN", "Leave breathing room for the clock."),
    ("NOV 19", "BUILD THE FIRST DRAFT", "Make the countdown clear in one glance."),
    ("NOV 20", "TEST ON YOUR PHONE", "Check contrast, scale and placement."),
    ("NOV 21", "POLISH + EXPORT", "Refine the details; prepare the files."),
    ("NOV 22", "PUBLISH THE PROJECT", "Prepare the link and submission story."),
    ("NOV 23", "VERIFY SUBMISSION", "Confirm the link before 11:59 PM PT."),
]
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
MONO="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
def font(size, weight=False, mono=False):
    return ImageFont.truetype(MONO if mono else BOLD if weight else REG, size)
def centerd(draw, text, y, f, fill, spacing=0):
    bb=draw.textbbox((0,0),text,font=f,stroke_width=0)
    draw.text(((W-(bb[2]-bb[0]))//2,y),text,font=f,fill=fill,spacing=spacing)
def glow(img, xy, radius, color, strength=100):
    temp=Image.new("RGBA",(W,H),(0,0,0,0))
    t=ImageDraw.Draw(temp)
    x,y=xy
    t.ellipse((x-radius,y-radius,x+radius,y+radius),fill=(*color,strength))
    img.alpha_composite(temp.filter(ImageFilter.GaussianBlur(radius//2)))
def build(idx):
    random.seed(2026)
    # Designed as an actual phone wallpaper: the top 730px is quiet and holds the native clock.
    base=Image.new("RGB",(W,H),(6,13,31))
    p=base.load()
    for y in range(H):
        blend=y/H
        for x in range(W):
            lateral=sin(x/220 + y/600)*0.5+0.5
            p[x,y]=(int(6+9*blend+3*lateral),int(13+11*blend+3*lateral),int(31+23*blend+7*lateral))
    img=base.convert("RGBA")
    glow(img,(1060,1040),280,(3,191,222),66)
    glow(img,(160,1610),380,(188,70,222),55)
    glow(img,(790,2200),420,(25,78,174),45)
    d=ImageDraw.Draw(img,"RGBA")
    # Constellation of micro-signals; no bright star competes with the real clock.
    for k in range(280):
        x=random.randrange(W); y=random.randrange(680, H-170)
        r=random.choice([1,1,1,2,2,3])
        alpha=random.randint(45,165)
        d.ellipse((x-r,y-r,x+r,y+r),fill=(160,217,248,alpha))
    # Transparent contour maps form the metaphor: a course toward the deadline.
    for j in range(26):
        points=[]
        for x in range(-40,W+45,12):
            y=2290 + j*18 + 54*sin(x/158+j*.23)+34*sin(x/83+j*.44)
            points.append((x,int(y)))
        d.line(points,fill=(28+min(j*3,80),171,211,max(14,90-j*3)),width=2)
    for j in range(15):
        points=[]
        for x in range(-40,W+45,12):
            y=2340+j*23+38*sin(x/117-j*.28)+25*cos(x/190+j*.42)
            points.append((x,int(y)))
        d.line(points,fill=(191,83,228,max(12,64-j*3)),width=2)
    # A minimal header below the phone clock safety area.
    d.line((108,760,360,760),fill=(101,234,248,170),width=3)
    d.text((385,730),"HANDSHAKE  /  NOV 2026",font=font(30,mono=True),fill=(191,216,234,235))
    d.line((925,760,1182,760),fill=(174,110,245,145),width=3)
    centerd(d,"S E V E N    S I G N A L S",830,font(45,True),(247,251,255,255))
    centerd(d,"A DEADLINE YOU CAN SEE",899,font(24,mono=True),(140,185,205,220))
    # Single orbit, seven signal points. Completed beacons illuminate as the date moves forward.
    cx,cy,r=645,1430,438
    d.arc((cx-r,cy-r,cx+r,cy+r),150,390,fill=(82,133,176,117),width=6)
    # Deeper ring and subtle navigation tick marks.
    d.arc((cx-r+26,cy-r+26,cx+r-26,cy+r-26),153,387,fill=(50,87,137,110),width=2)
    for j in range(7):
        theta=radians(150+j*40)
        x=int(cx+r*cos(theta)); y=int(cy+r*sin(theta))
        complete=(j<idx)
        current=(j==min(idx,6))
        if complete or current:
            col=(108,241,246) if complete else (246,126,220)
            d.ellipse((x-22,y-22,x+22,y+22),fill=(*col,43))
            d.ellipse((x-11,y-11,x+11,y+11),fill=(*col,255))
            d.ellipse((x-4,y-4,x+4,y+4),fill=(255,255,255,255))
        else:
            d.ellipse((x-9,y-9,x+9,y+9),outline=(118,161,193,190),width=3)
        label=str(j+1).zfill(2)
        lx=int(cx+(r+61)*cos(theta)); ly=int(cy+(r+61)*sin(theta))
        bb=d.textbbox((0,0),label,font=font(23,mono=True))
        d.text((lx-(bb[2]-bb[0])/2,ly-12),label,font=font(23,mono=True),fill=(127,157,187,205))
    # Central value shows calendar-day offset; no fake system clock/date.
    left=7-idx
    centerd(d,f"{left:02}",1190,font(300,True),(247,251,255,255))
    centerd(d,"DAYS TO LAUNCH" if left else "DEADLINE DAY",1555,font(39,True),(202,232,244,250))
    centerd(d,"NOV 23   /   11:59 PM PT",1642,font(27,mono=True),(128,196,219,243))
    # Progress readout
    d.rounded_rectangle((210,1845,1080,1855),radius=5,fill=(61,97,125,135))
    if idx:
        d.rounded_rectangle((210,1845,210+int(870*idx/7),1855),radius=5,fill=(94,229,242,235))
    d.text((210,1883),f"SIGNAL {idx+1:02}/08",font=font(31,mono=True),fill=(105,218,234,230))
    d.text((900,1883),f"{idx}/7 CLEARED",font=font(28,mono=True),fill=(173,185,208,210))
    # Action card: bigger typography; only one milestone for maximum clarity.
    d.rounded_rectangle((98,1980,1192,2278),radius=48,fill=(11,27,51,215),outline=(81,149,180,200),width=3)
    d.rounded_rectangle((137,2020,224,2108),radius=25,fill=(51,179,202,38),outline=(99,224,238,200),width=2)
    d.text((158,2037),str(idx+1).zfill(2),font=font(35,True),fill=(198,253,255,255))
    d.text((252,2030),"TODAY'S MISSION",font=font(27,mono=True),fill=(141,205,223,250))
    d.text((139,2140),DAYS[idx][1],font=font(48,True),fill=(246,248,255,255))
    d.text((143,2214),DAYS[idx][2],font=font(27),fill=(165,194,219,255))
    d.text((126,2480),"THE PATH IS BUILT ONE DAY AT A TIME.",font=font(28,mono=True),fill=(173,194,219,205))
    d.text((126,2550),f"DAY {idx+1:02}  /  {DAYS[idx][0]}, 2026",font=font(25,mono=True),fill=(117,164,197,220))
    # iPhone bottom tool/gesture area stays intentionally uncluttered.
    result=img.convert("RGB")
    out=OUT / f"Seven_Signals_{idx+1:02}_Nov_{16+idx}_D{left}.png"
    result.save(out,optimize=True)
    return out

if __name__=="__main__":
    files=[build(i) for i in range(8)]
    # Cover landscape for Handshake's required cover-image field.
    im=Image.open(files[0]).convert("RGB")
    cover=Image.new("RGB",(1600,900),(7,16,35))
    cd=ImageDraw.Draw(cover,"RGBA")
    for x in range(1600):
        col=(int(7+x/800),int(16+x/400),int(35+x/140))
        cd.line((x,0,x,900),fill=col)
    mock=im.resize((368,799),Image.Resampling.LANCZOS)
    cover.paste(mock,(1095,52))
    cd.rounded_rectangle((1080,38,1479,864),radius=50,outline=(132,210,231,230),width=5)
    cd.text((105,120),"HANDSHAKE  /  2026",font=font(32,mono=True),fill=(132,219,230,255))
    cd.text((104,270),"SEVEN",font=font(142,True),fill=(245,249,252,255))
    cd.text((104,422),"SIGNALS",font=font(142,True),fill=(245,249,252,255))
    cd.line((108,611,849,611),fill=(98,206,222,190),width=4)
    cd.text((109,655),"A countdown that becomes a daily plan.",font=font(35),fill=(180,207,229,255))
    cd.text((109,732),"7 milestones. 8 wallpapers. One deadline.",font=font(27,mono=True),fill=(99,216,231,255))
    cover.save(ROOT/"Cover_Seven_Signals_1600x900.png",optimize=True)
    print("\n".join(str(f) for f in files))
    print("Cover:",ROOT/"Cover_Seven_Signals_1600x900.png")
