"""
celeste_bot.py
"""

from threading import Timer


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
        # TODO main logic
        

        # queue again on timer if looping
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
            "o1y9j9v6"
        ]
    }

    CelesteLeaderboardBot(**config).main()
