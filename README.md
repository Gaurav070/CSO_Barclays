# <b>CSO_Barclays_Anomaly_Detection_API</b>
A Utility to detect anomaly in proxy logs of user activities on user agents

TO Run this utility, please do the following steps.


1. Install requirement.txt

pip install -r requirement.txt

2. Pipeline has Tow components fornt end Steamlit UI and Django based API
    a. Run API after locate to /CSO_Barclays/proxy_outlier_detection using command
        python manage.py runserver
    b. Run Streamlit UI using python script located in /CSO_Barclays
        streamlit run streamlit_benign_ui.py

3. Upload the sample file located in sample folder in UI and visualise the table

4. Run Unit Test

To run Unit Test locate to /CSO_Barclays/proxy_outlier_detection and run comd

pytest -v ./outlier_detection/tests/

All the Unit test located in /tests folder 
