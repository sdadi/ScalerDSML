import numpy as np

scores = np.loadtxt('survey.txt', dtype ='int')
print(scores.ndim, scores.shape, scores)
print(len(scores))

print('print first 10 user scores:', scores[:10])

print('print scores which are less than 6:', len(scores[scores <= 6]))

print('print only promoters count: ', len(scores[scores >= 9]))

print('nps score being added',len(scores[scores >= 9]) - len(scores[scores <= 6]))

print('nps score is: ', (len(scores[scores >= 9]) - len(scores[scores <= 6])) / len(scores) * 100)