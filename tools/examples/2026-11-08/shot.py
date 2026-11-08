# HTML 파일을 PNG로 렌더링: python3 shot.py in.html out.png 폭 [높이]
import sys,asyncio
from playwright.async_api import async_playwright
async def main(src,out,w,h):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium' if False else None)
        pg=await b.new_page(viewport={'width':w,'height':h or 800})
        await pg.goto('file://'+src); await pg.wait_for_timeout(300)
        if h: await pg.screenshot(path=out,clip={'x':0,'y':0,'width':w,'height':h})
        else:
            el=await pg.query_selector('#card'); await el.screenshot(path=out)
        await b.close()
import os
asyncio.run(main(os.path.abspath(sys.argv[1]),sys.argv[2],int(sys.argv[3]),int(sys.argv[4]) if len(sys.argv)>4 else 0))
