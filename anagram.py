def anagram(name):
    
    name = [i for i in list(name.lower()) if i not in ["'"," ", ".", "-", ","]]

    with open("morph-it_048_utf8.txt") as file:
        morphit = [i.split('\t')[0].lower() for i in file.readlines() if i.split('\t')[-1]\
            .startswith(("ADV","VER","ADJ","AUX","INT", "NOUN"))]
            
    def contrast1(word,name):
        for letter in word:
            if letter not in name:
                return False
            if name.count(letter) < word.count(letter):
                return False
        return True
    
    def contrast2(word,name):
        if len(word) != len(name):
            return False
        for letter in word:
            if name.count(letter) < word.count(letter):
                return False
        return True
        
    
    morphit_candidates = []
    for word in morphit:
        if contrast1(list(word),name) is True:
            morphit_candidates.append(word)
        
    morphit_candidates = set(morphit_candidates)
    
    a=[]
    for w1 in morphit_candidates:
        for w2 in morphit_candidates:
            if contrast2(list(w1)+list(w2), name) is True:
                a.append(w1+" "+w2)
                
    return a
