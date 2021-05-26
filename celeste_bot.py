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

    @classmethod
    def _valid_real_time(cls, run : dict) -> bool:
        """Checks if any RTA is submitted, returns False if so"""
        return run["times"]["realtime_t"] == 0

    @classmethod
    def _valid_version(cls, run: dict, *, id_var: str, id_val: str) -> bool:
        """Checks if the default version is submitted, returns False if so"""
        return not(run["values"][id_var] == id_val)

    @classmethod
    def _valid_in_game_time(cls, run: dict) -> bool:
        """Checks if the submitted IGT is invalid, returns False if so"""
        return (int(1000 * run["times"]["ingame_t"]) % 17) == 0

    def main(self, ignore: list = [], loop: bool = False) -> None:
        """
            Main function.

            Checks for the validity of any new submission not in the given ignore list and rejects them if necessary.
        """
        cache       : list = []
        faulty_runs : list = []
        # loop over all games
        for game in self.GAMES:
            #try:
                new_runs : dict = json.loads(
                    request.urlopen("https://www.speedrun.com/api/v1/runs?game={}&status=new".format(game["id"])).read()
                )["data"]
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
                    if not CelesteLeaderboardBot._valid_in_game_time(this_run):
                        invalid_run["faults"].append(SubmissionErrors.ERROR_INVALID_IGT)
                    # push to list of faulty runs if an error was found
                    if len(invalid_run["faults"]) > 0:
                        faulty_runs.append(invalid_run)
                # loop over all invalid runs
                for this_run in faulty_runs:
                    print("invalid: ", this_run)
                    pass  # TODO reject them
            #except Exception as error: raise error  # TODO !!! error handling on: HTTP404 or OS Conn Refused, prolly just continue
        # loop again if running from start()
        if loop:
                Timer(self.TIMER, self.main, [cache, loop]).start()

    def start(self) -> None:
        """Start bot, blocking calling thread"""
        self.main([], True)
