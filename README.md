# SberIstio
Для запуска


0) minikube start --driver=docker --memory 5000

1) export PATH=$PWD/bin:$PATH - из папки с istio
2) istioctl manifest apply --set profile=demo
3) kubectl label namespace default istio-injection=enabled
4) Запустить secret.sh для создания секрета
5) Запустить run.sh
6) Открыть minikube tunnel в другом окне

Для запроса запустить get_info_about.sh <pokemon или WhoHasAbility> <имя покемона или имя способности>

