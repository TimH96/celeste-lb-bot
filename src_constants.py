"""
src_constants.py

holds global speedrun.com API constants
"""

from data_models    import BotConfig
from dacite         import from_dict

# hardcode celeste-specific speedrun.com api config
# this mainly encompasses speedrun.com internal IDs and similar constants, which are static and specific to celeste
# it is therefore not advised to extract this into actual data (be it a .json file or a database even)
CELESTE_API_CONSTANTS = from_dict(
    data_class=BotConfig,
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
