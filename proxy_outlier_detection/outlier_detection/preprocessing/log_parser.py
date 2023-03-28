import re
import pandas as pd
class LogParser:

    def __init__(self) -> None:
        pass

    #   #given a line of a generic log entry of the format shown in line 7, return a dictionary of labeled informtion
    def generic_line_parser(self, log_line):
        def to_epoch(dt):
            epoch = pd.to_datetime('1970-01-01')
            return (dt - epoch).total_seconds()
        log_line = ' '.join(log_line.split())
        logPattern = '\[(?P<dateTime>.*?) (?P<timezone>.*?)\] \"(?P<userName>.*?)\" (?P<sourceIP>.*?) (?P<destinationIP>.*?) (?P<unknownValue>.*?) (?P<statusCode>.*?) (?P<cacheResult>.*?) \"(?P<httpMethod>.*?) (?P<urlRequested>.*?) HTTP\/(?P<httpVersion>.*?)\" \"(?P<domainClassification>.*?)\" \"(?P<riskClassification>.*?)\" \"(?P<mimeType>.*?)\" (?P<bytesSent>.*?) (?P<bytesReceived>.*?) \"(?P<userAgentString>.*?)\" \"(?P<webReferrerString>.*?)\" \"(?P<urlMeta1>.*?)\" \"(?P<urlMeta2>.*?)\" \"(?P<urlMeta3>.*?)\" \"(?P<urlMeta4>.*?)\"'
        matched = re.match(logPattern, log_line)
        matched_dict = matched.groupdict()
        #   #get the timestamp as a string, reformated to feed into pd.to_datetime
        #   #get the epoch time using the to_epoch function
        valPartitioned = log_line.split(" ")
        dt_string = valPartitioned[0].replace("[", "").replace(":"," ", 1)
        timeZone = valPartitioned[1].replace("]","")
        dt_string = dt_string + " " + timeZone
        dt_obj = pd.to_datetime(dt_string)
        dt_obj = dt_obj.replace(tzinfo=None)
        convertedTime = to_epoch(dt_obj)
        #now appended the dictionary with the dt_obj object and dt_string and
        #the concatinated URL meta data
        matched_dict['convertedTime'] = convertedTime
        matched_dict['timeString'] = dt_string
        matched_dict['urlMeta'] =  matched_dict['urlMeta1'] + " " + matched_dict['urlMeta2'] + " " + matched_dict['urlMeta3'] + " " + matched_dict['urlMeta4']
        return(matched_dict)