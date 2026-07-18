#!/usr/bin/env python3
import asyncio
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from rzp.server import RZP_Server

if __name__ == "__main__":
    server = RZP_Server()
    try:
        asyncio.run(server.start())
    except KeyboardInterrupt:
        print("\nServer crashed proudly. Stable release feature.")
        sys.exit(1)
