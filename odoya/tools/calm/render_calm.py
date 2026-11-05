#!/usr/bin/env python3
"""Odoya calm video: 15 s seamless loop, particle text, left layout.
Usage: python3 render_calm.py CLIP.mp4 OUT.mp4 '["line1","line2","line3","line4"]' 'highlight word.' [CLIP_START_SECONDS]
Needs: ffmpeg, playwright (chromium), numpy, opencv-python, scipy. Clip needs >= 16.5 s after START (extend short clips first).
Run bowls15.py once to make bowls15.m4a (python3 bowls15.py && ffmpeg -i bowls15.wav -c:a aac -b:a 256k bowls15.m4a)."""
import os,sys,json,shutil,subprocess,numpy as np,cv2
from playwright.sync_api import sync_playwright
H=os.path.dirname(os.path.abspath(__file__));W=os.path.join(H,'work');os.makedirs(W,exist_ok=True)
clip,out,LINES,HI=sys.argv[1],sys.argv[2],json.loads(sys.argv[3]),sys.argv[4];start=float(sys.argv[5]) if len(sys.argv)>5 else 0
audio=os.path.join(H,'bowls15.m4a')
F=lambda f:'file://'+os.path.join(H,'fonts',f)
fonts=''.join("@font-face{font-family:'%s';font-weight:%d;src:url('%s')}"%(n,w,F(f)) for n,w,f in [('Anton',400,'anton-latin-400-normal.woff2'),('Barlow',400,'barlow-latin-400-normal.woff2'),('Barlow',500,'barlow-latin-500-normal.woff2'),('Barlow',600,'barlow-latin-600-normal.woff2')])
G='background:linear-gradient(90deg,#88aaff,#a38dff 50%,#d283e2);-webkit-background-clip:text;background-clip:text;color:transparent;text-shadow:none'
hl=lambda w:'<span style="position:relative;display:inline-block"><span style="position:absolute;left:0;top:0;color:#fff;-webkit-text-stroke:7px #fff;text-shadow:none">%s</span><span style="position:relative;%s">%s</span></span>'%(w,G,w)
lines=[l.replace(HI,hl(HI)) if HI in l else l for l in LINES]
LOGO='file://'+os.path.join(H,'logo_lines_white.png')
head='<div style="position:absolute;left:140px;top:300px;display:flex;align-items:center;gap:28px"><img src="%s" style="height:150px;filter:drop-shadow(0 2px 10px #0008);opacity:.95"><div style="font:600 24px/30px Barlow,sans-serif;letter-spacing:.38em;color:#fffaf2;text-shadow:0 2px 14px #0007">@ODOYA.STORE.US<br><span style="display:inline-block;margin-top:12px">ODOYAMARKETPLACE.ETSY.COM</span></div></div>'%LOGO
phrase='<div style="position:absolute;left:140px;top:630px;color:#fffaf2;text-shadow:0 2px 24px #0006;font:400 69px/78px Anton,sans-serif;text-transform:uppercase;letter-spacing:.01em">%s</div>'%'<br>'.join(lines)
scrim='<div style="position:absolute;inset:0;background:radial-gradient(ellipse 60% 22% at 32% 27%,#0000003d,#0000 100%),linear-gradient(#0000 58%,#0004 100%)"></div><div style="position:absolute;inset:0;background:linear-gradient(#0005,#0000 40%)"></div>'
page='<html><head><meta charset="utf-8"><style>'+fonts+'html,body{background:transparent;margin:0;width:1080px;height:1920px;overflow:hidden}</style></head><body>%s</body></html>'
with sync_playwright() as p:
    b=p.chromium.launch()
    for k,v in [('scrim',scrim),('head',head),('phrase',phrase)]:
        fn=os.path.join(W,k+'.html');open(fn,'w').write(page%v)
        pg=b.new_page(viewport={'width':1080,'height':1920});pg.goto('file://'+fn);pg.wait_for_timeout(700);pg.screenshot(path=os.path.join(W,k+'.png'),omit_background=True);pg.close()
# particles: ~11000 dots gather into the text, left to right order top to bottom, 5 s
im=cv2.imread(os.path.join(W,'phrase.png'),cv2.IMREAD_UNCHANGED);a=im[...,3]
ys,xs=np.where(a>200);rng=np.random.default_rng(7);idx=rng.choice(len(xs),size=min(11000,len(xs)),replace=False)
tx=xs[idx].astype(np.float32);ty=ys[idx].astype(np.float32);col=im[ys[idx],xs[idx],:3].astype(np.float32);N=len(tx)
ang=rng.uniform(0,2*np.pi,N);rad=rng.uniform(80,520,N)
sx=tx+np.cos(ang)*rad+rng.normal(-60,40,N);sy=ty+np.sin(ang)*rad+rng.normal(90,40,N)
delay=((ty-ty.min())/(ty.max()-ty.min()))*1.3+rng.uniform(0,0.5,N);dur=rng.uniform(1.8,2.5,N);swirl=rng.uniform(-1,1,N)*40
PF=os.path.join(W,'pf');PR=os.path.join(W,'pr')
for d in(PF,PR):shutil.rmtree(d,ignore_errors=True);os.makedirs(d)
nf=150
for f in range(nf):
    t=f/30;u=np.clip((t-delay)/dur,0,1);e=0.5*(1-(1-u)**3)+0.5*(u*u*(3-2*u))
    x=sx+(tx-sx)*e+np.sin(u*np.pi)*swirl;y=sy+(ty-sy)*e;vis=np.clip(u*3,0,1)*(t>=delay)
    A=np.zeros((1920,1080),np.float32);C=np.zeros((1920,1080,3),np.float32)
    xi=np.round(x).astype(int);yi=np.round(y).astype(int);ok=(xi>1)&(xi<1078)&(yi>1)&(yi<1918)&(vis>0)
    for dx in(-1,0,1):
        for dy in(-1,0,1):
            w=1.0 if dx==0 and dy==0 else .55;xx=xi[ok]+dx;yy=yi[ok]+dy
            np.maximum.at(A,(yy,xx),(vis[ok]*w).astype(np.float32));C[yy,xx]=col[ok]
    glow=cv2.GaussianBlur(A,(0,0),8);pa0=np.clip(A+glow*.9,0,1)
    cf=np.clip((t-3.6)/1.2,0,1);fa=im[...,3].astype(np.float32)/255*cf;pa=pa0*(1-cf**2)
    Ao=fa+pa*(1-fa);pc=np.where(C.sum(-1,keepdims=True)>60,C,np.array([250,250,255],np.float32))
    rgb=(im[...,:3].astype(np.float32)*fa[...,None]+pc*(pa*(1-fa))[...,None])/np.maximum(Ao[...,None],1e-6)
    cv2.imwrite(os.path.join(PF,'f%04d.png'%f),np.dstack([np.clip(rgb,0,255),np.clip(Ao*255,0,255)]).astype(np.uint8))
for i in range(nf):os.symlink(os.path.join(PF,'f%04d.png'%(nf-1-i)),os.path.join(PR,'f%04d.png'%i))
fc=("[0:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,eq=saturation=0.9:contrast=0.95:brightness=0.03,format=yuv420p,split[s1][s2];"
"[s1]trim=start=1.5:duration=15,setpts=PTS-STARTPTS[a];[s2]trim=start=0:duration=1.5,setpts=PTS-STARTPTS[b];[a][b]xfade=transition=fade:duration=1.5:offset=13.5,format=yuv420p[v];"
"[1:v]format=rgba[sc];[2:v]format=rgba,trim=end_frame=147,setpts=PTS-STARTPTS[seq];[3:v]format=rgba,trim=start_frame=3,setpts=PTS-STARTPTS+10.1/TB[rev];[4:v]format=rgba[st];[5:v]format=rgba[ft];"
"[v][sc]overlay[a1];[a1][ft]overlay[a2];[a2][seq]overlay=eof_action=pass[b1];[b1][st]overlay=enable='between(t,4.9,10.1)'[c1];[c1][rev]overlay=enable='gte(t,10.1)':eof_action=pass,format=yuv420p[o]")
P=lambda n:os.path.join(W,n)
subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(start),'-t','16.5','-i',clip,'-loop','1','-t','15','-i',P('scrim.png'),'-framerate','30','-i',PF+'/f%04d.png','-framerate','30','-i',PR+'/f%04d.png','-loop','1','-t','15','-i',P('phrase.png'),'-loop','1','-t','15','-i',P('head.png'),'-i',audio,'-filter_complex',fc,'-map','[o]','-map','6:a','-t','15','-c:v','libx264','-preset','veryfast','-crf','20','-c:a','aac','-b:a','256k','-movflags','+faststart',out],check=True)
print('ok',out)
