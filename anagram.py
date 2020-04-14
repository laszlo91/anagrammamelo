from collections import Counter


def anagram(name):


    with open("morph-it_048_utf8.txt") as file:
        morphit = [i.split('\t')[0].lower() for i in file.readlines() if i.split('\t')[-1]\
            .startswith(("ADV","VER","ADJ","AUX","INT", "NOUN"))]
               
    name = list(name.lower())

    counter_name = Counter([i for i in name if i not in [' ', '.', '-', ',']])


    morphit_candidates = []
    for word in morphit:
        if [i for i in list(word) if i not in name] == []:
            counter_word = Counter(list(word))
            if counter_word & counter_name == counter_word:
                morphit_candidates.append(word)
        
    morphit_candidates = set(morphit_candidates)

    anagrams = []
    for i in morphit_candidates:
        for j in morphit_candidates:
            if Counter(list(i) + list(j)) == counter_name:
                anagrams.append((i + " " + j))
    
    return anagrams
