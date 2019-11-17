import json
import requests
from error import AIError

GET_EMOTION_URL = 'https://api-cn.faceplusplus.com/facepp/v3/detect'

def GetEmo(detect_param, API_KEY, API_SECRET):
    detect_url = detect_param['url']
    detect_data = {'api_key': API_KEY, 'api_secret': API_SECRET, 'image_url': detect_url, 'return_attributes': 'emotion'}
    # Error Process
    try:
        response = requests.post(GET_EMOTION_URL, data = detect_data)
        req_con = response.content.decode('utf-8')
        req_dict = json.JSONDecoder().decode(req_con)
    except requests.exceptions.Timeout:
        raise AIError('TLError', 'Time Limit Exceeded!')
    if('error_message' in req_dict):
        raise AIError('APIError', req_dict['error_message'])

    emotion = {}
    emotion['anger'] = req_dict['faces'][0]['attributes']['emotion']['anger']
    emotion['fear'] = req_dict['faces'][0]['attributes']['emotion']['fear']
    emotion['happiness'] = req_dict['faces'][0]['attributes']['emotion']['happiness']
    emotion['sadness'] = req_dict['faces'][0]['attributes']['emotion']['sadness']
    emotion['neutral'] = req_dict['faces'][0]['attributes']['emotion']['neutral']
    emotion['disgust'] = req_dict['faces'][0]['attributes']['emotion']['disgust']
    emotion['surprise'] = req_dict['faces'][0]['attributes']['emotion']['surprise']
    return emotion