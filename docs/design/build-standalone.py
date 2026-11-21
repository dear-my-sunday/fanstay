#!/usr/bin/env python3
"""problem-slides.html 의 영상(assets/*.mp4)을 base64로 안에 넣어 파일 하나로 열리는 버전을 만들어요.
미리보기 앱·메신저 전달처럼 assets 폴더를 같이 못 가져가는 경우에 써요.
사용: python3 docs/design/build-standalone.py → docs/design/problem-slides.standalone.html"""
import base64, re, pathlib
d = pathlib.Path(__file__).parent
html = (d / 'problem-slides.html').read_text()
def inline(m):
    f = d / m.group(1)
    if not f.exists():  # 주석 처리된 예비 클립 등
        return m.group(0)
    return "src:'data:video/mp4;base64," + base64.b64encode(f.read_bytes()).decode() + "'"
html = re.sub(r"src:'(assets/[^']+\.mp4)'", inline, html)
(d / 'problem-slides.standalone.html').write_text(html)
print('ok', round(len(html) / 1e6, 1), 'MB')
