"""
__main__.py

Reads out settings and CLI params and runs bot with them
"""

import sys
import json
from src_constants  import CELESTE_GAMES
from celeste_bot    import CelesteLeaderboardBot
from data_models    import Credentials
from dacite         import from_dict


# define credentials global
creds_d : dict
# read out credentials dict
try:
    with open(sys.argv[1]) as file:
        creds_d = json.loads(file.read())
except IndexError:
    with open("./credentials.json") as file:
        creds_d = json.loads(file.read())
# parse dict to dataclass
creds = from_dict(
    data_class=Credentials,
    data=creds_d
)

# create and start bot
CelesteLeaderboardBot(**config).main()
