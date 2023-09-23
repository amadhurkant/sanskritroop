import varna
import niyamSangyas as ns
import sandhi as sd
from sangya import *

# Subant pure forms
subant = []
for i in range(0, len(sup)):
    subant.append(ns.itsangya(sup[i]))

#Basic functionalities
def list_constructor(list1, list2):
    if len(list1) == len(list2):
        new_list = []
        loc_list = []
        for i in range(0, len(list2)):
            loc_list.append(list1[i])
            loc_list.append(list2[i])
            new_list.append(loc_list)
            loc_list = []
    else:
        raise Exception("length of both list doesn't match")
    return new_list

shabd = input("शब्द प्रविष्ट करें: ")
print("---------------------------------------------------")
print("लिंगानुशासन  ---- पुरुष: 'P ', स्त्री: 'S' एवं नपुंसक: 'N'" )
print("उदाहरण के लिये यदि पुल्लिङ्ग शब्द के रूप चाहिये हों तो P प्रविष्ट करें। ")
print("---------------------------------------------------")
lingam = input("शब्द का लिंग:")
baselist = [shabd for i in range(0, len(subant))]
# Subant Sangya prakaran
bhaSangyaKarak = [subant[5], subant[6], subant[9], subant[12],
                  subant[15], subant[16], subant[17], subant[18], subant[19]]
sarvanaamstanSangya = subant[0:5]
bhakaaradi = [7, 8, 10, 11, 13, 14]
halaadi = [0, 7, 8, 10, 11, 13, 14, 20]
#halaadi = [subant[0], subant[7], subant[8], subant[11], subant[20]]
# Rules: In this sections rules are being written
        # Halant Rules
def NapunshakLing(table, ling):
    table[2][1] = "ई"
    table[5][1] = "ई"
    table[1][1] = "इ"
    table[4][1] = "इ"
def change(table, ling):
    y = table[0][0]
    var = varna.varnaVicched(y)
    var_c = varna.varnaVicched(y)
    ant = var[-1]
    if ant == "छ्":
        var2 = var.copy()
        var2.insert(-1, "च्")
        new_chh = varna.varnaSamdhi(var2)
        for i in range(0, len(table)):
            if i not in halaadi:
                table[i][0] = new_chh
    for i in halaadi:
        if varna.varnaVicched("राज्") == var[-3:] or varna.varnaVicched("सृज्") == var[-3:] or varna.varnaVicched("मृज्") == var[-3:] or varna.varnaVicched("यज्") == var[-3:] or ant == "छ्":
            var[-1] = "ड्"
            vrat = varna.varnaSamdhi(var)
            table[i][0] = vrat
        elif ant == "च्":
            var[-1] = "क्"
            vrat = varna.varnaSamdhi(var)
            table[i][0] = vrat
        elif ant == "ज्":
            var[-1] = "ग्"
            vrat = varna.varnaSamdhi(var)
            table[i][0] = vrat
        elif ant == "श्": #r31
            var[-1] = "क्"
            vrat = varna.varnaSamdhi(var)
            table[i][0] = vrat
        elif ant == "ह्": #r40
            var[-1] = "घ्"
            new = varna.varnaSamdhi(var)
            for i in halaadi:
                table[i][0] = new
    return table

def halant_halaadi(table, ling):
    y = table[0][0]
    var = varna.varnaVicched(table[0][0])
    var_o = var.copy()#use copy
    print(var_o)
    ant = var[-1]
    table[0][1] = ""
    if ant in prathamaakshar: #r3
        t = prathamaakshar.index(ant)
        var[-1] = tratiyaakshar[t]
        new = varna.varnaSamdhi(var)
        table[0][0] = y+"-"+new
        for i in bhakaaradi: #r4
            table[i][0] = new
    elif ant in tratiyaakshar: #r5, r6
        t = tratiyaakshar.index(ant)
        var[-1] = prathamaakshar[t]
        new = varna.varnaSamdhi(var)
        table[0][0] = y+"-"+new
        table[20][0] = new
    elif ant in chaturthaakshar: #r7, r9
        t = chaturthaakshar.index(ant)
        var[-1] = prathamaakshar[t]
        new1 = varna.varnaSamdhi(var)
        var[-1] = tratiyaakshar[t]
        new2 = varna.varnaSamdhi(var)
        table[0][0] = new1+"-"+new2
        table[20][0] = new1
        for i in bhakaaradi: #r8
            table[i][0] = new2
    elif ant in dwitiyaakshar: #nr1 nr2
        t = dwitiyaakshar.index(ant)
        var[-1] = prathamaakshar[t]
        new1 = varna.varnaSamdhi(var)
        var[-1] = tratiyaakshar[t]
        new2 = varna.varnaSamdhi(var)
        table[0][0] = new1+"-"+new2
        table[20][0] = new1
        for i in bhakaaradi: #nr3
            table[i][0] = new2
    elif ant == "न्" and var[-2] == "इ": #r15
        var[-2] = "ई"
        new = varna.varnaSamdhi(var)
        table[0][0] = new
    elif ant == "न्": #r13
        var[-1] = ""
        new = varna.varnaSamdhi(var)
        for i in halaadi:
            table[i][0] = new
    elif ant == "र्": #r28, r29, r30
        t = hrasva_svar.index(ns.updhaSangya(y))
        var[ns.updhaSangya(y)] = dirgha_svar[t]
        new = varna.varnaSamdhi(var)
        for i in halaadi:
            table[i][0] = new
        new_vv = varna.varnaVicched(new)
        new_vv[-1] = ayogvaha[0]
        new_11 = varna.varnaSamdhi(new_vv)
        table[0][0] = new_11
        table[20][1] = "षु"
    elif ant == "स्": #r34, r36
        if var[-2] in hrasva_svar and ling != "N":
            t = hrasva_svar.index(var[-2])
            var[-2] = dirgha_svar[t]
            var[-1] = ayogvaha[0]
        new = varna.varnaSamdhi(var)
        table[0][0] = new
        new_v = varna.varnaVicched(table[20][0])
        new_v[-1] = ayogvaha[0]
        new2 = varna.varnaSamdhi(new_v)
        table[20][0] = table[20][0]+"-"+new2
        print(var_o[-2])
        if var_o[-2] != "इ" and var_o[-2] != "उ":
            var_n = varna.varnaVicched(table[7][0])
            var_n[-1] = "उ"
            if var[-2] in hrasva_svar:
                t = hrasva_svar.index(var[-2])
                var[-2] = dirgha_svar[t]
            new3 = sd.gunSandhi(varna.varnaSamdhi(var_n[:-1]), var_n[-1])
            for i in bhakaaradi:
                table[i][0] = new3
        elif var_o[-2] == "इ" or var_o[-2] == "उ":
            if ling!= "N":
                t = hrasva_svar.index(var[-2])
                var[-2] = dirgha_svar[t]
            var[-1] = "र्"
            new3 = varna.varnaSamdhi(var)
            for i in bhakaaradi:
                table[i][0] = new3
    return table

print(halant_halaadi(change(list_constructor(baselist, subant), lingam), lingam))
