# prompt_theme_nick3499
Random Bash prompt bg color themes: random.choice(), csv.reader(), socket.gethostname(), os

## .bashrc

Append the following lines to your Bash run commands file:

```shell
export TERM=xterm-256color;
export PROMPT_COMMAND='PS1="$(python3 /home/foo/scripts/prompt_theme/.prompt_theme.py)"'
```

`export TERM=xterm-256color;` is mainly for `xterm` to handle 256 colors. _The value of the variable [PROMPT_COMMAND](https://www.gnu.org/software/bash/manual/html_node/Controlling-the-Prompt.html#index-prompting) is examined just before Bash prints each primary prompt._

Those exports can also be found in the `.prompt_theme.sh` dot file.

