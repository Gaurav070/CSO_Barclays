# <b>CS_Proxies_Anomaly_Detection_API</b>
A Utility to detect anomaly in proxy logs of user activities on user agents

TO Run this utility, please do the following steps.


1. <b>Install requirement.txt</b>

pip install -r requirement.txt

2. Pipeline has Two components front end Steamlit UI and Django based API

    a. Run API after locate to /CSO_Barclays/proxy_outlier_detection using command
        <b>python manage.py runserver</b>
        
    b. Run Streamlit UI using python script located in /CSO_Barclays
        <b>streamlit run streamlit_benign_ui.py</b>

3. Upload the sample file located in sample folder in UI and visualise the table

BONUS!

4. <b>Run Unit Test</b>

To run Unit Test locate to /CSO_Barclays/proxy_outlier_detection and run comd

pytest -v ./outlier_detection/tests/

All the Unit test located in /tests folder 

BONUS!

5. Samples benign data and exploit data located under smaples folder

6. Presentation - Notebook is located in notebook folder as a presentation for analysing,training and evaluation of data
