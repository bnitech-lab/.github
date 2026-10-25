# .github

The BNI Tech organization profile shown at [github.com/bnitech-lab](https://github.com/bnitech-lab).

- `profile/README.md` is the profile itself.
- `profile/assets/` holds the banner and the by-year picture, light and dark. They are drawn in the
  fonts of [bnitech-lab.github.io](https://bnitech-lab.github.io) (Silkscreen and IBM Plex), because
  GitHub does not load web fonts in a README.
- `tools/make_images.py` redraws both pictures. It needs Google Chrome, which loads the fonts from
  Google Fonts. When an idea is marked public on the page, edit `ERAS` in the script and run
  `python3 tools/make_images.py`.
