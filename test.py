import pandas
from flask import jsonify
import predict

one_tdm = pandas.read_csv('csv/one_tdm.csv', sep=" ")
one_tdm = one_tdm.sort('freq', ascending=False)
one_tdm = one_tdm[0:3]

two_tdm = pandas.read_csv('csv/two_tdm.csv', sep=" ")
two_tdm.set_index('n1', inplace=True)

three_tdm = pandas.read_csv('csv/three_tdm.csv', sep=" ")
three_tdm.set_index(['n2', 'n1'], inplace=True)
three_tdm.sort_index(inplace=True)


value = "this is a test"
words, freq = predict.predictWords("this is a test", one_tdm, two_tdm, 
	three_tdm)

for word, freq in zip(words, freq):
	print(word, freq)