# .github

The BNI Tech organization profile shown at [github.com/bnitech-lab](https://github.com/bnitech-lab).

- `profile/README.md` is the profile itself: a front door to [bnitech-lab.github.io](https://bnitech-lab.github.io),
  my lab page. It links the page's six topics (`#topic=<key>`) and lists the games whose code lives in this
  organization. It holds no counts, so it does not go out of date when the page grows.
- `profile/assets/` holds the banner, light and dark. It is drawn in the page's fonts (Silkscreen, Space Grotesk
  and Space Mono) and colours, because GitHub does not load web fonts or CSS in a README.
- `tools/make_images.py` redraws the banner. It needs Google Chrome, which loads the fonts from Google Fonts. Run
  `python3 tools/make_images.py` when the page's wording or look changes.
