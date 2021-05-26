"""
celeste_bot.py
"""

import json
from threading  import Timer
from urllib     import request
from enum       import IntEnum


class SubmissionErrors(IntEnum):
    ERROR_SUBMITTED_RTA   = 0
    ERROR_INVALID_VERSION = 1
    ERROR_INVALID_IGT     = 2


class CelesteLeaderboardBot:
    """Class for leaderboard bot, interacting with speedrun.com API"""

    def __init__(self, *, key: str, timer: float, games: list) -> None:
        self.KEY   : str   = key
        self.GAMES : float = games
        self.TIMER : list  = timer

    @staticmethod
    def _valid_real_time(cls, run : dict) -> bool:
        return run["times"]["realtime_t"] == 0
    
    @staticmethod
    def _valid_version(cls, run: dict, *, id_var: str, id_val: str) -> bool:
        return not run["values"][id_var] == id_val

    @staticmethod
    def _valid_decimals(cls, run: dict) -> bool:
        return True

    def main(self, ignore: list = [], loop: bool = False) -> None:
        """
            Main function.

            Checks for the validity of any new submission not in the given ignore list and rejects them if necessary.
        """

        cache       : list = []
        faulty_runs : list = []
        # loop over all games
        for game in self.GAMES:
            try:
                new_runs : dict = json.loads(
                    request.urlopen("https://www.speedrun.com/api/v1/runs?game={}&status=new".format(game["id"])).read()["data"]
                )
                print(json.dumps(new_runs, indent=4))
                # loop over all new runs of a given game
                for this_run in new_runs:
                    # cache run for next iteration and skip if it was cached last iteration
                    cache.append(this_run["id"])
                    if this_run["id"] in ignore:
                        continue
                    # validity checks
                    invalid_run : dict = {
                        "id"     : this_run["id"],
                        "faults" : []
                    }
                    if not CelesteLeaderboardBot._valid_real_time(this_run):
                        invalid_run["faults"].append(SubmissionErrors.ERROR_SUBMITTED_RTA)
                    if not CelesteLeaderboardBot._valid_version(this_run, **game["version"]):
                        invalid_run["faults"].append(SubmissionErrors.ERROR_INVALID_VERSION)
                    if not CelesteLeaderboardBot._valid_decimals(this_run):
                        invalid_run["faults"].append(SubmissionErrors.ERROR_INVALID_IGT)
                    # push to list of faulty runs if an error was found
                    if not invalid_run["faults"]:
                        faulty_runs.append(invalid_run)
                # loop over all invalid runs
                for this_run in faulty_runs:
                    print("invalid: ", this_run)
                    pass  # TODO reject them
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
