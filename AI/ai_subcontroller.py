import json
import error
from emotion import GetEmo
from register import RegisFace
from search import SearchFace, Login
if __name__ == '__main__':
    import sys
    sys.path.append('../')
    from goldenarmada_mdcproj import controller

API_KEY = 'S13wf3nu7MaFIlbR80quFkSliO6fFmq3'
API_SECRET = 'VoFoVgcxQOu541XuedSHKBBsm7q0mdI2'
OUTER_ID = 'Smart_Home_Userset'

def QueryInHandler(request):
# Get Reponse and Decode into Dict
    request = json.loads(request)
    # Decode and Extract Request Info
    func = request['func']
    param = request['param']
    
    try:
        if(func == 'GetEmo'):
            print(GetEmo(param, API_KEY, API_SECRET))
        elif(func == 'SearchFace'):
            print(SearchFace(param, API_KEY, API_SECRET, OUTER_ID))
        elif(func == 'Login'):
            print(Login(param, API_KEY, API_SECRET, OUTER_ID))
        elif(func == 'RegisFace'):
            print(RegisFace(param, API_KEY, API_SECRET, OUTER_ID))

    except error.AIError as e:
        Error_Message = "An " + e.e_type + " Occurred! \n" + e.e_message
        print(Error_Message)
    return 0