

#part1:
def fun(dic):   # return the char that apper the most  in the dic
    list_key = []
    for n in dic.keys(): #in order to save the key in list/the charector
        list_key.append(n)
    max_common_char = 0
    for v in dic.values():# to know the bigees value
        if v>max_common_char:
            max_common_char = v
    index_key=0
    for k in dic.values():#the biggess value ,his key show the character that apperd more than the alse character
        if k!=max_common_char:
            index_key += 1
        else:
            break
    return list_key[index_key] # return the character that apperd more than the alse character

def fun6(text_input): #receve the text
    dic = {}
    text_input = text_input.lower()
    for s in text_input:   #to count howmany times the letter appear in the text
        if s.isalpha():
            num = 0
            for m in text_input: #it checks each letter (check all the charectors)
                if s==m:
                    num += 1
            dic[s] = num #save the  character in the key and how many times apperd in value

    dic_chars = {}
    dic_chars[fun(dic)] = "e"     #fun(dic) -- return the most comonr char
    dic_chars["e"]=fun(dic)
    dic.pop(fun(dic))      # remove the most common char from the dictionart
    dic_chars[fun(dic)]= "t"
    dic_chars["t"]=fun(dic)
    dic.pop(fun(dic))
    dic_chars[fun(dic)]= "o"
    dic_chars["o"]=fun(dic)
    dic.pop(fun(dic))
    dic_chars[fun(dic)]= "r"
    dic_chars["r"]=fun(dic)
    dic.pop(fun(dic))
    return dic_chars
print(fun6("'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'J.U.U.U Kmltin.mmps iks nmk eio; ---> hkmu"))


#part2:
def fun2(texs_input):
    den=fun6(texs_input) #  the fun that save the described connection between the letters into a dictionary
    list_key=[]
    for c in den.keys(): # to save the key in dectionary
        list_key.append(c)
    lev=[]
    for v in den.values(): # to save the values in dectionary
        lev.append(v)

    stt=""
    for do in texs_input: #
        no= do.lower()
        if no==lev[0]:  # if the charectors in the dectionary is appeard chang it to the appropriate
                       # letter and save in anather string (stt) ( the  charector in values list chag it to the key list
            stt+=list_key[0]
        elif no==lev[1]:
            stt+=list_key[1]
        elif no==lev[2]:
            stt+=list_key[2]
        elif no==lev[3]:
            stt+=list_key[3]
        elif no==lev[4]:
            stt+=list_key[4]
        elif no == lev[5]:
            stt += list_key[5]
        elif no == lev[6]:
            stt += list_key[6]
        elif no == lev[7]:
            stt += list_key[7]
        else:
            stt+=do # if it is not charector or the charector is not in the dictionary add to the sting (stt)
    return stt


print(fun2("'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'J.U.U.U Kmltin.mmps iks nmk eio; ---> hkmu"))



#part3:
def funfile():  #to save and add the decrypted text to the original text file and creat a file containing the decrypted
               #thetext results.


    with open("file_Original.txt", "w+" ) as file :

        file.write("'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'\n")
        file.write("J.U.U.U Kmltin.\n")
        file.write("mmps iks nmk eio; ---> hkmu\n")
        file.seek(0)
        so = file.read()
        file.write("The encryption for the above text is:\n")
        file.write(fun2(so) + "\n")

    with open("results.txt","w+") as file:
        file.write(fun2(so))


#part4:
def fun0():  #  will find the longest words in the file results.txt
    with open("results.txt","r") as file:
        file.seek(0)
        no=file.readline()
        sp=no.split()  # the list of readline() fil
    spindx=0
    dic={}
    for n in sp:  #for that check all the liste that have the words in the test file
        su=0
        for x in n: # for that count the character in the word
            if x.isalpha():
                su+=1

        dic[sp[spindx]]=su # save the word in key and character count in value
        spindx += 1

    maxum=0
    for m in dic.values():
        if m>maxum:
            maxum=m  # מספר האותיות במילה הארוכה ביותר
    l=[]
    for j in dic.keys():
        if dic.get(j)==maxum:
            l.append(j) # המילים הארוכות ביותר סאמתי אותם בתוך list
            break
    return l

def fun8():
    with open("results.txt","r")as file: #will return number of lines in the results.txt
        file.seek(0)
        lefile=file.readlines()
        lefile=len(lefile)
    return lefile

print(funfile())
print(fun0())
print(fun8())