# samplewebapp
Sample Django Web App

### Design and Architecture
#### Database Schema
![DB Schema Diagram](static/design/DBSchema.png?raw=true "")

#### Events Diagram
###### Version 1 (Implemented Here)
Assumes that PDF Generation and Upload does not consume much time.
![Events Diagram](static/design/EventsDiagramBasic.png?raw=true "")


###### Version 2 (Asynchronous)
Assumes that PDF Generation and Upload will consume time because of large data and hence it is handled asynchronously.
![Events Diagram](static/design/EventsDiagram.png?raw=true "")
Queue is AWS SQS.


### API Specifications

#### GET Candidates Data
`GET api/v1/candidates?pageId=<page_id>`

Returns the list of interview candidates in the batch of 10s.

###### Response Object
Status Code 200
```json
[
  {
    "fullName": "Rajat",
    "aadharId": "123456789",
    "dateOfBirth": "01/01/2000",
    "state": "Delhi",
    "pincode": "123456",
    "gender": "Male",
    "email": "abc@abc.abc",
    "primaryPhone": 91123456789,
    "otherPhone": 91123456789,
    "address": "hno.1, My City, Town",
    "longitude": -77, 
    "latitude": 38
  },
  {
    ...
  }
]
```
Status Code !200
```json
{
  "Error": "Error Message"
}
```

###### Response Codes 
TODO

#### POST New Candidates
`POST api/v1/candidates`

Add new candidates to the DB. This endpoint supports multiple uploads.

###### Request Object
```json
[
  {
    "fullName": "Rajat",
    "aadharId": "123456789",
    "dateOfBirth": "01/01/2000",
    "state": "Delhi",
    "pincode": "123456",
    "gender": "Male",
    "email": "abc@abc.abc",
    "primaryPhone": 91123456789,
    "otherPhone": 91123456789,
    "address": "hno.1, My City, Town",
    "longitude": -77, 
    "latitude": 38,
    "experience": 4,
    "skills": ["python", "postgresql"],
    "education": [
      {
        "board": "CBSE", 
        "level": "12",
        "specialization": "PCM",
        "yearOfPassing": 2010,
        "institute": "ABC School"
      },
      {
        "board": "NA", 
        "level": "BTech",
        "specialization": "Computer Science",
        "yearOfPassing": 2014,
        "institute": "ABC University"
      }
    ]
  },
  {
    ...
  }
]
```

###### Response Object
Status Code 200
```json
{
  "totalSuccessful": 10,
  "totalFailed": 2,
  "failedUploads": [
    {
      "reason": "Failure Reason",
      "data": {
        "fullName": "Rajat",
        "aadharId": "123456789",
        "dateOfBirth": "01/01/2000",
        "state": "Delhi",
        "pincode": "123456",
        "gender": "Male",
        "email": "abc@abc.abc",
        "primaryPhone": 91123456789,
        "otherPhone": 91123456789,
        "address": "hno.1, My City, Town",
        "longitude": -77, 
        "latitude": 38,
        "experience": 4,
        "skills": ["python", "postgresql"],
        "education": [
          {
            "board": "CBSE", 
            "level": "12",
            "specialization": "PCM",
            "yearOfPassing": 2010,
            "institute": "ABC School"
          },
          {
            "board": "NA", 
            "level": "BTech",
            "specialization": "Computer Science",
            "yearOfPassing": 2014,
            "institute": "ABC University"
          }
        ]
      }
    },
    {
      ...
    }
  ]
}
```
Status Code !200
```json
{
  "Error": "Error Message"
}
```

###### Response Codes 
TODO

#### GET Candidate Resume
`GET api/v1/resume?candidateId=<candidate_id>`

Returns FileResponse of Candidate's Resume.

###### Response Object
Status Code 200
```text
StreamingHttpResponse Object
```
Status Code !200
```json
{
  "Error": "Error Message"
}
```

###### Response Codes 
TODO