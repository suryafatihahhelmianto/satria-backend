import statistics as stat

def pAmtong(x): #FUNGSI INI DIGUNAKAN UNTUK DATA E2a dan E2b
    min_val = 0
    max_val = 3
    
    if x < min_val:
        x = min_val
    elif x > max_val:
        x = max_val
    
    normalized_value = (x - min_val) / (max_val - min_val)
    result = 1 - normalized_value
    return round(result,3)

def pTetes(x): #FUNGSI INI DIGUNAKAN UNTUK NORMALISASI E2c
    min_val = 0
    max_val = 30
    
    if x < min_val:
        x = min_val
    elif x > max_val:
        x = max_val
    
    normalized_value = (x - min_val) / (max_val - min_val)
    result = 1 - normalized_value
    return round(result,3)

def pHilangren(a,b,c,d): #FUNGSI INI DIGUNAKAN UNTUK E2d
    x = stat.mean([(a-b),(b-c),(c-d)])
    min_val = 0
    max_val = 1
    
    if x < min_val:
        x = min_val
    elif x > max_val:
        x = max_val
    
    normalized_value = (x - min_val) / (max_val - min_val)
    result = 1 - normalized_value
    return round(result,3)

def pDisAdil(a,b) : #FUNGSI INI DIGUNAKAN UNTUK E3
    x = (a-b)/a *100
    min_val = 15
    max_val = 30
    
    if x < min_val:
        x = min_val
    elif x > max_val:
        x = max_val
    
    normalized_value = (x - min_val) / (max_val - min_val)
    result = 1 - normalized_value
    return round(result,3)