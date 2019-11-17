# 上乘feedback，下接三个init函数
import sys
sys.path.append('../') # 不然没法import上层目录里的feedback.py
from goldenarmada-mdcproj import feedback
import json
import cv2
import numpy as np
from init_pkg import init_pattern
from init_pkg import init_cata
from init_pkg import init_color
from picamera import PiCamera
from time import sleep

def shot_and_get(json):
    """
    :lib: feedback
    :func: shot_and_get
    :param: ctr: the time this func has been called
    :return: none
    """
    ctr = jason['param']
    # 设置图片存储路径
    path_suffix = '.jpg'
    path_prefix = '/path/my_img'
    img_path = path_prefix + str(ctr) + path_suffix
    # 拍摄图片
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    camera.capture(img_path)
    camera.stop_preview()
    # 存储图片和标签
    pattern_tag = init_pattern.pattern(img_path)
    cata_tag = init_cata.cata(img_path)
    color_tag = init_color.color(img_path)
    request = [{
        'lib': 'DB',
        'func': 'InputClothes',
        'param': {'category':cata_tag,\
            'color':color_tag,\
            'pattern':pattern_tag,\
            'path':img_path}
    }]
    json_request = json.dumps(request)
    retval = feedback.queryOutHandler(json_request)
    return retval