import json
if __name__ == '__main__':
    import fb_subcontroller

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
    emotion = fb_subcontroller.queryOutHandler(json_request)
    update = emotion # 对emotion进行一通操作
    return update