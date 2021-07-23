# Celeste Leaderboard Bot

This is a bot to check for basic speedrun submission errors for the [Celeste leaderboards](https://www.speedrun.com/celeste) using the [speedrun.com REST API](https://github.com/speedruncomorg/api), as well as the [Twitch API](https://dev.twitch.tv/docs/api/), and Python. This project can easily be forked for similiar leaderboard bots. Just adjust/replace the ``CelesteLeaderboardBot`` class and its ``main`` method.

### Setup

#### Install

Pull the directory and install its dependencies:
```bash
$ git pull https://github.com/TimH96/celeste-lb-bot
$ cd celeste-lb-bot
$ pip install -r requirements.txt
$ python celeste-leaderboard-bot --credentials /path/to/credentials.json --timer 60
```

Or build the Docker image and run that, mounting ``/data`` to the folder on your host OS with the ``credentials.json`` file:
```bash
$ docker run --detach --name clbb --restart=always -v D:\path\to\folder\with\creds:/data clbb:latest
```

#### Configure

The bot is configured via a ``credentials.json``, which can be linked to via the ``--credentials`` flag, or alternatively is looked for in the directory from which the bot is executed.
The file should look like this:

```javascript
{
    "src": {
        "session" : "SRC_PHPSESH_COOKIE",    
        "csrf"    : "SRC_CSRF_TOKEN"
    },
    "twitch" : {
        "client"  : "TWITCH_CLIENT_ID",
        "secret"  : "TWITCH_CLIENT_SECRET"
    }
}
```
##### Twitch credentials

You can find your Twitch client ID and secret by registering your app [here](https://dev.twitch.tv/console/apps/create).

##### SRC credentials

The CSRF token and session ID for speedrun.com are easily found by inspecting a GET request on their main page while logged in, the CSRF token is found in the response HTML in the header and the session ID is part of your request body. I considered automating the retrieval of these credentials, but ultimately decided it wasn't worth the effort since speedrun.com forces email 2FA, so one would have to scrape and parse emails to effectively automate this step. Luckily, speedrun.com sessions last indefinitely in theory, and in practice are only cleared every half year or so for all users globally.

For future reference however, the session ID can be programmatically claimed by requesting a login, and the CSRF token by simply parsing a GET request from there.
