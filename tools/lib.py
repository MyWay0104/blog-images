# 원고 HTML 생성 도우미: 모든 서식을 인라인 style로 넣는다 (네이버 붙여넣기용)
import html as _h
E=_h.escape
def _inline(s):
    # **굵게**, ==형광펜==, `코드` 를 인라인 서식으로 바꾼다
    import re
    s=E(s,quote=False)
    s=re.sub(r'\*\*==(.+?)==\*\*',r'<b><span style="background-color:#fff3a3">\1</span></b>',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'==(.+?)==',r'<span style="background-color:#fff3a3">\1</span>',s)
    s=re.sub(r'`(.+?)`',r'<span style="background-color:#e9ecef">\1</span>',s)
    s=re.sub(r'\[\[(.+?)\|(.+?)\]\]',r'<a href="\2">\1</a>',s)
    return s
FF="font-family:'나눔스퀘어','NanumSquare',nanumsquare,sans-serif;"  # 네이버 에디터가 글꼴 지정을 받아 주는지 확인 필요 (2026-10-18 시험)
BL='<p><br></p>\n'
def P(*lines): return '<p style="'+FF+'text-align:center;font-size:16px;line-height:1.9">'+'<br>'.join(_inline(l) for l in lines)+'</p>\n'+BL
def H1(t): return BL+'<p style="'+FF+'text-align:center"><b><span style="'+FF+'font-size:28px">'+_inline(t)+'</span></b></p>\n'+BL
def H2(t): return '<p style="'+FF+'text-align:center"><b><span style="'+FF+'font-size:19px">'+_inline(t)+'</span></b></p>\n'+BL
def Q(*lines): return '<blockquote style="'+FF+'">'+'<br>'.join(_inline(l) for l in lines)+'</blockquote>\n'+BL
def HR(): return '<hr>\n'+BL
def BOX(*lines): return '<table style="border-collapse:collapse;width:100%"><tr><td style="background-color:#f1f3f5;border-left:5px solid #868e96;padding:14px 18px;text-align:left;font-size:15px;line-height:1.8;'+FF+'">'+'<br>'.join(_inline(l) for l in lines)+'</td></tr></table>\n'+BL
def CODE(text,colors=()):
    out=[]
    for ln in text.strip('\n').split('\n'):
        n=len(ln)-len(ln.lstrip(' '))
        s=E(ln.lstrip(' '),quote=False)
        for kw,c in colors: s=s.replace(E(kw,quote=False),f'<span style="color:{c}">{E(kw,quote=False)}</span>')
        out.append('&nbsp;'*n+s)
    return '<table style="border-collapse:collapse;width:100%"><tr><td style="background-color:#212529;color:#f8f9fa;padding:16px 18px;text-align:left;font-size:14px;line-height:1.7"><span style="color:#f8f9fa">'+'<br>'.join(out)+'</span></td></tr></table>\n'+BL
def TABLE(head,rows):
    td='border:1px solid #ced4da;padding:9px 12px;text-align:left;font-size:15px;line-height:1.6;'+FF
    h='<tr>'+''.join(f'<td style="{td};background-color:#e9ecef"><b>{_inline(c)}</b></td>' for c in head)+'</tr>'
    b=''.join('<tr>'+''.join(f'<td style="{td}">{_inline(c)}</td>' for c in r)+'</tr>' for r in rows)
    return f'<table style="border-collapse:collapse;width:100%">{h}{b}</table>\n'+BL
import os,base64
EMBED_DIR=os.environ.get('EMBED_DIR')  # 설정되면 이미지 파일을 base64로 본문에 직접 넣는다
IMG_URL_BASE=os.environ.get('IMG_URL_BASE')  # 설정되면 이미지를 외부 주소(GitHub raw)로 참조한다. 예: https://raw.githubusercontent.com/MyWay0104/blog-images/main/2026-10-19_mon
_DAYS={'월':'mon','화':'tue','수':'wed','목':'thu','금':'fri'}
def IMG(n,fname,desc,src=None):
    p=os.path.join(EMBED_DIR,fname) if EMBED_DIR else None
    if IMG_URL_BASE:
        import re as _re
        m=_re.match(r'([월화수목금])_(\d\d)_',fname)
        url=f"{IMG_URL_BASE}/{_DAYS[m.group(1)]}_{m.group(2)}.png"
        s=f'<p style="text-align:center"><img src="{url}" alt="{E(desc)}" style="max-width:100%;height:auto"></p>\n'
    elif p and os.path.exists(p):
        b64=base64.b64encode(open(p,'rb').read()).decode()
        s=f'<p style="text-align:center"><img src="data:image/png;base64,{b64}" alt="{E(desc)}" style="max-width:100%;height:auto"></p>\n'
    else:
        s=f'<table style="border-collapse:collapse;width:100%"><tr><td style="background-color:#dee2e6;border:2px dashed #495057;padding:10px 14px;text-align:left;font-size:14px"><b>[이미지 {n}: {E(fname)} | {E(desc)}]</b></td></tr></table>\n'
    if src: s+=f'<p style="text-align:center;font-size:13px;color:#868e96">{_inline(src)}</p>\n'
    return s+BL
def CAP(n,what,mark): return f'<table style="border-collapse:collapse;width:100%"><tr><td style="background-color:#ffe3e3;border:2px dashed #c92a2a;padding:10px 14px;text-align:left;font-size:14px"><b>[캡처 필요 {n}: {E(what)} | {E(mark)}]</b></td></tr></table>\n'+BL
def PAGE(title,body,fname):
    doc=f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(title)}</title></head>
<body style="margin:0;background:#f8f9fa;font-family:'Malgun Gothic','Apple SD Gothic Neo',sans-serif;color:#212529">
<div id="guide" style="max-width:760px;margin:24px auto 0;padding:20px 24px;background:#fff;border:1px solid #dee2e6;border-radius:12px">
<div style="font-size:13px;color:#868e96;margin-bottom:6px">네이버 제목 칸에 붙여넣을 제목</div>
<div id="ttl" style="font-size:20px;font-weight:700;margin-bottom:14px">{E(title)}</div>
<button onclick="cp('ttl',true)" style="padding:10px 18px;font-size:15px;border:1px solid #212529;background:#fff;border-radius:8px;cursor:pointer">제목 복사</button>
<button onclick="cp('post',false)" style="padding:10px 18px;font-size:15px;border:1px solid #212529;background:#212529;color:#fff;border-radius:8px;cursor:pointer;margin-left:6px">본문 복사</button>
<span id="msg" style="margin-left:10px;font-size:14px;color:#2b8a3e"></span>
<div style="font-size:13px;color:#868e96;margin-top:12px;line-height:1.7">버튼이 동작하지 않으면 아래 본문 영역을 마우스로 선택해 복사해도 됩니다.<br>회색 점선 상자는 이미지 자리, 붉은 점선 상자는 직접 찍을 캡처 자리입니다. 이미지를 올린 뒤 상자는 지워주세요.</div>
</div>
<div id="post" style="max-width:760px;margin:16px auto 60px;padding:28px 24px;background:#fff;border:1px solid #dee2e6;border-radius:12px">
{body}</div>
<script>
function cp(id,plain){{
  var el=document.getElementById(id),m=document.getElementById('msg');
  if(plain&&navigator.clipboard){{navigator.clipboard.writeText(el.innerText).then(function(){{m.textContent='제목을 복사했습니다';}},function(){{sel(el,m);}});return;}}
  sel(el,m);
}}
function sel(el,m){{
  var r=document.createRange();r.selectNodeContents(el);var s=window.getSelection();s.removeAllRanges();s.addRange(r);
  var ok=false;try{{ok=document.execCommand('copy');}}catch(e){{}}
  s.removeAllRanges();m.textContent=ok?'복사했습니다. 네이버 글쓰기 화면에 붙여넣으세요':'복사에 실패했습니다. 직접 선택해 복사해주세요';
}}
</script></body></html>'''
    open(fname,'w',encoding='utf-8').write(doc)
