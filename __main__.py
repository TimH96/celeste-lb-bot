"""
__main__.py

Reads out settings and CLI params and runs bot with them
"""

import json
from src_constants  import CELESTE_GAMES
from celeste_bot    import CelesteLeaderboardBot
from data_models    import Credentials
from dacite         import from_dict
from argparse       import ArgumentParser, Namespace


# argparse
parser : ArgumentParser = ArgumentParser(
    description='Celeste speedrun.com bot to reject faulty submissions',
    allow_abbrev=True
)
parser.add_argument(
    '-c', '--credentials',
    type=str,
    help='path to credentials.json file',
    default='./default.json'
)
parser.add_argument(
    '-t', '--timer',
    type=int,
    help='interval between polls',
    default=60
)
args : Namespace = parser.parse_args()
# read out credentials dict
with open(args.credentials) as file:
    creds_d : dict = json.loads(file.read())
# parse dict to dataclass
creds = from_dict(
    data_class=Credentials,
    data=creds_d
)

# create and start bot
CelesteLeaderboardBot(creds, CELESTE_GAMES, args.timer).start()
