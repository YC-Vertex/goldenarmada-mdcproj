import sys
sys.path.append('../') # 不然没法import上层目录里的feedback.py
from myFeedback import feedback
import json

def pre_update(json):
    """
    :lib: feedback
    :func: pre_update
    :param: emotion
    :return: tag (1+1+1)

    Capture a img of clothes when called, and return the tag of it.
    """
    request = [{
        'lib': 'intel',
        'func': 'emotion_recog',
        'param': ''
    }]
    json_request = json.dumps(request)
    emotion = feedback.queryOutHandler(json_request)
    update = emotion # 对emotion进行一通操作
    return update