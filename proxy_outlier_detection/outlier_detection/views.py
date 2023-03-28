from rest_framework.views import APIView, Response
from outlier_detection.executor.anomaly_detection_executor import AnomalyDetectionExecutor
from outlier_detection.apps import OutlierDetectionConfig
# Create your views here.

class BenignOutlierView(APIView):

    def post(self, request):
        if request.method == 'POST':
            data = request.data
            inference_data = data['log']
            model = OutlierDetectionConfig.model
            anomaly_detector = AnomalyDetectionExecutor()
            response = anomaly_detector.process_anomaly_detection(inference_data=inference_data, model=model)
            if response['status'] == 200:
                return Response(data=response, status=200)
            elif response['status'] == 422:
                return Response(data=response, status=422)
            else:
                return Response(data=response, status=500)

                
        




