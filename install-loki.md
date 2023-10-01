helm repo add grafana <https://grafana.github.io/helm-charts>
helm repo update
helm install --values values-loki.yaml loki grafana/loki
