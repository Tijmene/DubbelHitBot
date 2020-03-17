from flask import Flask
from DubbelHitBot import DubbelHitBot
import datetime
from playsound import playsound
import time


bot = DubbelHitBot()
app = Flask(__name__)


@app.route("/")
def home():
    return "The server is running"


@app.route("/DubbelHit")
def click_button():
    current_time = datetime.datetime.now()
    if 17 > current_time.hour > 8:
        bot.send_email()
        playsound("alarm.mp3")
        bot.mouse_click()

        f = open("log.txt", "a+")
        f.write("Clicked the button at {}. \n".format(current_time))
        f.close()
        time.sleep(50)

        bot.reset()

    return "Clicked the button at {}.".format(current_time)


if __name__ == "__main__":
    app.run()
