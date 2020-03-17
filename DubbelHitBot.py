from pynput.mouse import Button, Controller
from random import random
import math
import time
import smtplib
import os

EMAIL_ADRESS = os.environ.get("GmailAdress")
EMAIL_PASSWORD = os.environ.get("PythonEmailApp")
EMAIL_RECEIVER = os.environ.get("DubbelHitEmail")


class DubbelHitBot:
    mouse = Controller()
    radius = 20
    x_centre = None
    y_centre = None
    x_close = None
    y_close = None
    x_close_war = None
    y_close_war = None
    x_close_confirm = None
    y_close_confirm = None

    def __init__(self):
        self.calibrate_mouse()

    def mouse_click(self):
        angle = random() * 3.14 * 2

        radius = self.radius * random()

        xpos = math.cos(angle) * radius
        ypos = math.sin(angle) * radius

        xpos += self.x_centre
        ypos += self.y_centre

        self.mouse.position = (xpos, ypos)
        self.mouse.click(Button.left, 1)

        time.sleep(20 + 10*random())

        angle = random() * 3.14 * 2

        radius = self.radius * 0.7 * random()

        xpos = math.cos(angle) * radius
        ypos = math.sin(angle) * radius

        xpos += self.x_centre
        ypos += self.y_centre + 430

        self.mouse.position = (xpos, ypos)
        self.mouse.click(Button.left, 1)

    def reset(self):
        self.mouse.position = (self.x_close, self.y_close)
        self.mouse.click(Button.left, 1)
        time.sleep(3)
        self.mouse.position = (self.x_close_confirm, self.y_close_confirm)
        self.mouse.click(Button.left, 1)
        time.sleep(100)
        # Open the sky app from static location on desktop
        self.mouse.position = (276, 411)
        self.mouse.click(Button.left, 2)
        time.sleep(100)
        self.mouse.position = (self.x_close_war, self.y_close_war)
        self.mouse.click(Button.left, 1)

    def calibrate_mouse(self):
        input("Position the cursor over the close button and press enter...")
        self.x_close, self.y_close = self.mouse.position
        print("Close button is at: ({},{})".format(self.x_close, self.y_close))

        self.x_centre = self.x_close - 219
        self.y_centre = self.y_close + 265

        self.x_close_war = self.x_close - 175
        self.y_close_war = self.y_close + 523

        self.x_close_confirm = self.x_close - 123
        self.y_close_confirm = self.y_close + 455

    def send_email(self):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)

            subject = "DRUK OP DE KNOP"
            body = "Twee keer dezelfde artiest heuj!"

            msg = f'Subject: {subject}\n\n{body}'

            email_adresses = EMAIL_RECEIVER.split(",")
            for email_adress in email_adresses:
                smtp.sendmail(EMAIL_ADRESS, email_adress.strip(), msg)

if __name__ == "__main__":
    # mouse = Controller()
    #
    # while True:
    #     print(mouse.position)

    bot = DubbelHitBot()
    bot.send_email()
    # time.sleep(10)
    # bot.reset()



