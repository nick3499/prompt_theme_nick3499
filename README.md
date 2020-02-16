# prompt_theme_nick3499
Random Bash prompt bg color themes:

Methods used:

- random.choice()
- csv.reader()
- socket.gethostname()
- os.environ()
- os.getcwd()

This repo has been made available under the [MIT](https://opensource.org/licenses/MIT) open source license.

The `.prompt_theme.py` Python3 script was tested with:

- Linux kernel 5.4.0-14-generic
- Ubuntu 20.04 (Focal Fossa) (development branch)
- Python 3.8.2rc1 (Feb 12 2020)

## .bashrc

Append the following lines to your Bash run commands file:

```shell
export TERM=xterm-256color;
export PROMPT_COMMAND='PS1="$(python3 /home/nick/.userpy/prompt_theme/.prompt_theme.py)"'
```

`export TERM=xterm-256color;` is mainly for `xterm` to handle 256 colors. _The value of the variable [PROMPT_COMMAND](https://www.gnu.org/software/bash/manual/html_node/Controlling-the-Prompt.html#index-prompting) is examined just before Bash prints each primary prompt._

Those exports can also be found in the `.prompt_theme.sh` dot file.

## RGB_COLORS

`RGB_COLORS` contains **color names** with their semicolon-separated **RGB values**:

```csv
affair_8c489f,140;72;159
albescent_white_f6e7d2,246;231;210
anakiwa_99ccff,153;204;255
aquamarine_66ffff,102;255;255
astronaut_29407c,41;64;124
avocado_999967,153;153;103
azure_336699,51;102;153
azure_radiance_0099FF,0;153;255
bahama_blue_006699,0;102;153
bitter_lemon_d5d50d,213;213;13
. . .
```

## RGB_THEMES

`RGB_THEMES` contains three-color **theme names**.

```csv
anakiwa_99ccff,de_york_99cc99,tangerine_ffcc00
astronaut_29407c,lonestar_660000,pirate_gold_d08504
azure_336699,dove_gray_666666,dusty_gray_999999
bahama_blue_006699,pacific_blue_0099cc,dolly_ffff81
blue_bell_9999cc,de_york_99cc99,cream_ffffcc
blue_stone_006666,buddha_gold_cc9900,school_bus_yellow_ffde00
bossanova_443266,affair_8c489f,periwinkle_gray_c3c3e5
brown_4d1a00,oregon_993300,orange_e64d00
buccaneer_663333,grenadier_cc3300,peach_orange_ffcc99
burgundy_8c001a,sushi_8ca93e,texas_f6fa9c
. . .
```

## prompt_theme()

`prompt_theme()` method opens `colors.csv` and `themes.csv`. Then creates CSV readers with them, which are iterated through to generate both `RGB_COLORS` and `RGB_THEMES` dictionaries.

## rand_num

`rand_num = choice(list(RGB_THEMES.keys()))` provides a pseudo-random number for theme choice&mdash;a random theme based on enumerated values which prefix the theme records.

## rand_theme

`rand_theme = RGB_THEMES[rand_num]` assigns the three-color list of names to `rand_theme`.

## _user, _host, _dir

`_user = environ['USER']`, `_host = gethostname()` and `_dir = getcwd()` get the **username**, **hostname** and **working directory**.

## _prompt

To keep the value of `_prompt` from extending too far beyond 79 characters, it was split up into four sections:

- user
- host
- current working directory
- reset to default text format

```python
_prompt = f'\\[\\033[1;7m\\033[38;2;{RGB_COLORS[rand_theme[0]]}m\\]{_user}'
_prompt += f'\\[\\033[38;2;{RGB_COLORS[rand_theme[1]]}m\\]@{_host}'
_prompt += f'\\[\\033[38;2;{RGB_COLORS[rand_theme[2]]}m\\] {_dir} '
_prompt += f'\\[\\033[0m\\]\\$ '  # reset format to default
```

## print()

Finally, the `_prompt` is printed:

```python
print(_prompt)
```

## Future Plans

Considering how the constantly changing prompt themes may become annoying, I have considered reducing the total number of themes to thirty-one, and using the `datetime` module to feature one theme per day. Another option would be to increase the total number of themes to 62, and feature one theme per day for two months.
