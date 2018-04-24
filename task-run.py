import base64
import requests
import json
import config

taskID = 1
# tac_url = 'http://{host}:8080/org.talend.administrator/metaServlet?'
tac_url = config.tac_url
authUser = config.authUser
authPass = config.authPass

json_txt = { "actionName":"runTask", "authPass":authPass,
  "authUser":authUser, "mode":"asynchronous", "taskId":taskID}

s = json.dumps(json_txt)
# print(s)

encoded_json = str(base64.b64encode(s.encode('utf-8')))
# print(encoded_json)
encoded_url = tac_url+encoded_json

# call encoded_url
response = requests.get(encoded_url)

print(response.text)
