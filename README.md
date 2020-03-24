# intel-backlight-change
A script which allows to change the backlight on GNU/Linux for the intel cpu.

The script is intended to be run from a program like sxhkd, or a tiling window manager like XMonad, BSPWM, or simply from the terminal.

## Prerequisites:
* Python3.8 or higher
* The user must be part of the video group

## Dependency
* There are no dependency to install

## How does it work
* Make the ibc script executable

## Commands
* `--help, -h` List all available commands
* `--current, -c` Display the current value of the brightness
* `--max, -m` Display the maximum value of the brightness (usually 976)
* `--set, -s` Set the current value of the brightness
* `--inc, -i` Increment the value of the brightness (default by 100)
* `--dec, -d` Decrement the value of the brightness (default by -100)
