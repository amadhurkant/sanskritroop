import varna
import niyamSangyas as ns
from sangya import *

def yanSandhi(word1, word2):
    word1 = varna.varnaVicched(word1)
    word2 = varna.varnaVicched(word2)
    v1 = word1[-1]
    if ns.savarnSangya(v1, word2[0]) is False:
        if v1 == "इ" or v1 == "ई":
            word1[-1] = "य्"
        elif v1 == "उ" or v1 == "ऊ":
            word1[-1] = "व्"
        elif v1 == "ऋ" or v1 == "ॠ":
            word1[-1] = "र्"
        elif v1 == "ऌ":
            word1[-1] = "ल्"
    else:
        raise Exception("yanSandhi() called but can't be performed as words don't satisfy 'इको यणाचि' (6/1/77)")
    word = varna.varnaSamdhi(word1+word2)
    return word

def ayadiSandhi(word1, word2):
    word1 = varna.varnaVicched(word1)
    word2 = varna.varnaVicched(word2)
    v1 = word1[-1]
    if ns.savarnSangya(v1, word2[0]) is False:
        if v1 == "ए":
            word1[-1] = "य्"
            word1.insert(-1, "अ")
        if v1 == "ऐ":
            word1[-1] = "य्"
            word1.insert(-1, "आ")
        if v1 == "ओ":
            word1[-1] = "व्"
            word1.insert(-1, "अ")
        if v1 == "औ":
            word1[-1] = "व्"
            word1.insert(-1, "आ")
    else:
        raise Exception("ayadiSandhi() called but can't be performed as words don't satisfy 'एचोऽयवायावः' (6/1/78)")
    word = varna.varnaSamdhi(word1+word2)
    return word

def gunSandhi(word1, word2):
    word1 = varna.varnaVicched(word1)
    word2 = varna.varnaVicched(word2)
    v1 = word1[-1]
    v2 = word2[0]
    if v1 in ["अ", "आ"] and v2 in  sarvaSvara and ns.savarnSangya(v1, v2) is False:
        if v1 in ["अ", "आ"] and v2 in ["इ", "ई"]:
            word1[-1] = gunSangya[0]
            word2[0] = ""
        if v1 in ["अ", "आ"] and v2 in ["उ", "ऊ"]:
            word1[-1] = gunSangya[1]
            word2[0] = ""
        if v1 in ["अ", "आ"] and v2 in ["ऋ", "ॠ"]:
            word1[-1] = gunSangya[2][:1]
            word2[0] = gunSangya[2][1:]
        if v1 in ["अ", "आ"] and v2 in ["ऌ"]:
            word1[-1] = gunSangya[3][:1]
            word2[0] = gunSangya[3][1:]
    else:
        raise Exception("gunSandhi() called but can't be performed as words don't satisfy 'आद्गुणः' (6/1/87)")
    word = varna.varnaSamdhi(word1+word2)
    return word

def vrddhiSandhi(word1, word2):
    word1 = varna.varnaVicched(word1)
    word2 = varna.varnaVicched(word2)
    v1 = word1[-1]
    v2 = word2[0]
    if v1 in ["अ", "आ"] and v2 in sarvaSvara and ns.savarnSangya(v1, v2) is False:
        if v1 in ["अ", "आ"] and v2 in ["ए", "ऐ"]:
            word1[-1] = vrddhiSangya[1]
            word2[0] = ""
        if v1 in ["अ", "आ"] and v2 in ["ओ", "औ"]:
            word1[-1] = vrddhiSangya[2]
            word2[0] = ""
    else:
        raise Exception("vraddhiSandhi() called but can't be performed as words don't satisfy 'वृद्धिरेचि' (6/1/88)")
    word = varna.varnaSamdhi(word1+word2)
    return word

def savarndirghaSandhi(word1, word2):
    word1 = varna.varnaVicched(word1)
    word2 = varna.varnaVicched(word2)
    v1 = word1[-1]
    v2 = word2[0]
    if v1 in sarvaSvara and v2 in sarvaSvara and ns.savarnSangya(v1, v2) is True:
        if v1 in ["अ", "आ"] and v2 in ["अ", "आ"]:
            word1[-1] = "आ"
            word2[0] = ""
        if v1 in ["इ", "ई"] and v2 in ["इ", "ई"]:
            word1[-1] = "ई"
            word2[0] = ""
        if v1 in ["उ", "ऊ"] and v2 in ["उ", "ऊ",]:
            word1[-1] ="ऊ"
            word2[0] = ""
        if v1 in ["ए", "ऐ"] and v2 in ["ए", "ऐ"]:
            word1[-1] = "ऐ"
            word2[0] = ""
        if v1 in ["ओ", "औ"] and v2 in ["ओ", "औ"]:
            word1[-1] = "औ"
            word2[0] = ""
        if v1 in ["ऋ", "ॠ"] and v2 in ["ऋ", "ॠ"]:
            word1[-1] = "ॠ"
            word2[0] = ""
    else:
        raise Exception("savarndirghaSandhi() called but can't be performed as words don't satisfy 'अकः सवर्णे दीर्घः' (6/1/101)")
    word = varna.varnaSamdhi(word1+word2)
    return word
