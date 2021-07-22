"""
__main__.py

Reads out settings and CLI params and runs bot with them
"""

import sys
import json
from _config        import CELESTE_API_CONSTANTS
from celeste_bot    import CelesteLeaderboardBot


# define credentials global
creds : dict

# read out credentials dict
try:
    with open(sys.argv[1]) as file:
        creds = json.loads(file.read())
except IndexError:
    with open("./config.json") as file:
        creds = json.loads(file.read())

# create and start bot
#CelesteLeaderboardBot(**config).start()
