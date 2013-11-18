import random

#random.seed(1)

grammar = [
  ['$noun', 'of', '$adjective'],
  ['$noun', 'of', '$adjective'],
  ['the', '$noun', 'and', 'the', '$noun']
]

partsOfSpeech = dict(
   noun=['kings', 'hammer', 'heart', 'slave', 'warriors', 'blood', 'drums', 'master', 'speakers', 'war', 'death', 'avenger', 'battle', 'mountains', 'crown', 'ring', 'sign', 'warlord', 'outlaws', 'brothers'],
   adjective=['metal', 'courage', 'death', 'war']
)

for i in range(1,10):
    trackName = ''
    structure = grammar[random.randint(0, len(grammar)-1)];
    for part in structure:
        #print(part)
        if (part.startswith('$')):
            source = partsOfSpeech[part[1:]]
            #print(len(source))
            word = source[random.randint(0, len(source)-1)]
        else:
            word = part
        trackName = trackName + word + ' '
    print(str(i) + ". " + trackName)
