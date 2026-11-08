# 썸네일 공통 틀: 상단 45% 글자, 하단 55% 그림
import subprocess,sys
def make(name,out,bg,bg2,ac,l1,l2,sub,svg,fs=118):
    html=f'''<html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1080px;background:radial-gradient(circle at 70% 78%,{bg2},{bg} 62%);font-family:'Noto Sans CJK KR';overflow:hidden;position:relative}}
.top{{position:absolute;left:64px;top:56px;right:64px;height:430px}}
.lab{{font-size:34px;font-weight:700;color:{ac};margin-bottom:18px}}
.t{{font-size:{fs}px;font-weight:900;line-height:1.16;letter-spacing:-3px;color:#f4f5f7;white-space:nowrap}}
.t .a{{color:{ac};text-shadow:0 0 38px {ac}66}}
.sub{{font-size:38px;font-weight:500;color:#c3c7d1;margin-top:22px}}
svg{{position:absolute;left:0;top:486px}}
</style></head><body><div class="top"><div class="lab">[AI활용]</div><div class="t">{l1}<br><span class="a">{l2}</span></div><div class="sub">{sub}</div></div>
<svg width="1080" height="594" viewBox="0 0 1080 594" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans CJK KR">{svg}</svg></body></html>'''
    open(name+'.html','w',encoding='utf-8').write(html)
    subprocess.run([sys.executable,'shot.py',name+'.html',out,'1080','1080'],check=True)
