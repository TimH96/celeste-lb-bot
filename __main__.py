"""
__main__.py

Reads out settings and CLI params and runs bot with them
"""

from celeste_bot import CelesteLeaderboardBot

# TODO read out settings
config : dict = {
    "key"   : None,
    "timer" : 60,
    "games" : [
        "o1y9j9v6"
    ]
}

CelesteLeaderboardBot(**config).start()
