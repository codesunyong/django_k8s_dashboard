from kubernetes import client, config , watch

# Configs can be set in Configuration class directly or using helper utility
# 基于HTTPS证书
#config.load_kube_config('E:\k8s_project\devops\config')
#v1 = client.CoreV1Api()

# 基于Token认证
configuration = client.Configuration()
configuration.host = "https://192.168.100.10:6443"  # APISERVER地址
configuration.ssl_ca_cert="E:\k8s_project\devops\ca.crt"  # CA证书
configuration.verify_ssl = True   # 启用证书验证
token="eyJhbGciOiJSUzI1NiIsImtpZCI6IllIajdENTlJMjhMYnpmNTZabVNJcTBZV1JfTmppWkJNTjMxbmNyNUNGcmsifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjg4NjM5MDg4LCJpYXQiOjE2ODg2MzU0ODgsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsInNlcnZpY2VhY2NvdW50Ijp7Im5hbWUiOiJkYXNoYm9hcmQtYWRtaW4iLCJ1aWQiOiJkZDEyNzI4MS0wYzI4LTQ5YTYtYmYxZi0zNzQ5OTc2ZjRmZGIifX0sIm5iZiI6MTY4ODYzNTQ4OCwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmVybmV0ZXMtZGFzaGJvYXJkOmRhc2hib2FyZC1hZG1pbiJ9.CvFscBioeICvc0FPdcgCT4zKTKFM-r-lnXNtfPsOTetAV8iE6lnxppUZMAIGkruf_r7VvHNCsgwqXwIDW1jRXnFO-RfgEr295pW8atBKMxowwWVaIo9mpblkuhKGfQvZeGv6CLlmQuTcJTzHfbJfkxZmNe4ZHfw-bNgYg0r2fizY-ZFAdDb44sejNOkLHmiFhyP5fkAEfdqE6MXtqrULhTFM1w-FqAXYNzGw8qCZH9bAUAM2qDUx4Y7TtEyojcgN6Vfqq60XkVIfS62-XiZJQYL79tdZWrzgNUGa17khYW9nmn9uLySPOzRzpbdH-SnTRKROjNq9j749qvdXwYIc_w"
configuration.api_key = {"authorization": "Bearer " + token}  # 指定Token字符串
client.Configuration.set_default(configuration)

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))