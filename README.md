# concierge
AI Concierge


## Getting Started

### Prerequisites
#### Anaconda
1. Download
```
https://www.anaconda.com/download
```

2. Installing


## Protobufs

### To generate protobuf files
```
cd protobuf
python -m grpc_tools.protoc -I . --python_out=../protobuf --grpc_python_out=../protobuf ./concierge.proto
python -m grpc_tools.protoc -I ../protobuf --python_out=. --grpc_python_out=. ../protobuf/concierge.proto

#### where
* -I ../model/protobuf is where to find the protobuf file and its imports
* --python_out=../model is where to put the model file
* --grpc_python_out=../model is where to put the grpc file
```

## Workflow
#### client -> concierge -> service -> rag
####                                -> mocked

## Usage


## Running

