#!/usr/bin/env python3

import argparse
from onvif import ONVIFCamera
import zeep

def get_stream_uris(cam):
    # create media service
    media_service = cam.create_media_service()

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

def get_capabilities(cam):
    # get the device management service
    devicemgmt_service = cam.create_devicemgmt_service()

    # get the device capabilities
    return devicemgmt_service.GetCapabilities({'Category': 'All'})

def print_capabilities(capabilities):
    def recurse_dict(d, indent=0):
        if isinstance(d, dict):
            for key, value in d.items():
                if key == '__values__':
                    recurse_dict(value, indent)
                elif value is None:
                    print('  ' * indent + f'{key}: None')
                elif isinstance(value, list) and key == 'SupportedVersions':
                    print('  ' * indent + f'{key}:')
                    for version in value:
                        print('  ' * (indent + 1) + f'Version {version["Major"]}.{version["Minor"]}')
                elif isinstance(value, dict) or hasattr(value, '__dict__'):
                    print('  ' * indent + f'{key}:')
                    recurse_dict(value, indent + 1)
                else:
                    print('  ' * indent + f'{key}: {value}')
        elif hasattr(d, '__dict__'):
            for key, value in d.__dict__.items():
                if key == '__values__':
                    recurse_dict(value, indent)
                elif value is None:
                    print('  ' * indent + f'{key}: None')
                elif isinstance(value, list) and key == 'SupportedVersions':
                    print('  ' * indent + f'{key}:')
                    for version in value:
                        print('  ' * (indent + 1) + f'Version {version["Major"]}.{version["Minor"]}')
                elif isinstance(value, dict) or hasattr(value, '__dict__'):
                    print('  ' * indent + f'{key}:')
                    recurse_dict(value, indent + 1)
                else:
                    print('  ' * indent + f'{key}: {value}')
        else:
            print('  ' * indent + str(d))

    print("Device Capabilities:")
    recurse_dict(capabilities)

# parse command-line arguments
parser = argparse.ArgumentParser(description='Get ONVIF Camera Information and Stream URLs')
parser.add_argument('ip', help='IP address of the camera')
parser.add_argument('port', type=int, help='Port number')
parser.add_argument('username', help='Username')
parser.add_argument('password', help='Password')
parser.add_argument('--capabilities', '-c', action='store_true', help='Print camera capabilities')
args = parser.parse_args()

# initialize the camera
cam = ONVIFCamera(args.ip, args.port, args.username, args.password)

# get camera stream URLs
stream_uris = get_stream_uris(cam)

# print each profile name and URI on a new line
for name, uri in stream_uris.items():
    print(f"{name}: {uri}")

if args.capabilities:
    capabilities = get_capabilities(cam)
    print_capabilities(capabilities)
