import varna
from sangya import *
from dump import *

def itsangya(updesh):
    vicched = varna.varnaVicched(updesh)
    org = vicched
    if vicched[-1] == ayogvaha[6] and vicched[-2] in sarvaSvara: # 'उपदेशेऽज् अनुनासिक इत्' (१/३/२/)
        vicched = vicched[:-2]
    if vicched[-1] == "स्" or vicched[-1] == "म्": # "न विभक्तौ तुस्माः" (1/3/4)
        check1 = True
    else:
        check1 = False
    if vicched[-1] in hal_niswar and check1 is False: #"हलन्त्यम्" (1/3/3) and "न विभक्तौ तुस्माः" (1/3/4)
        vicched = vicched[:-1]
    if vicched[0] == "ञ्" and vicched[1] == "इ": #आदिर्ञिटुडवः (1/3/5)
        vicched = vicched[2:]
    if vicched[0] == "ट्" and vicched[1] == "उ": #आदिर्ञिटुडवः (1/3/5)
        vicched = vicched[2:]
    if vicched[0] == "ड्" and vicched[1] == "उ": #आदिर्ञिटुडवः (1/3/5)
        vicched = vicched[2:]
    if vicched[0] == "ष्": #षः प्रत्ययस्य (1/3/6)
        vicched = vicched[1:]
    if vicched[0] in chavarga or vicched[0] in taavarga: #चुटू )1/3/7
        vicched = vicched[1:]
    if vicched[0] == "ल्" or vicched[0] == "श्": # लशक्वतद्धिते (1/3/8)
        check2 = True
    else:
        check2 = False
    if vicched[0] in kavarga or check2 is True:  # लशक्वतद्धिते (1/3/8)
        vicched = vicched[1:]
     # After application of above sutras all that is itsangyaks are removed by तस्य लोपः .
    shabd = varna.varnaSamdhi(vicched)
    return shabd

def savarnSangya(a, b):
    y = VarnaAbhyantarPryatna.get(a)
    z = VarnaAbhyantarPryatna.get(b)
    if y == z:
        return True
    else:
        return False

def samyogSangya(a):
    z = varna.varnaVicched(a)
    i = 0
    listi = []
    listii = []
    while i < len(z):
        if i < len(z) and z[i] in hal_niswar and z[i+1] in hal_niswar:
            listii.append(z[i])
            if z[i+2] in sarvaSvara:
                listii.append(z[i+1])
                listi.append(listii.copy())
                del listii[:]
            i+=1
        else:
            i += 1
    if len(listi) > 0:
        listi.insert(0, True)
    return listi

def updhaSangya(word):
    z = varna.varnaVicched(word)
    for i in range(-len(z), 0):
        if z[i] in sarvaSvara:
            updha = i
    return updha
