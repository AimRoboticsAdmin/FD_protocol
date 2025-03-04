from common import send_command

def set_speed(value):
    """Sets the motor speed. Value: 0-100 for forward, -100 to 0 for reverse."""
    send_command(f'speed {value}')

if __name__ == '__main__':
    set_speed(50)  # Example: Set speed to 50
