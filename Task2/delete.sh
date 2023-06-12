#!/bin/bash

kubectl delete deployment flask-service-deployment nginx-service-deployment
kubectl delete se pokeapi-service-entry
kubectl delete vs pokeapi-egressgateway flask-service-ingress
kubectl delete cm nginx-service-cm
kubectl delete svc flask-service nginx-service
kubectl delete gateway pokeapi-egressgateway flask-service-gateway
kubectl delete destinationrule egressgateway-for-pokeapi
kubectl delete -n istio-system secret pokemon-credential

rm -rf ./example_certs1 ./example_certs2

