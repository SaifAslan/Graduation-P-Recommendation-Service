from flask import Flask

import pandas as pd
import pickle

app = Flask(__name__)

def load_model():
    pk_filename = "pickle_model.pkl"
    with open (pk_filename, 'rb') as file:
     model = pickle.load(file)
    return model

def load_indicies():
    pk_filename = "products_indicies.pkl"
    with open (pk_filename, 'rb') as file:
     model = pickle.load(file)
    return model

cosine_sim = load_model()

indicies= load_indicies()

@app.route('/')
def index():
 return "hello!"

@app.route('/get-recommendations/<id>')
def index_recommendations(id):
  return get_recommendations(id)

def get_recommendations(id, cosine_sim=cosine_sim):
  index=indicies[int(id)]
  sim_scores = enumerate (cosine_sim[index])
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
  sim_scores = sim_scores [1:11]
#   for i in sim_scores:
#     print(i)
  sim_index = [i[0] for i in sim_scores]
  return [i for i in indicies.iloc[sim_index].index] 
  # print (df["merged_column"].iloc[sim_index])