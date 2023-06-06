# SberIstio
Для запуска


0) minikube start --driver=docker --memory 5000

1) export PATH=$PWD/bin:$PATH - из папки с istio
2) istioctl manifest apply --set profile=demo
3) kubectl label namespace default istio-injection=enabled
4) Открыть minikube tunnel в другом окне

5) Запросы вида curl 127.0.0.1/pokemon/"Имя покемона" и curl 127.0.0.1/WhoHasAbility/"Имя способности"
