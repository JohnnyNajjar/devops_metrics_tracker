#!/bin/bash
docker build -t spark-metrics .
docker run --rm spark-metrics
