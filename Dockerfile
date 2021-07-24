FROM python:3
ADD __main__.py /
ADD celeste_bot.py /
ADD data_models.py /
ADD src_constants.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "-u", "./__main__.py", "--credentials", "./data/credentials.json", "--timer", "180"]