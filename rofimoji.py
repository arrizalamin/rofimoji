#!/usr/bin/python3
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import os
from time import time
import requests
from bs4 import BeautifulSoup

urls = [
    'https://emojipedia.org/people/',
    'https://emojipedia.org/nature/',
    'https://emojipedia.org/food-drink/',
    'https://emojipedia.org/activity/',
    'https://emojipedia.org/travel-places/',
    'https://emojipedia.org/objects/',
    'https://emojipedia.org/symbols/',
    'https://emojipedia.org/flags/']

emoji_cache = os.path.join(os.path.expanduser('~'), '.cache/rofimojis')


def refresh_cache():
    text = ''
    for url in urls:
        data = requests.get(url)  # type: requests.Response
        soup = BeautifulSoup(data.content, 'lxml')  # type: BeautifulSoup

        soup = soup.find("div", attrs={"class": "content"})
        for table_row in soup.find_all('li'):
            emoji_row = table_row.find('a')
            text += emoji_row.get_text() + '\n'
    with open(emoji_cache, 'w') as f:
        f.write(text)

    return text


def open_cache():
    with open(emoji_cache, 'r') as f:
        return f.read()


def get_emojis():
    if not os.path.exists(emoji_cache):
        return refresh_cache()

    last_modified = os.stat(emoji_cache).st_mtime
    if (time() - last_modified >= 60 * 60 * 24 * 30):
        return refresh_cache()

    return open_cache()


emojis = get_emojis()

rofi = Popen(
    args=[
        'rofi',
        '-dmenu',
        '-i',
        '-p',
        ' 😀   ',
        '-kb-custom-1',
        'Alt+c'
    ],
    stdin=PIPE,
    stdout=PIPE
)
(stdout, stderr) = rofi.communicate(input=emojis.encode('utf-8'))

if rofi.returncode == 1:
    exit()
else:
    emoji = stdout.split()[0]
    if rofi.returncode == 0:
        Popen(
            args=[
                'xdotool',
                'type',
                '--clearmodifiers',
                emoji.decode('utf-8')
            ]
        )
    elif rofi.returncode == 10:
        xsel = Popen(
            args=[
                'xsel',
                '-i',
                '-b'
            ],
            stdin=PIPE
        )
        xsel.communicate(input=emoji)
