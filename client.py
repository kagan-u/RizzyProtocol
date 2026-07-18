#!/usr/bin/env python3
import asyncio
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from rzp.client import RZP_Client

if __name__ == "__main__":
    client = RZP_Client()
    try:
        asyncio.run(client.communicate())
    except KeyboardInterrupt:
        print("\nClient leaving. probably")
        sys.exit(1)
