# ONVIF Camera Information Retrieval Tool

This Python script is designed to query and retrieve the stream URLs from an ONVIF-compliant IP camera.

## Requirements

- Python 3.x
- ONVIF-compliant IP Camera
- Python packages: `onvif-zeep`, `zeep`

## Installation

1. Clone the repository or download the script `getonvifinfo.py`.
2. Install required Python packages:

   ```bash
   pip install onvif-zeep zeep
   ```

## Usage

To use the script, run it from the command line with the IP address, port, username, and password of your ONVIF-compliant camera.

```bash
python getonvifinfo.py <ip_address> <port> <username> <password>
```

## Example

```bash
$ python getonvifinfo.py 192.168.4.58 80 admin p4ssw0rd
{'PROFILE_000': 'rtsp://192.168.4.58/live/0/MAIN', 'PROFILE_001': 'rtsp://192.168.4.58/live/0/SUB'}
```

This command retrieves the stream URLs for the main and sub-profiles from the camera at IP 192.168.4.58.

