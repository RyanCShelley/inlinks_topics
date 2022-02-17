import pandas as pd
import plotly.express as px
import numpy as np
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions

import streamlit as st

authenticator = IAMAuthenticator('8oDlRra5QVkiUS2DQRfuSQM_rYxRWwY1pr23xWJ8NfV_')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/91f2c64d-4a34-40b2-8aed-c311a315a8c6')


st.title('Internal Link Topic Tagging')

st.subheader('Upload Your Crawl Data')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
		dataframe = pd.read_csv(uploaded_file)
     
st.write(dataframe)

df = pd.read_csv(dataframe)

st.subheader('Topic Annotations')

st.caption('Below is the list of URLs with the associated topics.')

concepts = []

# Loop items in results
for page in df['Address']:
  response = natural_language_understanding.analyze(
    url= page,
    features=Features(concepts=ConceptsOptions(limit=1))).get_result()
  if response is not None:
    concepts.append(response)


df_concepts_full = pd.json_normalize(concepts)
df_concepts_full['concepts'] = pd.json_normalize(df_concepts_full['concepts'])
df_concepts_full = pd.concat([df_concepts_full[['retrieved_url']], pd.json_normalize(df_concepts_full['concepts'])], axis=1)
st.dataframe(df_concepts_full)
