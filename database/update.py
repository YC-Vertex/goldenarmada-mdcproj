def UpdatePref(param, suit_cursor):
    cno = param['CNO']
    command = 'SELECT PREFERENCE FROM UC WHERE CNO='+cno
    suit_cursor.execute(command)
    pref = suit_cursor.fetchone()[0]
    happiness = int(param['emotion']['happiness'])
    sadness = int(param['emotion']['sadness'])
    pref += happiness*100-sadness*100

    command = 'UPDATE UC SET PREFERENCE='+str(pref)+' WHERE CNO='+str(cno)
    suit_cursor.execute(command)
    return