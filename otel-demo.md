 All services are available via the Frontend proxy: <http://localhost:8080>
  by running these commands:
     kubectl port-forward svc/my-otel-demo-frontendproxy 8080:8080

  The following services are available at these paths once the proxy is exposed:
  Webstore             <http://localhost:8080/>
  Grafana              <http://localhost:8080/grafana/>
  Feature Flags UI     <http://localhost:8080/feature/>
  Load Generator UI    <http://localhost:8080/loadgen/>
  Jaeger UI            <http://localhost:8080/jaeger/ui/>
