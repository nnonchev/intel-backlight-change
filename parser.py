import argparse

def parser():
    parser = argparse.ArgumentParser(
        description = 'ibc - Intel Backlight Change.'
    )
    group = parser.add_mutually_exclusive_group()
    
    parser.add_argument(
            '--current',
            '-c',
            help = 'Get current value',
            action = 'store_true'
    )
    
    parser.add_argument(
            '--max',
            '-m',
            help = 'Get max value',
            action = 'store_true'
    )
    
    group.add_argument(
            '--set',
            '-s',
            help = 'Set current value',
            type = int
    )
    
    group.add_argument(
            '--inc',
            '-i',
            help = 'Increment current value',
            action = 'store_true'
    )
    
    group.add_argument(
            '--dec',
            '-d',
            help='Decrement current value',
            action = 'store_true'
    )
    
    return parser.parse_args()

