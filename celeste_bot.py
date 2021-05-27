"""
celeste_bot.py
"""

import json
from threading      import Timer
from urllib.request import Request, urlopen
from urllib.error   import HTTPError
from enum           import IntEnum
from typing         import Callable

__version__ = "1.0"


class SubmissionErrors(IntEnum):
    ERROR_SUBMITTED_RTA   = 0
    ERROR_NO_VERSION      = 1
    ERROR_INVALID_IGT     = 2
    ERROR_INVALID_VERSION = 3
    ERROR_BAD_VOD         = 4


class CelesteLeaderboardBot:
    """Class for leaderboard bot, interacting with speedrun.com API"""

    AGENT       : str = f'celeste-leaderboard-bot{__version__}'
    BASE_REASON : Callable = lambda x : f'The Celeste Leaderboard Bot found the following problem{x} with your submission, please edit it accordingly: '
    REASON_TEXT : dict = {
        0 : "Your submission has real-time, leave the real-time column empty",
        1 : "You did not select a version, make sure to select the correct game version",
        2 : "Your submission has an invalid IGT, check the final time of your run and adjust the submission",
        3 : "The version you selected does not exist on your platform, please select the correct one",
        4 : "The video you submitted is a Twitch past broadcast, which will be automatically deleted after a while, please highlight your run"
    }

    def __init__(self, *, keys: dict, timer: float, games: list) -> None:
        self.SRC_KEY    : str   = keys["src"]
        self.TWITCH_KEY : str   = keys["twitch"]
        self.GAMES      : float = games
        self.TIMER      : list  = timer

    @classmethod
    def _valid_real_time(cls, run : dict) -> bool:
        """Checks if any RTA is submitted, returns False if so"""
        return run["times"]["realtime_t"] == 0

    @classmethod
    def _valid_default_version(cls, run: dict, *, id_var: str, id_val: str) -> bool:
        """Checks if the default version is submitted, returns False if so"""
        return not(run["values"][id_var] == id_val)

    @classmethod
    def _valid_in_game_time(cls, run: dict) -> bool:
        """Checks if the submitted IGT is invalid, returns False if so"""
        return (int(1000 * run["times"]["ingame_t"]) % 17) == 0

    @classmethod
    def _valid_existing_version(cls, run: dict) -> bool:
        """Checks if the submitted version is available on the submitted platform, returns False if it isn't"""
        return True  # TODO

    @classmethod
    def _valid_permanent_vod(cls, run: dict) -> bool:
        """Checks if submitted VOD is a past broadcast, returns False if so"""
        return True  # TODO

    def main(self, ignore: list = [], loop: bool = False) -> None:
        """
            Main function.

            Checks for the validity of any new submission not in the given ignore list and rejects them if necessary.
        """
        cache : list = []
        # loop over all games
        for game in self.GAMES:
            faulty_runs : list = []
            try:
                get_req : Request = Request(f'https://www.speedrun.com/api/v1/runs?game={game["id"]}&status=new')
                get_req.add_header('User-Agent', CelesteLeaderboardBot.AGENT)
                new_runs : dict = json.loads(urlopen(get_req).read())["data"]
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
                    # RTA check
                    if not CelesteLeaderboardBot._valid_real_time(this_run):
                        invalid_run["faults"].append(SubmissionErrors.ERROR_SUBMITTED_RTA)
                    # default version check
                    if not CelesteLeaderboardBot._valid_default_version(this_run, **game["version"]):  # TODO call needs to be adjusted
                        invalid_run["faults"].append(SubmissionErrors.ERROR_NO_VERSION)
                    # IGT check
                    if not CelesteLeaderboardBot._valid_in_game_time(this_run):
                        invalid_run["faults"].append(SubmissionErrors.ERROR_INVALID_IGT)
                    # existing version check
                    if not CelesteLeaderboardBot._valid_existing_version(this_run):
                        invalid_run["faults"].append(SubmissionErrors.ERROR_INVALID_IGT)
                    # past broadcast check
                    if not CelesteLeaderboardBot._valid_in_game_time(this_run):
                        invalid_run["faults"].append(SubmissionErrors.ERROR_INVALID_IGT)
                    # push to list of faulty runs if an error was found
                    if len(invalid_run["faults"]) > 0:
                        faulty_runs.append(invalid_run)
                # loop over all invalid runs
                for this_run in faulty_runs:
                    x : str = 's' if len(this_run["faults"]) > 1 else ''
                    dyn_reason : str = ' || '.join(
                        [CelesteLeaderboardBot.REASON_TEXT[fault] for fault in this_run["faults"]]
                    )
                    put_req : Request = Request(
                        f'https://www.speedrun.com/api/v1/runs/{this_run["id"]}/status',
                        headers = {
                            'User-Agent'    : CelesteLeaderboardBot.AGENT,
                            'Content-Type'  : 'application/json',
                            'X-API-Key'     : self.SRC_KEY,
                        },
                        data = bytes(json.dumps({
                            "status": {
                                "status": "rejected",
                                "reason": CelesteLeaderboardBot.BASE_REASON(x) + dyn_reason
                            }
                        }), encoding="utf-8"),
                        method = "PUT"
                    )
                    urlopen(put_req)
                    print(f'Rejected run <{this_run["id"]}> for reasons {this_run["faults"]}')
            # invalid URI or no authorization
            except HTTPError as error:
                print(f'There was an HTTP error: {error}')
                cache  = []
                break
            # connection error
            except (ConnectionResetError, ConnectionRefusedError, ConnectionAbortedError, ConnectionError) as error:
                print(f'There was a connection error: {error}')
                cache = []
                break
        # loop again if running from start()
        if loop: Timer(self.TIMER, self.main, [cache, loop]).start()

    def start(self) -> None:
        """Start bot, blocking calling thread"""
        self.main([], True)
