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
    "key"   : "YOUR_API_KEY",           # your speedrun.com API key
    "timer" : 60,                       # polling interval in seconds
    "games" : [
        {
            "id"      : "o1y9j9v6",     # unique game ID, found and used via the API
            "name"    : "Celeste",      # unused/optional
            "version" : {
                "id_var" : "38do9y4l",  # Celeste specific version variable identifier
                "id_val" : "5q8e7y3q"   # Celeste specific version value identifier
            }
        }
    ]
}
```
