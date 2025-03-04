

# **FD Dispensing Unit Command Interface**

This repository contains individual Python scripts to control the **FD Dispensing Unit** using serial commands. Each script corresponds to a specific command that can be sent to the FD dispensing unit via a serial port.

---

## **Prerequisites**

- Python 3.x
- `pyserial` library

---

## **Installation**

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install the required library:**
   ```bash
   pip install pyserial
   ```

3. **Update the serial port:**

Modify the `SERIAL_PORT` variable in **common.py** to match your specific USB port (e.g., `/dev/ttyUSB0` on Linux/Mac or `COMx` on Windows).

---

## **Usage**
Each script can be executed independently from the command line to send specific commands to the FD dispensing unit.

### **Common Functionality**
All scripts use the `send_command` function defined in `common.py` to handle serial communication.

---

## **Commands**

### **Set Motor to Maximum Power**
**Script:** `max.py`

```bash
python max.py
```

### **Set Motor to Reduced Power**
**Script:** `reduced.py`

```bash
python reduced.py
```

### **Set Motor Speed**
**Script:** `speed.py`

**Usage:** Provide the speed as a command-line argument.

**Value Limits:** Normal values are between **0 - 100** for forward motion and **-100 to 0** for reverse motion.

```bash
python speed.py <speed>
```

**Example:**
```bash
python speed.py 50
```

### **Stop Motor**
**Script:** `stop.py`

```bash
python stop.py
```

### **Check Connection**
**Script:** `ping.py`

```bash
python ping.py
```

---

## **Example Commands**

**Set motor to maximum power:**
```bash
python max.py
```

**Set motor to reduced power:**
```bash
python reduced.py
```

**Set motor speed to 50:**
```bash
python speed.py 50
```

**Stop motor:**
```bash
python stop.py
```

**Check FD unit connection:**
```bash
python ping.py
```

---

## **Notes**
- Ensure that the **`SERIAL_PORT`** in `common.py` is correctly set to match the connected USB port of the FD dispensing unit.
- The scripts expect the FD dispensing unit to respond with data. Ensure the unit is properly connected and configured before executing commands.
- The **motor speed setting is crucial** for the proper operation of dispensing. Adjust it as needed before starting any movement.

