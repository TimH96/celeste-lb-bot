"""
src_constants.py

holds global speedrun.com API constants
"""

from data_models    import CelesteGames
from dacite         import from_dict


CELESTE_GAME_CONSTANTS = from_dict(
    data_class=CelesteGames,
    data={
        "games" : [
            {
                "id"      : "o1y9j9v6",
                "name"    : "Celeste",
                "version" : {
                    "variable_id" : "38do9y4l",
                    "default_ver" : "5q8e7y3q",
                    "invalid_ver" : {
                        "nzelkr6q" : ["810gdx5l", "zqoo4vxq"],
                        "o7e2mx6w" : ["810gdx5l", "zqoo4vxq", "21dg78p1"],
                        "8gej2n93" : [],
                    }
                }
            }
        ]
    }
)

PLATFORMS : dict = {
    "PlayStation 4" : "nzelkr6q",
    "Xbox One"      : "o7e2mx6w",
    "PC"            : "8gej2n93",
    "Switch"        : "7m6ylw9p",
    "Google Stadia" : "o064z1e3",
    "PlayStation 5" : "4p9zjrer"
}
