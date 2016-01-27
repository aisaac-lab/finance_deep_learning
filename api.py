#coding:utf-8

import json, urllib2
import numpy as np

def get_training_data():
    url = "http://scholes.io/api/v1/listings/training_data"
    r = urllib2.urlopen(url)
    datas = json.loads(r.read())
    training_inputs = []
    training_results = []
    for data in datas:
        training_inputs.append([data['unit_offer_price'], data['stock_market'], data['business_category'], data['population']])
        training_results.append(data['result'])
    np_training_inputs = [np.reshape(x, (4, 1)) for x in np.array(training_inputs)]
    n = len(training_results)
    np_training_results = np.array(training_results).reshape(n,1)
    training_data = zip(np_training_inputs, np_training_results)
    return training_data

def get_test_data():
    url = "http://scholes.io/api/v1/listings/test_data"
    r = urllib2.urlopen(url)
    datas = json.loads(r.read())
    training_inputs = []
    training_results = []
    for data in datas:
        training_inputs.append([data['unit_offer_price'], data['stock_market'], data['business_category'], data['population']])
        training_results.append(data['result'])
    np_training_inputs = [np.reshape(x, (4, 1)) for x in np.array(training_inputs)]
    n = len(training_results)
    np_training_results = np.array(training_results).reshape(n,1)
    training_data = zip(np_training_inputs, np_training_results)
    return training_data

def get_data(code):
    url = "http://scholes.io/api/v1/listings/{0}".format(code)
    r = urllib2.urlopen(url)
    data = json.loads(r.read())
    training_inputs = []
    training_results = []
    training_inputs.append([data['unit_offer_price'], data['stock_market'], data['business_category'], data['population']])
    training_results.append(data['result'])
    np_training_inputs = [np.reshape(x, (4, 1)) for x in np.array(training_inputs)]
    n = len(training_results)
    np_training_results = np.array(training_results).reshape(n,1)
    training_data = zip(np_training_inputs, np_training_results)
    return training_data
