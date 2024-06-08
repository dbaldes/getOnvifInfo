# ONVIF Camera Information Retrieval Tool

This is a simple python script that retrieves available RTSP stream URLs from an ONVIF camera.
I found that it is often difficult to find the stream URLs without such a tool.

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
./getonvifinfo.py <ip_address> <port> <username> <password>
```

## Example

```bash
$ ./getonvifinfo.py 192.168.4.58 8999 admin p4ssw0rd
MainStream: rtsp://192.168.4.58:554/1/h264major
SubStream: rtsp://192.168.4.58:554/1/h264minor
```

