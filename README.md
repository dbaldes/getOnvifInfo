# ONVIF Camera Information Retrieval Tool

This is a simple python script that retrieves available RTSP stream URLs and, optionally,
device capabilities and device information from an ONVIF camera.
I found that it is often difficult to find the stream URLs and other information of a
camera without such a tool.

## Installation

1. Clone the repository
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Make the script executable:
   ```bash
   chmod u+x getonvifinfo.py
   ```

## Usage

To use the script, run it from the command line with the IP address, port, username, and password of your ONVIF-compliant camera.

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

