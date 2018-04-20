# Emoji-Picker

This repo is a fork of [fdw/rofimoji](https://github.com/fdw/rofimoji) with auto-update emoji list

How often did you want to insert one of those Unicode emoji only to learn that there is no nice picker for Linux?
Fear no more, this script uses the power of [rofi](https://github.com/DaveDavenport/rofi/) to present exactly the picker you always wanted.
Inserts the selected emoji directly, or copies it to the clipboard.

## Usage

1. Run `rofimoji.py`
2. Search for the emoji you want
3. - Hit enter to insert the emoji directly
   - Hit `Alt+c` to copy it to the clipboard
4. 🎠

## How does it look?

![Screenshot of rofimoji](screenshot.png?raw=true)

## Installation

Download `rofimoji.py` and move it somewhere on your path, for example `/usr/local/bin`.

What else do you need:
- Python 3
- A font that can display emoji, for example [EmojiOne](https://github.com/emojione/emojione) or [Noto Emoji](https://www.google.com/get/noto/)
- xdotool for typing the emoji
- xsel to copy the emoji to the clipboard

For Ubuntu zesty: `sudo aptitude install python3 fonts-emojione xsel xdotool`
