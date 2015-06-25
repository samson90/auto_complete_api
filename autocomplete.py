import os
from flask import Flask, jsonify
from flask.ext.cors import CORS
import pandas
import predict

app = Flask(__name__)
cors = CORS(app)

# load term document matrices
one_tdm = pandas.read_csv('csv/one_tdm.csv', sep=" ")
one_tdm = one_tdm.sort('freq', ascending=False)
one_tdm = one_tdm[0:3]

two_tdm = pandas.read_csv('csv/two_tdm.csv', sep=" ")
two_tdm = two_tdm.set_index('n1')

three_tdm = pandas.read_csv('csv/three_tdm.csv', sep=" ")
three_tdm.set_index(['n2', 'n1'], inplace=True)
three_tdm.sort_index(inplace=True)

@app.route('/autocomplete/api/v1.0/words/<phrase>', methods=['GET'])
def get_words(phrase):
	words, freqs = predict.predictWords(phrase, one_tdm, two_tdm, three_tdm)
	predicted_words = []
	for word, freq in zip(words, freqs):
		predicted_words.append({'word': word, 'freq': freq})
	return jsonify({'words': predicted_words})