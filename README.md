# Talend Admin Console API
The Talend Administration Center MetaServlet API is an RPC style HTTP API, (not restful) that it is very easy to use and can be easily wrapped with a RESTful interface if desired.

## Objective:
Run Job Conductors using Talend Admin Console API

## Invoking the Talend Administration Center API interactively

Interactively invoke the Talend Administration Center API.
Procedure:
- Go to the Job Conductor page of Talend Administration Center, select the arrow icon next to any of the columns and make sure the Id column is checked so that it will be displayed.
Note that you can also retrieve the ID of the task using MetaServlet by executing the getTaskIdByName command, see [Talend Administration Center MetaServlet API commands](https://help.talend.com/reader/oYf9gKhmYrkWCiSua4qLeg/SLiAyHyDTjuznLR_F~MiQQ).
- Encode the MetaServlet JSON arguments in base64.
- Get the url

```
http://<host>:<port>/<TalendAdministrationCenter_name>/metaServlet?<base64_arguments>
```

`http://localhost:8080/org.talend.administrator/metaServlet?ew0KICAiYWN0aW9uTmFtZSI6ICJydW5
UYXNrIiwNCiAgImF1dGhQYXNzIjogInRhZG1pbiIsDQogICJhdXRoVXNlciI6ICJ0YWRtaW5AZW9zdC5uZXQiLA0KI
CAibW9kZSI6ICJhc3luY2hyb25vdXMiLA0KICAidGFza0lkIjogIjgiDQp9DQo=`

The result of the HTTP Get message is returned as JSON to the object. It includes the execRequestId which is the handle for your new Job instance.

```json
{ execRequestId: "1432855205979_a5zn8", executionTime: { millis: 564, seconds: 0 }, returnCode: 0 }
```

- Once the HTTP Get message is sent, monitor the progress of the execution through the Execution History page of Talend Administration Center.
