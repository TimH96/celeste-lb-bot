FROM python:3
# RUN pip install the twtich thingy
ADD __main__.py /
ADD celeste_bot.py /
CMD [ "python", "./__main__.py", "/data/config.json" ]