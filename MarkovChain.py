data = "hello hello helli"
def generateTable(data, k=4):
    T = {}
    for i in range(len(data) - k):
        X = data[i:i + k]
        y = data[i + k]
        if T.get(X) is None:
            T[X] = {}
            T[X][y] = 1
        else:
            if T[X].get(y) is None:
                T[X][y] = 1
            else:
                T[X][y] += 1
    return T
T = generateTable(data)
T

def convertFreqIntoProb(T):
    for kx in T.keys():
        s = float(sum(T[kx].values()))
        for k in T[kx].keys():
            T[kx][k] =  T[kx][k]/s
    return T
convertFreqIntoProb(T)

with open("english_speech_2.txt") as f:
  text = f.read().lower()
print(text)
def trainMarkovChain(text,k=4):
  T = generateTable(text)
  T = convertFreqIntoProb(T)
  return T
T = trainMarkovChain(text)
print(T)
import numpy as np
def sample_text(ctx,T,k=4):
  ctx = ctx[-k:]
  if T.get(ctx) is None:
    return ""
  possible_chars = list(T[ctx].keys())
  possible_prob = list(T[ctx].values())
  return np.random.choice(possible_chars, p = possible_prob)
sample_text("flag ",T)
def generateText(starting_sent, k=4, maxLen=1000):
    sentence = starting_sent
    ctx = starting_sent[-k:]
    for ix in range(maxLen):
        next_pred = sample_text(ctx, T, k)
        sentence += next_pred
        ctx = sentence[-k:]
    return sentence

fake =generateText("people")
print(fake)
