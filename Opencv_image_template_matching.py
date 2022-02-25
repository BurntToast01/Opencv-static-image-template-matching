import time
import pyautogui
import cv2 as cv
import numpy as np
from PIL import ImageGrab
pyautogui.FAILSAFE = None

main_templates = ["/home/something/PycharmProjects/REDLIGHT automation/Windows login/gmail print button.png",
                  "/home/something/PycharmProjects/REDLIGHT automation/Windows login/gmail print save button.png",
                  ]

class automated_without_coordinates:
    def __init__(self, x):
        self.templates = x
        self.find_vmButton ()

    def find_vmButton(self):
        start = time.time ()
        self.counter1 = 0
        for i in self.templates:
            # for ImageGrab.grab (bbox=(x, y, x + w, y + h) you can set x and y as 0, then set w and h to the
            # resolution of the screen. you can also call a pyautogui.locate to find the (x,y,w,h) in a while is
            # None loop and pass that tuple to bbox. the while is None loop is great for find images that might
            # move somtimes or when you didn't pass a (x,y,x+h,y+h) location in the first place. capturing the
            # whole screen can lead to errors unless you call cv2.waitkey() before clicking or performing and
            # action. This current while True loop is working well. I would say it take roughly about 0.6 of a sec
            # to find an image.
            # The current loop for this opencv template is no coordinates version
            print("counter is: " ,self.counter1)
            template = cv.imread (i)
            template_gray = np.array (cv.cvtColor (template, cv.COLOR_RGB2GRAY))
            # cv.imshow("gray",template_gray)
            # cv.waitKey()
            h, w, = template_gray.shape
            
            while True:
                a = np.array (ImageGrab.grab (bbox=(0, 0, h+ 2560, w + 1440)))
                b = cv.cvtColor (a, cv.COLOR_RGB2GRAY)
                # the line of code is to make sure we can see a live image from the screen
                # cv.imshow ('a', b)
                # cv.waitKey()
                result = cv.matchTemplate (
                    image=b,
                    templ=template_gray,
                    method=cv.TM_CCOEFF_NORMED, )
                # print("finished matching")
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc (result)
                # print(max_val)
                if self.counter1 >= len (self.templates):
                    break
                if max_val >= 0.9:
                    pyautogui.click (
                        x=max_loc[0],
                        y=max_loc[1]
                    )
                    self.counter1 += 1
                    end = time.time ()
                    find_time = end - start
                    print ("full loop took: ", find_time)
                    print ("find_vmButton was successful")
                    break


b= automated_without_coordinates(main_templates)
