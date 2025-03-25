
# speed.py
from common import send_command

def set_speed(value):
    """Sets the motor speed. Value: 0-100 for forward, -100 to 0 for reverse."""
    send_command(f'speed {value}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python speed.py <speed>")
    else:
        set_speed(sys.argv[1])

