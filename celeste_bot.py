"""
celeste_bot.py
"""

import json
from threading  import Timer
from urllib     import request


class CelesteLeaderboardBot:
    """Class for leaderboard bot, interacting with speedrun.com API"""

    def __init__(self, *, key: str, timer: float, games: list) -> None:
        self.KEY   : str   = key
        self.GAMES : float = games
        self.TIMER : list  = timer

    def main(self, ignore: list = [], loop: bool = False) -> None:
        """
            Main validation function.

            Checks for the validity of any new submission not in the given ignore list and rejects them if necessary.
        """

        cache : list = []
        # loop over all games
        for game in self.GAMES:
            try:
                new_runs : dict = json.loads(
                    request.urlopen("https://www.speedrun.com/api/v1/runs?game={}&status=new".format(game["id"])).read()
                )
                # loop over all new runs of a given game
                for run in new_runs["data"]:
                    print(run["values"])
                    # cache run for next iteration and skip if it was cached last iteration
                    cache.append(run["id"])
                    if run["id"] in ignore:
                        print("continued")
                        continue
                    # validity checks
                    pass
                
            except Exception: pass  # TODO !!! error handling on: HTTP404 or OS Conn Refused, prolly just continue
        # loop again if running from start()
        if loop:
                Timer(self.TIMER, self.main, [cache, loop]).start()

    def start(self) -> None:
        """Start bot, blocking calling thread"""
        self.main([], True)

"""TIMER_OFFSET : dict = {
    0  : 0,
    1  : 2,
    2  : 4,
    3  : 6,
    4  : 3,
    5  : 10,
    6  : 12,
    7  : 14,
    8  : 16,
    9  : 1,
    10 : 3,
    11 : 5,
    12 : 7,
    13 : 9,
    14 : 11,
    15 : 13,
    16 : 15
}

def is_valid_decimal(time: float):
    if time == 0: return False
    nat : int = int(time)
    dec : int = 0 if (time - int(time) == 0) else int(1000 * float("0." + str(time).split(".")[1]))  # dec is decimals of number * 1000
    print(nat, dec)
    print((TIMER_OFFSET[nat % 17] + dec) % 17)

is_valid_decimal(140.352)"""

# test main method
if __name__ == '__main__':
    config : dict = {
        "key"   : None,
        "timer" : 60,
        "games" : [
            {
                "id"      : "o1y9j9v6",
                "name"    : "Celeste",
                "version" : {
                    "id_var" : "38do9y4l",
                    "id_val" : "" 
                }
            }
        ]
    }

    CelesteLeaderboardBot(**config).main()
