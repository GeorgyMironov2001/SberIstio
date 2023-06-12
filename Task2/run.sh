#!/bin/bash


istioctl manifest apply --set profile=demo -y
kubectl label namespace default istio-injection=enabled
kubectl apply -f pokemon/flask.yml
kubectl apply -f ingress/ingress.yml
kubectl apply -f egress/egress.yml -f egress/service_entry.yml
kubectl apply -f nginx/service.yml -f nginx/configmap.yml
