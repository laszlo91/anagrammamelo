def openmorphit():
    with open("morphit.txt") as file:
        morphit = [i.split('\t')[0].lower() for i in file.readlines() if i.split('\t')[-1]\
            .startswith(("ADV","VER","ADJ","AUX","INT", "NOUN"))]
        return morphit


def cleanup(name):    
    return [i for i in name if i not in ["'"," ", ".", "-", ","]]

    
def isanagram(word,name):
    if len(word) != len(name):
        return False
    if word == name:
        return False
    for letter in word:
        if name.count(letter) < word.count(letter):
            return False
    return True

    
def filter_candidates(name, morphit):
        
    def issublist(word,name):
        for letter in word:
            if letter not in name:
                return False
            if name.count(letter) < word.count(letter):
                return False
        return True
        
    morphit_candidates = []
    for word in morphit:
        w = list(word)
        if issublist(w,name):
            morphit_candidates.append(word)
    return morphit_candidates


def monogram(name, morphit):
    
    name = cleanup(name)
    b = []
    for i in morphit:
        if isanagram(list(i), name):
            b.append(i)
    return set(b)

    
def anagram(name, morphit):
    
    name = list(name.lower())
    
    if " " not in name and len(name) < 12:
        return monogram(name, morphit)
    
    name = cleanup(name)
            
    morphit_candidates = set(filter_candidates(name, morphit))
            
    a=[]
    for w1 in morphit_candidates:
        for w2 in morphit_candidates:
            if isanagram(list(w1)+list(w2), name):
                a.append(w1+" "+w2)
    return a
