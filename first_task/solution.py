#The following code makes a request to the Sandbox server
#in order to validate a request for a Card-On-File query 


#The requests library is standard for HTTP requests in python
from urllib.error import HTTPError
import requests


#Server url to use
url_ = 'https://sandbox.api.visa.com/cofds-web/v1/datainfo' 



#Basic Auth info
required_id = 'Y2XYXHGP26YURTXGSV7721vUPlpb3olv1vAV9Rz0VN-f2BGgk'
required_password = '505rHgTlS95'
required_cert = '/Users/shalom/Desktop/visa/cert.pem'
required_key = '/Users/shalom/Desktop/visa/key_df55f1bb-c724-4939-8613-3c7bc13d384c.pem'
timeout_ = 5


#Details of transaction to validate
request_data = {
   "requestHeader":{
      "requestMessageId":"6da6b8b024532a2e0eacb1af58581",
      "messageDateTime":"2019-02-35 05:25:12.327"
   },
   "requestData":{
      "pANs":[
         4072208010000000
      ],
      "group":"STANDARD"
   }
}





#Make a post request and inspect its response
try:
  response = requests.post(url= url_, auth= (required_id, required_password,), cert= (required_cert, required_key), json= request_data)                

  print(response.request.headers)
  print(response.request.body)
except HTTPError as e:
    print(e)


if response.status_code == 200:
    print('Verification successful')
else:
    print(str(response.status_code))
