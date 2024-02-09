# <b>Proxies_Anomaly_Detection_API</b>
A Utility to detect anomalies in proxy logs of user activities on user agents

TO Run this utility, please do the following steps.


1. <b>Install requirement.txt</b>

pip install -r requirement.txt

2. Pipeline has Two components front-end Steamlit UI and the back-end Django-based API

    a. Run API after locating to /Proxy_Outlier_Detection/proxy_outlier_detection using command
        <b>python manage.py runserver</b>
        
    b. Run Streamlit UI using Python script located in /Proxy_Outlier_Detection
        <b>streamlit run streamlit_benign_ui.py</b>

3. Upload the sample file located in the sample folder in UI and visualize the table

4. <b>Run Unit Test</b>

To run Unit Test locate to /Proxy_Outlier_Detection/proxy_outlier_detection and run cmd

pytest -v ./outlier_detection/tests/

All the Unit tests are located in /tests folder 

5. Samples benign data and exploit data located under samples folder

6. EDA - The notebook is located in the notebook folder as a presentation for analyzing, training and EDA
