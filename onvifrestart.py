#!/usr/bin/env python3

import argparse
from onvif import ONVIFCamera

# parse command-line arguments
parser = argparse.ArgumentParser(description='Restart an ONVIF Camera')
parser.add_argument('ip', help='IP address of the camera')
parser.add_argument('port', type=int, help='Port number')
parser.add_argument('username', help='Username')
parser.add_argument('password', help='Password')
args = parser.parse_args()

# initialize the camera
cam = ONVIFCamera(args.ip, args.port, args.username, args.password)

# Get the device management service
devicemgmt_service = cam.create_devicemgmt_service()

# Restart the camera
devicemgmt_service.SystemReboot()

print("Camera restarted.")
