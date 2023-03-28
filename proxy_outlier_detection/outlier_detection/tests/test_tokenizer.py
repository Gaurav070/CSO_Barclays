from unittest import TestCase

from outlier_detection.preprocessing.tokenizer import tokenizeText

class TestTokenizer(TestCase):

    def setUp(self) -> None:
        self.log_sample = '[02/Aug/2011:22:00:00 -0700] "user_1" 0.0.0.0 0.0.0.0  9080 200 TCP_HIT "GET http://games.maktoob.com/smart/gamesCH1/gimages/smart1040.jpeg HTTP/1.0" "unknown"  "low risk" "image/jpeg" 2370 409 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.237 Safari/534.10" "i1.makcdn.com" "-" "0" "" "-"'
    
    def test_tokenize_test_success(self) -> None:
        result = tokenizeText(self.log_sample)
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], int)