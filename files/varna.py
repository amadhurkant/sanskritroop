#define char encoding
from dump import num_codes_khadi, khadi
from sangya import *
svara_l = ["आ"]+hrasva_svar[1:]+dirgha_svar[1:]
matra = matra_hrasva+matra_dirgha
halant =  "्"
avagrah = "ऽ"
def dustclear(tl, item):
    cleaned = list(filter((item).__ne__, tl))
    return cleaned

def varnaVicched(shabd):
    listver = []
    const_listver = []
    if shabd == "":
        return [""]
    for i in range(0, len(shabd)):
        listver.append(shabd[i])
        const_listver.append(shabd[i])
    for i in range(0, len(listver)-1):
        if listver[i] in hal_sswar:
             t = hal_sswar.index(listver[i])
             listver[i] = hal_niswar[t]
    for i in range(0, len(listver)):
        if listver[i] in hal_niswar and listver[i+1] != halant and listver[i+1] not in matra:
            listver.insert(i+1, "अ")
    for i in range(0, len(listver)):
        if listver[i] in matra:
            t = matra.index(listver[i])
            listver[i] = svara_l[t]
    listver = dustclear(listver, halant)
    if listver[-1] == ayogvaha[0] and listver[-2] in hal_niswar and const_listver[-2] in hal_sswar:
        listver.insert(-1, "अ")
    if listver[-1] in hal_sswar:
        t = hal_sswar.index(listver[-1])
        listver[-1] = hal_niswar[t]
        listver.insert(len(listver), "अ")
    return listver

def varnaSamdhi(varnaList):
    varnaList = dustclear(varnaList, "")
    for i in range(0, len(varnaList)):
        if i != 0 and varnaList[i] in sarvaSvara:
            t = hal_niswar.index(varnaList[i-1]) + 1
            u = sarvaSvara.index(varnaList[i]) + 1
            indexx = str(t)+"."+str(u)
            k = num_codes_khadi.index(indexx)
            varnaList[i-1] = khadi[k]
            varnaList[i] = ""
    varnaList = dustclear(varnaList, "")
    shabd = ""
    for i in range(0, len(varnaList)):
        shabd += varnaList[i]
    return shabd

#print(varnaVicched("मधुरकान्तिः"))
