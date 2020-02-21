#! /bin/python3
'''`print_themes` module contains the `print_themes()` method
which generates random prompt background color themes.
prints a generic prompt, followed by color names.'''
from csv import reader

RGB_COLORS = {}  # RGB colors dict
RGB_THEMES = {}  # RGB themes dict


def print_themes():
    '''`prompt_theme()` method prints list of prompt examples,
along with color names within available themes.'''
    # CSV file
    with open('/home/nick/.userpy/prompt_theme/colors.csv', 'r') as colors_file:
        colors_reader = reader(colors_file)  # CSV reader
        for color in colors_reader:
            RGB_COLORS[color[0]] = color[1]  # generate RGB colors dict
    # CSV file
    with open('/home/nick/.userpy/prompt_theme/themes.csv', 'r') as themes_file:
        themes_reader = reader(themes_file)  # CSV reader
        for theme in enumerate(themes_reader, 1):
            RGB_THEMES[theme[0]] = theme[1]  # generate enumerated themes dict
    # print color themes
    for i in RGB_THEMES:
        color_1 = RGB_COLORS[RGB_THEMES[i][0]]  # foo user color
        color_2 = RGB_COLORS[RGB_THEMES[i][1]]  # foo host color
        color_3 = RGB_COLORS[RGB_THEMES[i][2]]  # foo cwd color
        print(f'\x1b[1;7m\x1b[38;2;{color_1}mfoo\x1b[38;2;{color_2}m@foo-host\x1b[38;2;{color_3}m /home/foo/scripts \x1b[0m$ {RGB_THEMES[i][0]} | {RGB_THEMES[i][1]} | {RGB_THEMES[i][2]}')


if __name__ == '__main__':
    print_themes()
