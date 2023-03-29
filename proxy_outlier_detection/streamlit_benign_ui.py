import streamlit as st
import os
import pandas as pd
import time
import requests
import matplotlib.pyplot as plt
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
        labels = 'Benign', 'Not Benign'
        if len(final_benign_df['label'].value_counts())==2:
            sizes = [final_benign_df['label'].value_counts()[0], final_benign_df['label'].value_counts()[1]]
        else:
            sizes = [final_benign_df['label'].value_counts()[0], 0]

        explode = (0, 0.1)
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)
        st.success("Completed!")
        
         
