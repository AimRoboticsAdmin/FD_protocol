from common import send_command

def ping_device():
    """Checks if the FD dispensing unit is connected and responsive."""
    send_command('ping')

if __name__ == '__main__':
    ping_device()
