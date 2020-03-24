from sys import argv

PATH = "/sys/class/backlight/intel_backlight"
BRIGHTNESS = '/brightness'
MAX_BRIGHTNESS = '/max_brightness'


def getMax():
    global MAX_BRIGHTNESS, PATH

    max_val = None

    with open(f'{PATH}/{MAX_BRIGHTNESS}', 'r') as f:
        max_val = f.readline().strip()

    return int(max_val)


def getCurrent():
    global BRIGHTNESS, PATH

    cur_val = None

    with open(f'{PATH}/{BRIGHTNESS}', 'r') as f:
        cur_val = f.readline().strip()

    return int(cur_val)


def setCurrent(val):
    global BRIGHTNESS, PATH

    max_val = getMax()

    res = False

    if 0 <= val <= max_val:
        res = True
        with open(f'{PATH}/{BRIGHTNESS}', 'w') as f:
            f.write(str(val))

    return res


def increment():
    global BRIGHTNESS, PATH
    
    cur_val = getCurrent() + 100
    max_val = getMax()

    res = True

    if cur_val > max_val:
        cur_val = max_val
        res = False

    with open(f'{PATH}/{BRIGHTNESS}', 'w') as f:
        f.write(str(cur_val))

    return res


def decrement():
    global BRIGHTNESS, PATH
    
    cur_val = getCurrent() - 100

    res = True

    if cur_val < 0:
        cur_val = 0
        res = False

    with open(f'{PATH}/{BRIGHTNESS}', 'w') as f:
        f.write(str(cur_val))

    return res
