def FetchClothes(param, suit_cursor):
    CTYP = '(0, 1, 2)'
    CTEX = '(0, 1, 2)'
    CCOLOR = '(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)'
    if(param['CTYP'] != '-1'):
        CTYP = '(' + param['CTYP'] +')'
    if(param['CCOLOR'] != '-1'):
        CCOLOR = '(' + param['CCOLOR'] +')'

    command = 'SELECT CIMG, CNO FROM CLOTHES WHERE CTYP IN ' + CTYP + ' AND CTEX IN ' + CTEX + ' AND CCOLOR IN ' + CCOLOR
    suit_cursor.execute(command)

    print(suit_cursor.fetchall())
    return