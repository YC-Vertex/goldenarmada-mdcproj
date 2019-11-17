import json
import requests
from error import AIError

SEARCH_FACE_URL = 'https://api-cn.faceplusplus.com/facepp/v3/search'

def SearchFace(search_param, API_KEY, API_SECRET, OUTER_ID):
    image_url = search_param['image_url']
    search_data = {'api_key': API_KEY, 'api_secret': API_SECRET, 'image_url': image_url, 'outer_id': OUTER_ID}
    # Error Process
    try:
        response = requests.post(SEARCH_FACE_URL, data = search_data)
        req_con = response.content.decode('utf-8')
        req_dict = json.JSONDecoder().decode(req_con)
    except requests.exceptions.Timeout:
        raise AIError('TLError', 'Time Limit Exceeded!')
    if('error_message' in req_dict):
        raise AIError('APIError', req_dict['error_message'])

    print(req_dict)
    if(float(req_dict['results'][0]['confidence']) > float(req_dict['thresholds']['1e-5'])):
        return True
    return False

def Login(login_param, API_KEY, API_SECRET, OUTER_ID):
    if(SearchFace(login_param, API_KEY, API_SECRET, OUTER_ID)):
        return True
    return False