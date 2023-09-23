# functions: some functions are being made to manage sangyaas
def halantat(alist):  # this functions remove halant from akshars
    list1 = []
    for i in range(0, len(alist)):
        z = alist[i]
        list1.append(z[0])
    return list1

# Pratyahaar Sutras
pratya1 = ["अ","इ","उ"]
pratya2 = ["ऋ","ऌ"]
pratya3 = ["ए", "ओ"]
pratya4 = ["ऐ","औ"]
pratya5 = ["ह्","य्","व्","र्"]
pratya6 = ["ल्"]
pratya7 = ["ञ्","म्","ङ्","ण्","न्"]
pratya8 = ["झ्","भ्"]
pratya9 = ["घ्","ढ्","ध्"]
pratya10 = ["ज्","ब्","ग्","ड्", "द्"]
pratya11 = ["ख्","फ्","छ्","ठ्","थ्","च्","ट्","त्"]
pratya12 = ["क्","प्"]
pratya13 = ["श्","ष्","स्"]
pratya14 = ["ह्"]
# Akshara Sangyas: Sangyas for working with aksharas. Ach and Hal.
hrasva_svar = ["अ", "इ", "उ", "ऋ", "ऌ"]
dirgha_svar = ["आ", "ई", "ऊ", "ॠ", "ए", "ऐ", "ओ", "औ"]
pluta_svara = ["अ३", "इ३", "उ३", "ऋ३", "ऌ३", "ए३", "ऐ३", "ओ३", "औ३"]
svara = ["अ", "इ", "उ", "ऋ", "ऌ", "ए", "ऐ", "ओ", "औ"]
sarvaSvara = [ "अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ", "औ", "ऋ", "ॠ", "ऌ"]

kavarga = ["क्",  "ख्",  "ग्",  "घ्",  "ङ्"]
chavarga = ["च्",  "छ्",  "ज्",  "झ्",  "ञ्"]
taavarga = ["ट्",  "ठ्",  "ड्",  "ढ्",  "ण्"]
tavarga = ["त्",  "थ्",  "द्",  "ध्",  "न्"]
pavarga = ["प्",  "फ्",  "ब्",  "भ्", "म्"]

antastha = ["य्",  "र्",  "ल्",  "व्"]
ushma = ["श्",  "ष्",  "स्",  "ह्"]

ayogvaha = ["ः",  "", "", "ं", "",  "ꣳ",  "ँ", "ळ्"]
halant = "्"  # special: not included in varnmala
avagrah = "ऽ"  # special: not included in varnmala

matra_hrasva = ["ा", "ि",  "ु", "ृ", "ॢ"]
matra_dirgha = ["ी",  "ू", " ॄ", "े", "ै", "ो", " ौ"]


prathamaakshar = ["क्", "च्","ट्", "त्", "प्"]
dwitiyaakshar = ["ख्", "छ्", "ठ्", "थ्", "फ्",]
tratiyaakshar = ["ग्", "ज्", "ड्", "द्", "ब्"]
chaturthaakshar = ["घ्", "झ्", "ढ्", "ध्", "भ्"]
panchamaaskshar = ["ङ्", "ञ्", "ण्", "न्", "म्"]

# panini sangyas of Aksharas
ach = hrasva_svar + dirgha_svar
hal_niswar = kavarga + chavarga + taavarga + tavarga + pavarga + antastha + ushma
hal_sswar = halantat(hal_niswar)

# sup prakaran's sangyas: these names are for working with sup prakaran
sup = ["सुँ", "औ", "जस्", "अम्", "औट्", "शस्", "टा", "भ्याम्", "भिस्", "ङे", "भ्याम्",
       "भ्यस्", "ङसिँ", "भ्याम्", "भ्यस्", "ङस्", "ओस्", "आम्", "ङि", "ओस्", "सुप्"]

# Sandhi Vishay sangyas: for working with sandhi prakaran
gunSangya = ["ए", "ओ", "अर्", "अल्"]
vrddhiSangya = ["आ", "ऐ", "औ", "आर्"]
