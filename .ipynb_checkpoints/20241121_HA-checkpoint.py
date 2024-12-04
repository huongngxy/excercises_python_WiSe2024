
import matplotlib
import matplotlib.pyplot as plt

def buchstaben_häufigkeit (x):
    mein_d = {}

    for b in x.lower():
        if b.isalpha():
            if b not in mein_d:
                mein_d[b] = 1
            else: 
                mein_d[b] += 1
                
    mein_d_sorted = dict(sorted(mein_d.items()))
    return mein_d_sorted

bh_dict1 = buchstaben_häufigkeit(x = "123Wie geht es Ihnen")
bh_dict2 = buchstaben_häufigkeit (x = "Hallo, Berlin")

#buchstaben_häufigkeit(x = "Hallo, HWR Berlin")

plt.bar(bh_dict1.keys(), bh_dict1.values())
#plt.bar(bh_dict2.keys(), bh_dict2.values())
plt.show()