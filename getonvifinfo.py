#!/usr/bin/env python3

import argparse
from onvif import ONVIFCamera
import zeep

def get_camera_info(ip, port, username, password):
    # initialize the camera
    mycam = ONVIFCamera(ip, port, username, password)

    # create media service
    media_service = mycam.create_media_service()

    # get profiles
    profiles = media_service.GetProfiles()

    # getting the stream URI
    stream_uris = {}
    for profile in profiles:
        try:
            request = media_service.create_type('GetStreamUri')
            request.ProfileToken = profile.token
            request.StreamSetup = {'Stream': 'RTP-Unicast', 'Transport': {'Protocol': 'RTSP'}}
            stream_uris[profile.Name] = media_service.GetStreamUri(request).Uri
        except Exception as e:
            print(f"Error getting stream URI for {profile.Name}: {e}")

    return stream_uris

# parse command-line arguments
parser = argparse.ArgumentParser(description='Get ONVIF Camera Information and Stream URLs')
parser.add_argument('ip', help='IP address of the camera')
parser.add_argument('port', type=int, help='Port number')
parser.add_argument('username', help='Username')
parser.add_argument('password', help='Password')
args = parser.parse_args()

# get camera stream URLs
stream_uris = get_camera_info(args.ip, args.port, args.username, args.password)

# print each profile name and URI on a new line
for name, uri in stream_uris.items():
    print(f"{name}: {uri}")
