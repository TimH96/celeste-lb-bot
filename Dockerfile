FROM arm64v8/python:3
RUN pip install python-twitch-client
ADD __main__.py /
ADD celeste_bot.py /
CMD [ "python", "./__main__.py", "/data/config.json" ]