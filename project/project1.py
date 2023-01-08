ma="'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'J.U.U.U Kmltin.mmps iks nmk eio; ---> hkmu"


def fun(dic):  #מחזיר את האותיה שהיתה מופיעה ב   dectinary יותר
    les1 = []
    for n in dic.keys(): #in order to save the key in list
        les1.append(n)
    maxx=0
    for v in dic.values():# to know the bigees value
        if v>maxx:
            maxx=v
    no=0
    for k in dic.values():#the biggess value ,his key show the character that apperd more than the alse character
        if k!=maxx:
            no+=1
        else:
            break
    return les1[no] # return the character that apperd more than the alse character

def fun6(ma): #receive a text string and will replace alphabetical characters in the text with
                #other alphabetical characters
    dic={}
    ma=ma.lower()
    for s in ma:   #to count howmany times the letter appeard in the text
        if  s.isalpha():
            num=0
            for m in ma: #it checks each letter
                if s==m :
                    num+=1
            dic[s]=num #save the charaty in the key and how many times apperd in valuo

    de={}
    de[fun(dic)]="e"
    de["e"]=fun(dic)
    dic.pop(fun(dic))
    de[fun(dic)]="t"
    de["t"]=fun(dic)
    dic.pop(fun(dic))
    de[fun(dic)]="o"
    de["o"]=fun(dic)
    dic.pop(fun(dic))
    de[fun(dic)]="r"
    de["r"]=fun(dic)
    dic.pop(fun(dic))
    return de
print(fun6("'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'J.U.U.U Kmltin.mmps iks nmk eio; ---> hkmu"))




def fun2(ma):
    den=fun6(ma) #  the fun that save the described connection between the letters into a dictionary
    lek=[]
    for c in den.keys(): # to save the key in dectionary
        lek.append(c)
    lev=[]
    for v in den.values(): # to save the values in dectionary
        lev.append(v)
    stt=""
    for c in ma: #
        if c==lev[0]:  # if the charectors in the dectionary is appeard chang it to the appropriate
                       # letter and save in anather string (stt) ( the  charector in values list chag it to the key list

          stt+=lek[0]
        elif c==lev[1]:
            stt+=lek[1]
        elif c==lev[2]:
            stt+=lek[2]
        elif c==lev[3]:
            stt+=lek[3]
        elif c==lev[4]:
            stt+=lek[4]
        elif c == lev[5]:
            stt += lek[5]
        elif c == lev[6]:
            stt += lek[6]
        elif c == lev[7]:
            stt += lek[7]
        else:
            stt+=c # if the charector is not in the dictionary add to the sting (stt)
    return stt

print(fun2("'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'J.U.U.U Kmltin.mmps iks nmk eio; ---> hkmu"))




def funfile(ma):
    lin=ma
    f = fun2(ma)
    with open("results.txt","w") as file:
        file.write(fun2(ma))
    with open("file_Original.txt", "w+" ) as file :

        file.write(lin)
        file.write("The encryption for the above text is:")
        file.write(f)




funfile("'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'J.U.U.U Kmltin.mmps iks nmk eio; ---> hkmu")


def fun0(f):
    with open("results.txt","r") as file:
        file.seek(0)
        no=file.readline()
        sp=no.split()
    spindx=0
    dic={}
    for n in sp:
        su=0
        for x in n:
            if x.isalpha():
                su+=1

        dic[sp[spindx]]=su
        spindx += 1

    maxum=0
    for m in dic.values():
        if m>maxum:
            maxum=m
    l=[]
    for j in dic.keys():
        if dic.get(j)==maxum:
            l.append(j)

    return l

def fun8(f):
    with open("results.txt","r")as file:
        file.seek(0)
        lefile=file.readlines()
        lefile=len(lefile)
    return lefile

print(funfile("'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'J.U.U.U Kmltin.mmps iks nmk eio; ---> hkmu"))

print(fun0("'Practice, eventually makes perfect. All you need is Python.'J.U.U.U Kolkin.oops its not him; ---> etor"))
print(fun8("'Practice, eventually makes perfect. All you need is Python.'J.U.U.U Kolkin.oops its not him; ---> etor"))