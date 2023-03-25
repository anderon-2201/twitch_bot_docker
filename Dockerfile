FROM debian:latest

COPY twitch_bot.service /etc/systemd/system/
COPY src/ /bot/

RUN apt update && apt upgrade -y
RUN apt install python3 pip neovim systemd -y

RUN pip install -r /bot/requirements.txt

RUN systemctl enable twitch_bot.service

WORKDIR /bot/

CMD [ "python3", "/bot/bot.py" ]
