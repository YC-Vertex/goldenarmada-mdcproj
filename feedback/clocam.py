# 上乘feedback，下接三个init函数

import sys
sys.path.append('../') # 不然没法import上层目录里的feedback.py
from myFeedback import feedback
import json
import cv2
import numpy as np
from init_pkg import init_pattern
from init_pkg import init_cata
from init_pkg import init_color
from picamera import PiCamera
from time import sleep

def shot_and_get():
    """
    :lib: feedback
    :func: shot_and_get
    :param: 
    :return: tag (1+1+1)

    Capture a img of clothes when called, and return the tag of it.
    """
    request = [{
        'lib': 'intel',
        'func': 'to_shot_clothes',
        'param': ''
    }]
    json_request = json.dumps(request)
    shot_order = feedback.queryOutHandler(json_request)
    if shot_order==True:
        camera=PiCamera()
        camera.start_preview()
        sleep(5)
        camera.capture('path/img.jpg')
        camera.stop_preview()
        img=cv2.imread('path/picture.jpg',1)
        tag=get_tag(img)
        return tag
    else:
        return [-1,-1,-1]

def get_tag(img):
    """
    :lib: feedback
    :func: get_tag
    :param: img
    :return: tag (1+1+1)

    Get the tag of the clothes and return. 
    """
    img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    pattern_tag=init_pattern.pattern(img)
    cata_tag=init_cata.cata(img_grey)
    color_tag=init_color.color(img)
    tag=[pattern_tag]+[cata_tag]+[color_tag]
    return tag