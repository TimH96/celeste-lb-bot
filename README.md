# Celeste Leaderboard Bot

This is a bot to check for basic speedrun submission errors for the [Celeste leaderboards](https://www.speedrun.com/celeste) using the [speedrun.com REST API](https://github.com/speedruncomorg/api) and Python. This project can easily be forked for similiar leaderboard bots. Just adjust/replace the ``CelesteLeaderboardBot`` class and its ``main`` method.

### Setup

Pull the directory:
```bash
$ git pull <eventuallink>
$ python celeste-leaderboard-bot /path/to/config.json
```

Or get the Docker image from the releases (or build it yourself) and run that, mounting ``/data`` to the folder on your host OS with the ``config.json``:
```bash
$ docker run --name clbb -v D:\path\to\folder\with\config:/data celesteleaderboardbot:latest
```

The bot is configured via a ``config.json``. This can be linked to via the first command line parameter upon execution, or alternatively is looked for in the directory from which it is executed.

The file should look like this:

```json
{
    "keys"  : {
        "src"    : "YOUR_API_KEY",              # your speedrun.com API key
        "twitch" : {
            "client" : "YOUR_TWITCH_CLIENT",    # your twitch client id
            "secret" : "YOUR_TWITCH_SECRET"     # your twitch client secret
        }
    },
    "timer" : 30,                               # polling interval in seconds
    "games" : [
        {
            "id"      : "o1y9j9v6",             # unique game ID, found and used via the API
            "name"    : "Celeste",              # unused/optional
            "version" : {                       # Celeste-specific, catching faults on 'Game Version' variable
                "variable_id" : "38do9y4l",     # ID of version variable for that game
                "default_ver" : "5q8e7y3q",     # ID of default value for that game
                "invalid_ver" : {               # array of invalid version hashed for each platform
                    "nzelkr6q" : ["810gdx5l", "zqoo4vxq"],
                    "o7e2mx6w" : ["810gdx5l", "zqoo4vxq", "21dg78p1"],
                    "8gej2n93" : [],
                }
            }
        }
    ]
}
```

### Dependencies
twitch thingy
