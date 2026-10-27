"""Draw the banner for the BNI Tech organization page.

Writes profile/assets/banner-{light,dark}.html and renders each to a PNG at 2x
with headless Chrome, which loads the site's fonts (Silkscreen, Space Grotesk,
Space Mono) from Google Fonts. The banner holds no counts or dates, so it only
needs redrawing when the site's wording or look changes:  python3 tools/make_images.py
"""
import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "profile", "assets")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Silkscreen&family=Space+Grotesk:wght@400;500'
         '&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">')
THEMES = {  # the site's own palette (page.html); gh is GitHub's page colour behind the image
    "light": dict(gh="#ffffff", paper="#e8e8e4", ink="#111111", muted="#55554f"),
    "dark": dict(gh="#0d1117", paper="#131313", ink="#ecebe6", muted="#a3a39b"),
}
YELLOW = "#ffd400"
LINE = "BNI is me. Tech is what I build with. Lab is where I work on it. Not a company."
INTRO = "My lab, by Dawn. From my first game in 2011 to what I am working on today. You are welcome to look around."


def banner(c):
    css = f"""body{{margin:0;background:{c['gh']}}}
.p{{box-sizing:border-box;width:960px;min-height:100vh;display:flex;flex-direction:column;justify-content:space-between;background:{c['paper']};border-radius:12px;overflow:hidden;color:{c['ink']}}}
.in{{padding:42px 46px 0;display:flex;flex-direction:column;gap:14px}}
h1{{font-family:Silkscreen,monospace;font-weight:400;font-size:70px;line-height:1;margin:0;letter-spacing:.02em}}
.l{{font-family:'Space Mono',monospace;font-size:15px;line-height:1.6;color:{c['muted']};margin:0}}
.i{{font-family:'Space Grotesk',sans-serif;font-size:20px;line-height:1.5;margin:0;max-width:62ch}}
.s{{height:14px;margin-top:30px;background:repeating-linear-gradient(-45deg,#111111 0 10px,{YELLOW} 10px 20px)}}"""
    body = f'<div class="in"><h1>BNI TECH</h1><p class="l">{LINE}</p><p class="i">{INTRO}</p></div><div class="s"></div>'
    return css, body


for theme, c in THEMES.items():
    css, body = banner(c)
    html = os.path.join(OUT, f"banner-{theme}.html")
    with open(html, "w", encoding="utf-8") as f:
        f.write(f"<html><head>{FONTS}<style>{css}</style></head><body><div class='p'>{body}</div></body></html>")
    png = os.path.join(OUT, f"banner-{theme}.png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=6000",
                    "--force-device-scale-factor=2", "--window-size=960,276", f"--screenshot={png}",
                    "file://" + os.path.abspath(html)], check=True, capture_output=True)
    os.remove(html)
    print(png)
