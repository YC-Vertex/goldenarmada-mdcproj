def InputClothes(param, suit_cursor, max_cno):
    CNO = max_cno + 1
    CTEX = param['CTEX']
    CTYP = param['CTYP']
    CCOLOR = param['CCOLOR']
    CIMG = param['CIMG']
    
    command = 'INSERT INTO CLOTHES(CNO, CTEX, CTYP, CCOLOR, CIMG) VALUES(' + CNO  + ', ' + CTEX + ', ' + CTYP + ', ' + CCOLOR + ', \'' + CIMG + '\');'
    suit_cursor.execute(command)
    return 