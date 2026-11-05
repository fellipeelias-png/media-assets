import numpy as np, scipy.signal as sg, scipy.io.wavfile as wf
sr=48000;T=15.0;n=int(sr*T);N2=2*n;t2=np.arange(N2)/sr
rng=np.random.default_rng(3)
def bowl(f0,start,amp,decay=7.0):
    out=np.zeros(N2);s=int(start*sr);tt=np.arange(N2-s)/sr
    att=0.5-0.5*np.cos(np.pi*np.clip(tt/0.08,0,1))
    for r,a,dk,beat in [(1.0,1.0,1.0,0.6),(2.76,0.16,0.55,1.1),(5.40,0.04,0.3,1.7)]:
        f=f0*r;env=np.exp(-tt/(decay*dk))*att
        out[s:]+=a*np.sin(2*np.pi*f*tt+rng.uniform(0,6.28))*env
        out[s:]+=0.7*a*np.sin(2*np.pi*(f+beat)*tt+rng.uniform(0,6.28))*env
    return out*amp
x=np.zeros(N2)
for f0,st,a in [(196.0,0.5,1.0),(261.63,5.6,0.7),(220.0,10.4,0.85)]:
    x+=bowl(f0,st,a)
x=x[:n]+x[n:]                      # fold the tail onto the start: seamless loop
t=np.arange(n)/sr
x+=(np.sin(2*np.pi*98*t)*0.5+np.sin(2*np.pi*147*t+1)*0.3)*0.05*(0.7+0.3*np.sin(2*np.pi*(2/15)*t))
def echo(sig,d,g,lpf=700):
    b,a=sg.butter(1,lpf/(sr/2));y=sig.copy()
    for k in range(1,7):
        y+=(g**k)*sg.lfilter(b,a,np.roll(sig,k*d))
    return y
L=echo(x,int(0.52*sr),0.5);R=echo(np.roll(x,int(0.011*sr)),int(0.67*sr),0.5)
st=np.stack([L,R],1)
# circular low-pass (3x tile) so the loop point has no filter discontinuity
b,a=sg.butter(2,2200/(sr/2));st=sg.lfilter(b,a,np.tile(st,(3,1)),axis=0)[n:2*n]
st=st/np.abs(st).max()*0.6
wf.write('bowls15.wav',sr,(st*32767).astype(np.int16))
print('loop jump',np.abs(st[0]-st[-1]).max().round(5),'max step',np.abs(np.diff(st,axis=0)).max().round(5))
