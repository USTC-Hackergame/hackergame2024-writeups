#!/usr/bin/env python
import argparse

from pyVNC.Client import Client

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1", type=str, help="Hostname of the VNC Server")
    parser.add_argument("--port", default="5902", type=int, help="VNC Server Port")
    parser.add_argument("--password", default=None, type=str, help="Password of the VNC Server")
    parser.add_argument("--depth", default=32, type=int, help="Color Depth")
    parser.add_argument("--fast", default=False, type=bool,  help="Fast encoding")
    parser.add_argument("--shared", default=False, type=bool,  help="Shared VNC Instance")
    args = parser.parse_args()

    vnc = Client(host=args.host,
                    port=args.port,
                    password=args.password,
                    depth=args.depth,
                    fast=args.fast,
                    shared=args.shared,
                    gui=True,
                    gui_with_array=False
                 )
    vnc.start()


