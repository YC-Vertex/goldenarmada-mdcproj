# 上乘controller，下接preference和clocam
import controller
from feedback import clocam
from feedback import preference
import json

def queryInHandler(json):
    if json['func'] == 'pre_update':
        result = preference.pre_update(json['param'])
        return result
    elif json['func'] == 'shot_and_get':
        result = clocam.shot_and_get(json['param'])
        return result

def queryOutHandler(json):
    if json['lib'] == 'feedback':
        return queryInHandler(json)
    else:
        return controller.queryInHandler(json)