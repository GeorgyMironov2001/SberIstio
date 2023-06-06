#!/bin/bash
kubectl apply -f flask/flask.yaml
kubectl apply -f flask/gateway.yaml
kubectl apply -f flask/external.yaml
kubectl apply -f nginx/nginx.yaml
kubectl apply -f nginx/gateway.yaml
