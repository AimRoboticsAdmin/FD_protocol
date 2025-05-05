import serial
import time

#Serial port settings
SERIAL_PORT = 'COM4' #Change this to your Arduino's USB port (COM for windows)
BAUD_RATE = 115200

def send_command(command):
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
        ser.write((command + '\n').encode())
        time.sleep(0.1) #wait for adruino to process the command
        response = ser.read(ser.in_waiting).decode().strip()
        if response:
            print(f"From Arduino: {response}")