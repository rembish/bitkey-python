#!/bin/bash

cd `dirname $0`

protoc --python_out=../src/ *.proto
