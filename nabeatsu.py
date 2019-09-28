import random

basic_number = {"1": 'いち', "2":'に', "3":'さん', "4":'よん', "5":'ご', "6":'ろく', "7":'なな', "8":'はち', "9":'きゅう', "0":'ぜろ'}
jyu = "じゅう"
hyaku = "ひゃく"



def numchange(x):
    if x < 10:
        y = basic_number[str(x)]
        return y
    elif x < 100:
        lbox = [int(z) for z in list(str(x))]
        y1 = basic_number[str(lbox[0])]
        if y1 == "いち":
            y1 = jyu
        else: 
            y1 = y1 + jyu
        y2 = basic_number[str(lbox[1])]
        if y2 == "ぜろ":
            y2 = ""
        y3 = y1 + y2
        return y3
    elif x < 1000:
        lbox = [int(z) for z in list(str(x))]
        w1 = basic_number[str(lbox[0])]
        if w1 == "いち":
            w1 = hyaku
        else: 
            w1 = w1 + hyaku
        w2 = basic_number[str(lbox[1])]
        if w2 == "いち" or w2 == "ぜろ":
            w2 = jyu
        else: 
            w2 = w2 + jyu
        w3 = basic_number[str(lbox[2])]
        if w3 == "ぜろ":
            w3 = ""
        w4 = w1 + w2 + w3
        return w4
        
    
    
for number_ in range(1,1000):
    if number_ % 3 == 0:
        t = numchange(number_)
        print(t)
    elif "3" in str(number_):
        t = numchange(number_)
        print(t)
    else:
        print(str(number_))

