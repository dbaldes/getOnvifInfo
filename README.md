# ONVIF Camera Tools

**getonvifinfo.py** is a simple python script that retrieves available RTSP stream URLs and, optionally,
device capabilities and device information from an ONVIF camera.
I found that it is often difficult to find the stream URLs and other information of a
camera without such a tool.

**onvifrestart.py** is a python script that restarts a camera using the ONVIF protocol. I got some cheap
cameras that need regular restarting.

## Installation

1. Clone the repository
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Make the scripts executable:
   ```bash
   chmod u+x *.py
   ```

## Usage

To use the scripts, run them from the command line with the IP address, port, username, and password of your ONVIF-compliant camera.

```bash
$ ./getonvifinfo.py -h
usage: getonvifinfo.py [-h] [--info] [--capabilities] ip port username password

Get ONVIF Camera Information and Stream URLs

positional arguments:
  ip                  IP address of the camera
  port                Port number
  username            Username
  password            Password

options:
  -h, --help          show this help message and exit
  --info, -i          Print device info
  --capabilities, -c  Print camera capabilities
```

```bash
$ ./onvifrestart.py -h
usage: onvifrestart.py [-h] ip port username password

Restart an ONVIF Camera

positional arguments:
  ip          IP address of the camera
  port        Port number
  username    Username
  password    Password

options:
  -h, --help  show this help message and exit
```

## Example

```bash
$ ./getonvifinfo.py 192.168.103.245 10080 admin p4ssw0rd --info
PROFILE_000: rtsp://192.168.103.245:10554/tcp/av0_0
PROFILE_001: rtsp://192.168.103.245:10554/tcp/av0_1

Device Info:

Manufacturer: IP camera
Model: IP Camera
FirmwareVersion: 2.4
SerialNumber: AAC0996975AFPN
HardwareId: 1.0
```

