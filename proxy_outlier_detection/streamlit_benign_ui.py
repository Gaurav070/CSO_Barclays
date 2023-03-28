import streamlit as st
import os
import pandas as pd
import time
import requests
st.title("CSO Anomaly Detection Assignment")

benign_proxy_file = st.file_uploader("choose file", type = ["webgateway", "txt"])
if benign_proxy_file is not None:
    button = st.button("Process....")
    user_agent_strings = benign_proxy_file.read().splitlines()
    final_benign_df = pd.DataFrame()
    if button:
        with st.spinner("Processing.."):
            results = list()
            for line in user_agent_strings:
                request = dict()
                request['log'] = line
                response = requests.post(url="http://localhost:8000/benign_outlier_detection/", data=request)
                results.append(response.json()['prediction_metadata'])
                final_benign_df = pd.DataFrame(results)
                st.dataframe(final_benign_df)
        st.success("Completed!")
        
         
