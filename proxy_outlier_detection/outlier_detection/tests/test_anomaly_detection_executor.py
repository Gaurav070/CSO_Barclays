from unittest import TestCase
from unittest.mock import ANY, MagicMock, patch
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.svm import OneClassSVM
from outlier_detection.preprocessing.log_parser import LogParser
from outlier_detection.executor.anomaly_detection_executor import AnomalyDetectionExecutor

class TestAnomalyDetectionExecutor(TestCase):
    
    def setUp(self) -> None:
        self.anomaly_detection_executor = AnomalyDetectionExecutor()
        clf = OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
        self.model = Pipeline([('clf', clf)])

    # def mock_response():
    #     log_dict = dict()
    #     log_dict["userName"] = "user_1"
    #     log_dict["cacheResult"] = "TCP_HIT"
    #     log_dict["userAgentString"] = "Mozilla/5.0"
    #     response = dict()
    #     response["status"] = 200
    #     response["description"] = "description"
    #     response["message"] = "success"
    #     response["log_details"] = log_dict
    #     return Response(data=response, status=200)
    
    def log_dict():
        log_dict = dict()
        log_dict["userName"] = "user_1"
        log_dict["cacheResult"] = "TCP_HIT"
        log_dict["userAgentString"] = "Mozilla/5.0"
        return log_dict


    def prepare_request_data():
        request_data = dict()
        request_data["log"] = '[02/Aug/2011:22:00:00 -0700] "user_1" 0.0.0.0 0.0.0.0  9080 200 TCP_HIT "GET http://games.maktoob.com/smart/gamesCH1/gimages/smart1040.jpeg HTTP/1.0" "unknown"  "low risk" "image/jpeg" 2370 409 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.237 Safari/534.10" "i1.makcdn.com" "-" "0" "" "-"'
        return request_data
    
    @patch.object(LogParser, "generic_line_parser", MagicMock(args=ANY, return_value = log_dict()))
    @patch.object(AnomalyDetectionExecutor, "map_prediction_to_label", MagicMock(args=ANY, return_value = "benign"))
    @patch.object(Pipeline, "predict", MagicMock(args=ANY, return_value = np.array([1])))
    def test_api_view_benign(self) -> None:
        request_data = dict()
        request_data["log"] = '[02/Aug/2011:22:00:00 -0700] "user_1" 0.0.0.0 0.0.0.0  9080 200 TCP_HIT "GET http://games.maktoob.com/smart/gamesCH1/gimages/smart1040.jpeg HTTP/1.0" "unknown"  "low risk" "image/jpeg" 2370 409 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.237 Safari/534.10" "i1.makcdn.com" "-" "0" "" "-"'
        response = self.anomaly_detection_executor.process_anomaly_detection(request_data['log'], self.model)
        self.assertEqual(response['status'], 200)
        self.assertEqual(response['prediction_metadata']['label'], "benign")
    
    @patch.object(LogParser, "generic_line_parser", MagicMock(args=ANY, return_value = log_dict()))
    @patch.object(AnomalyDetectionExecutor, "map_prediction_to_label", MagicMock(args=ANY, return_value = "not benign"))
    @patch.object(Pipeline, "predict", MagicMock(args=ANY, return_value = np.array([-1])))
    def test_api_view_not_benign(self) -> None:
        request_data = dict()
        request_data["log"] = '[02/Aug/2011:22:00:00 -0700] "user_1" 0.0.0.0 0.0.0.0  9080 200 TCP_HIT "GET http://games.maktoob.com/smart/gamesCH1/gimages/smart1040.jpeg HTTP/1.0" "unknown"  "low risk" "image/jpeg" 2370 409 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.237 Safari/534.10" "i1.makcdn.com" "-" "0" "" "-"'
        response = self.anomaly_detection_executor.process_anomaly_detection(request_data['log'], self.model)
        self.assertEqual(response['status'], 200)
        self.assertEqual(response['prediction_metadata']['label'], "not benign")
    
    def test_map_prediction_to_label_benign(self) -> None:
        result = self.anomaly_detection_executor.map_prediction_to_label(1)
        self.assertEqual(result, "benign")
    
    def test_map_prediction_to_label_not_benign(self) -> None:
        result = self.anomaly_detection_executor.map_prediction_to_label(-1)
        self.assertEqual(result, "not benign")

    



