FROM python:3
ADD __main__.py /
ADD celeste_bot.py /
CMD [ "python", "./__main__.py", "/data/config.json" ]