# samplewebapp
Sample Django Web App

### Design and Architecture
#### Database Schema
![DB Schema Diagram](static/design/DBSchema.png?raw=true "")

#### Events Diagram
![Events Diagram](static/design/EventsDiagram.png?raw=true "")
Queue is AWS SQS.


### API Specifications

#### GET Candidates Data
`GET api/v1/candidates`

Returns the list of interview candidates.
