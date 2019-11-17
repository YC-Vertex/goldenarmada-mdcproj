import json
import pymysql
import fetch
import input
import update
if __name__ == '__main__':
    import sys
    sys.path.append('../')
    from goldenarmada_mdcproj import controller
host = 'localhost'
username = 'root'
password = 'O13579oO'
database = 'test'

def QueryInHandler(request):
    # Connect Local Database
    sudb = pymysql.connect(host, username, password, database)
    sucur = sudb.cursor()
    max_cno = 0
    # Get Request and Decode into Dict
    request = json.loads(request)
    # Decode and Extract Request Info
    func = request['func']
    param = request['param']

    if func == 'InputClothes':
        if(not max_cno):
            sucur.execute('SELECT MAX(CNO) FROM CLOTHES')
            max_cno = sucur.fetchone()[0]
        input.InputClothes(param, sucur,max_cno)
        sudb.commit()
        max_cno += 1
    elif func == 'FetchClothes':
        fetch.FetchClothes(param, sucur)
    elif func == 'UpdatePref':
        update.UpdatePref(param, sucur)
        sudb.commit()
    return 0

