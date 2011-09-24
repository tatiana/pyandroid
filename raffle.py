# -*- coding: utf-8 -*-
import android
import random

class Raffler(object):

    def __init__(self, min, max):
        self.min = min
        self.max = max

    def raffle(self):
        return random.randint(self.min, self.max)

def notify_raffled_number(droid, number):
    droid.dialogCreateAlert("Sorteio", "O número sorteado foi: %d!" % number)
    droid.dialogSetPositiveButtonText("Ok")
    droid.dialogShow()

if __name__ == '__main__':
    droid = android.Android()
    droid.webViewShow('file:///sdcard/sl4a/scripts/html/home.html')
    while True:
        result = droid.eventWaitFor('raffle').result
        maximum = int(result['data'])
        number = Raffler(1, maximum).raffle()
        notify_raffled_number(droid, number)
