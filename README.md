# samplewebapp
Sample Django Web App

### Design and Architecture
#### Database Schema
![DB Schema Diagram](static/design/DBSchema.png?raw=true "")

#### Events Diagram
#####Version 1 (Implemented Here)
Assumes that PDF Generation and Upload does not consume much time.
![Events Diagram](static/design/EventsDiagramBasic.png?raw=true "")


#####Version 2 (Asynchronous)
Assumes that PDF Generation and Upload will consume much time and hence it handled asynchronously.
![Events Diagram](static/design/EventsDiagram.png?raw=true "")
Queue is AWS SQS.


### API Specifications

#### GET Candidates Data
`GET api/v1/candidates`

Returns the list of interview candidates.
