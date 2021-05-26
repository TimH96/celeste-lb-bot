"""
__main__.py

Reads out settings and CLI params and runs bot with them
"""

import sys
import json
from celeste_bot import CelesteLeaderboardBot

# define config global
config : dict

# read out config
try:
    with open(sys.argv[1]) as file:
        config = json.loads(file.read())
except IndexError:
    with open("./config.json") as file:
        config = json.loads(file.read())

# create and start bot
CelesteLeaderboardBot(**config).start()
