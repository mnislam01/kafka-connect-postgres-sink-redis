# Kafka: Connector and Sink

In this repository we have configured a postgres connector, and a redis sink.

### Build using docker

`
docker-compose build
`

### Run

`
docker-compose up
`

### Configuration files are located in this directory 
`cd kafka/connector`

## Run to configure the postgres connector
`
curl -X POST -H "Accept:application/json" -H "Content-Type: application/json" --data @postgres-source.json http://localhost:8088/connectors
`

## Run to configure the redis sink

`
curl -s -X POST -H 'Content-Type: application/json' --data @redis-sink.json http://localhost:8088/connectors
`

## Browse into the Control Center to monitor the cluster, connector and sink
`
http://localhost:9021
`

## Run to get the list of active connector
`
curl -s -X GET -H 'Content-Type: application/json'  http://localhost:8088/connectors
`
