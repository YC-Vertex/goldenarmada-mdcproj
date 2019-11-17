import json
import requests
from error import AIError

SEARCH_FACE_URL = 'https://api-cn.faceplusplus.com/facepp/v3/search'
ADD_USER_TOKEN_URL = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'

def RegisFace(regis_param, API_KEY, API_SECRET, OUTER_ID):
    regis_url = regis_param['image_url']
    # See if This User Exists
    detect_data = {'api_key': API_KEY, 'api_secret': API_SECRET, 'image_url': regis_url, 'outer_id': 'Smart_Home_Userset'}
    try:
        response = requests.post(SEARCH_FACE_URL, data = detect_data)
        req_con = response.content.decode('utf-8')
        req_dict = json.JSONDecoder().decode(req_con)
    except requests.exceptions.Timeout:
        raise AIError('TLError', 'Time Limit Exceeded!')
    if('error_message' in req_dict):
        raise AIError('APIError', req_dict['error_message'])

    if(req_dict['results'][0]['confidence'] > req_dict['thresholds']['1e-5']):
        regis_token = req_dict['faces'][0]['face_token'] # Only One Face Should Exist!!
        raise AIError('FunError', 'User Already Registered!')
    
    # Regis FaceToken
    regis_data = {'api_key': API_KEY, 'api_secret': API_SECRET, 'outer_id': OUTER_ID, 'face_tokens': regis_token}
    # Error Process
    try:
        response = requests.post(ADD_USER_TOKEN_URL, data = regis_data)
        req_con = response.content.decode('utf-8')
        req_dict = json.JSONDecoder().decode(req_con)
    except requests.exceptions.Timeout:
        raise AIError('TLError', 'Time Limit Exceeded!')
    if('error_message' in req_dict):
        raise AIError('APIError', req_dict['error_message'])