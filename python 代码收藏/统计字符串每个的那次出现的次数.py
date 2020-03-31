sentence = 'i can because i think i can'
resut={word: sentence.split().count(word) for word in set (sentence.split())}
print(resut)