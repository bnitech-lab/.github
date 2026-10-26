"""Draw the banner and the by-year picture for the BNI Tech organization page.

Writes profile/assets/{banner,timeline}-{light,dark}.html and renders each to a
PNG at 2x with headless Chrome, which loads the site's fonts (Silkscreen and
IBM Plex) from Google Fonts. Edit ERAS when an idea is marked public on the
site, then run:  python3 tools/make_images.py
"""
import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "profile", "assets")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Silkscreen&family=IBM+Plex+Sans:wght@400;500;600'
         '&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')
THEMES = {  # the site's own palette
    "light": dict(gh="#ffffff", paper="#f4f5f7", surface="#ffffff", ink="#16181d", muted="#5a6070",
                  rule="#d9dce3", accent="#2a46c9", soft="#e6eafb"),
    "dark": dict(gh="#0d1117", paper="#101217", surface="#171a21", ink="#e7e9ef", muted="#9aa1b2",
                 rule="#2a2f3a", accent="#93a6ff", soft="#1f2640"),
}
ERAS = [  # (years, title, [(name, label, kind)]) kind: try | code | none
    ("2011–2017", "Games, one per language I learned", [
        ("BLUE DICE GAME", "2011", "code"), ("Mukbo DB", "2011", "code"), ("Rolly Poly", "2011", "code"),
        ("Teris", "2011", "code"), ("Space Shooter", "2012", "code"), ("PackMan plus", "2012", "code"),
        ("Angry Pokemons", "2014", "code"), ("WarmyLand", "2015", "code"), ("3D Maze", "2016", "code"),
        ("CrashTower", "2017", "code")]),
    ("2019–2021", "Web and backend", [("Nexon Dabang M", "2019", "code"), ("Excel download", "2020", "code"),
                                    ("Docs from tests", "2021", "code")]),
    ("2026", "AI tools", [("Team AI workflow", "2026", "none"), ("Persona debate lab", "try it", "try"),
                          ("Vancouver room hunt", "try it", "try"), ("AI trend digest", "try it", "try"),
                          ("AI news service", "idea", "none")]),
]
BASE = """body{{margin:0;background:{gh}}}.p{{box-sizing:border-box;width:960px;background:{paper};border:1px solid {rule};
border-radius:12px;padding:40px 46px 36px;font-family:'IBM Plex Sans',sans-serif;color:{ink}}}"""

def banner(c):
    css = BASE.format(**c) + f"""h1{{font-family:Silkscreen;font-weight:400;font-size:70px;line-height:1;margin:0;letter-spacing:.02em}}
.i{{font-size:19px;margin:20px 0 0;max-width:62ch;line-height:1.55}}.l{{font-family:'IBM Plex Mono';font-size:15px;color:{c['accent']};margin:16px 0 0}}"""
    body = ('<h1>BNI TECH</h1><p class="i">Ideas I have built and kept running. Each one works without me: '
            'you can try it on your own, in minutes, from its repository.</p>')
    return css, body

def timeline(c):
    css = BASE.format(**c) + f"""h2{{font-size:15px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:{c['muted']};margin:0 0 22px}}
.eras{{display:grid;grid-template-columns:2fr 1fr 1.15fr;gap:26px}}.y{{font-family:'IBM Plex Mono';font-weight:500;color:{c['accent']};font-size:15px}}
.bar{{height:6px;border-radius:3px;background:{c['accent']};margin:8px 0 12px}}.t{{font-weight:600;font-size:16px;margin:0 0 12px}}
.chips{{display:grid;gap:8px}}.two{{grid-template-columns:1fr 1fr}}.c{{display:flex;justify-content:space-between;align-items:center;
border:1px solid {c['rule']};background:{c['surface']};border-radius:6px;padding:6px 11px;font-size:14.5px;font-weight:500}}
.c span{{font-family:'IBM Plex Mono';font-size:12px;color:{c['muted']};font-weight:400}}.none{{border-style:dashed;color:{c['muted']};font-weight:400;background:transparent}}
.try{{background:{c['soft']};border-color:{c['accent']}}}.try span{{color:{c['accent']};font-weight:500}}
.k{{font-family:'IBM Plex Mono';font-size:12.5px;color:{c['muted']};margin:20px 0 0}}"""
    cols = []
    for years, title, items in ERAS:
        chips = "".join(f'<div class="c {"" if k == "code" else k}">{n}<span>{lab}</span></div>' for n, lab, k in items)
        two = " two" if len(items) > 6 else ""
        cols.append(f'<div><div class="y">{years}</div><div class="bar"></div><p class="t">{title}</p>'
                    f'<div class="chips{two}">{chips}</div></div>')
    body = (f'<h2>Ideas by the year they started</h2><div class="eras">{"".join(cols)}</div>'
            '<p class="k">blue: try it yourself in minutes · solid: public code · dashed: no public code</p>')
    return css, body

for name, fn, height in (("banner", banner, 232), ("timeline", timeline, 440)):
    for theme, c in THEMES.items():
        css, body = fn(c)
        html = os.path.join(OUT, f"{name}-{theme}.html")
        with open(html, "w", encoding="utf-8") as f:
            f.write(f"<html><head>{FONTS}<style>{css}</style></head><body><div class='p'>{body}</div></body></html>")
        png = os.path.join(OUT, f"{name}-{theme}.png")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=6000",
                        "--force-device-scale-factor=2", f"--window-size=960,{height}", f"--screenshot={png}",
                        "file://" + os.path.abspath(html)], check=True, capture_output=True)
        os.remove(html)
        print(png)
