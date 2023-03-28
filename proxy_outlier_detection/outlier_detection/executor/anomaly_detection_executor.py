from outlier_detection.preprocessing.log_parser import LogParser
import pandas as pd
class AnomalyDetectionExecutor:

    def __init__(self) -> None:
        pass

    def process_anomaly_detection(self, inference_data, model):
        try:
            response = dict()
            logs = list()
            log_details = dict()
            response["status"] = None
            response["description"] = None
            log_details = LogParser().generic_line_parser(inference_data)
            logs.append(log_details)
            benign_df = pd.DataFrame(logs)
            benign_df_series = pd.Series(benign_df['userAgentString'])
            prediction = model.predict(benign_df_series)
            log_details['label'] = self.map_prediction_to_label(prediction[0])
            response['status'] = 200
            response["description"] = "Prediction Successful!"
            response["message"] = "Success"
            response['prediction_metadata'] = dict()
            response['prediction_metadata']['label'] = log_details['label']
            response['prediction_metadata']['userName'] = log_details['userName']
            response['prediction_metadata']['userAgentString'] = log_details['userAgentString']
            response['prediction_metadata']['score'] = prediction[0]
            return response
        except Exception as e:
            response = dict()
            response["status"] = 422
            response["description"] = "Unprocessible Entity"
            response["message"] = "Failed"
            response["prediction_metadata"] = dict()
            return response
    
    def map_prediction_to_label(self, prediction):
        if prediction==1:
            return "benign"
        elif prediction==-1:
            return "not benign"
        else:
            raise NotImplementedError("No Prediction")