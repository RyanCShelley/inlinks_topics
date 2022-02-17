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
