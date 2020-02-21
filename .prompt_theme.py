#! /bin/python3
# João Pinto dropped a tip in `askubuntu.com`
# https://askubuntu.com/a/17738/122050
'''`prompt_theme` module:
- `prompt_theme()` method: generates random prompt theme.'''
from csv import reader
from socket import gethostname
from os import (environ, getcwd)
from datetime import datetime

RGB_COLORS = {}  # RGB colors dict
RGB_THEMES = {}  # RGB themes dict


def prompt_theme():
    '''`prompt_theme()` method generates random prompt theme.'''
    # CSV file
    with open('/home/foo/scripts/prompt_theme/colors.csv', 'r') as colors_file:
        colors_reader = reader(colors_file)  # CSV reader
        for color in colors_reader:
            RGB_COLORS[color[0]] = color[1]  # generate RGB colors dict
    # CSV file
    with open('/home/foo/scripts/prompt_theme/themes.csv', 'r') as themes_file:
        themes_reader = reader(themes_file)  # CSV reader
        for theme in enumerate(themes_reader, 1):
            RGB_THEMES[theme[0]] = theme[1]  # generate enumerated themes dict

    dt = datetime.today()  # date and time object (now)
    _month = dt.month  # month number
    _day = dt.day  # day number

    if (_month % 2) == 0:
        _theme = RGB_THEMES[_day + 31]  # theme for even month
    else:
        _theme = RGB_THEMES[_day]  # theme for odd month

    _user = environ['USER']  # username
    _host = gethostname()  # hostname
    _dir = getcwd()  # current working dir
    _prompt = f'\\[\\033[1;7m\\033[38;2;{RGB_COLORS[_theme[0]]}m\\]{_user}'
    _prompt += f'\\[\\033[38;2;{RGB_COLORS[_theme[1]]}m\\]@{_host}'  # hostname
    _prompt += f'\\[\\033[38;2;{RGB_COLORS[_theme[2]]}m\\] {_dir} '  # cwd
    _prompt += f'\\[\\033[0m\\]\\$ '  # reset format to default
    print(_prompt)  # print Bash prompt


if __name__ == '__main__':
    prompt_theme()
