from common import send_command

def stop_motor():
    """Stops the motor."""
    send_command('22222')

if __name__ == '__main__':
    stop_motor()
