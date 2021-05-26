"""
__main__.py

Reads out settings and CLI params and runs bot with them
"""

from celeste_bot import CelesteLeaderboardBot

# TODO read out settings
config : dict = {
    "key"   : None,
    "timer" : 5,
    "games" : [
        {
            "id"      : "o1y9j9v6",
            "name"    : "Celeste",
            "version" : {
                "id_var" : "",
                "id_val" : "" 
            }
        }
    ]
}

CelesteLeaderboardBot(**config).start()
