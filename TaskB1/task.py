TRACE=[(1,0,48),(2,20,71),(3,40,86),(4,60,None),(5,80,131),(6,100,142),(7,120,175),(8,140,190),(9,160,None),(10,180,236),(11,200,248),(12,220,271)]
def metrics(trace):
    got=[(s,tx,rx) for s,tx,rx in trace if rx is not None]
    loss=100*(len(trace)-len(got))/len(trace)
    avg_delay=sum(rx-tx for _,tx,rx in got)/len(got)
    jitter=0.0
    for (_,tx1,rx1),(_,tx2,rx2) in zip(got,got[1:]):
        d=abs((rx2-rx1)-(tx2-tx1))
        jitter+=(d-jitter)/16
    return loss,avg_delay,jitter
def mos(loss,avg_delay,jitter):
    d=avg_delay+2*jitter+25
    id_=0.024*d+(0.11*(d-177.3) if d>177.3 else 0)
    ie=95*loss/(loss+25.1)
    r=93.2-id_-ie
    return r,1+0.035*r+7e-6*r*(r-60)*(100-r)
for label,trace in [('Original trace',TRACE),('No lost packets',[(s,tx,rx if rx is not None else tx+50) for s,tx,rx in TRACE])]:
    loss,delay,jitter=metrics(trace)
    r,score=mos(loss,delay,jitter)
    print(label)
    print(f'packet loss {loss:.1f} %')
    print(f'average delay {delay:.1f} ms, jitter {jitter:.2f} ms')
    print(f'R-factor {r:.1f}, MOS {score:.2f}')
    print('VoIP quality:', 'good' if score>=4.0 else 'acceptable' if score>=3.6 else 'poor')
