from django.shortcuts import render, redirect
from django.http import JsonResponse, QueryDict
from kubernetes import client, config
import os,hashlib,random
from devops import k8s
# Create your views here.

# Create your views here.

def deployment(request):
    return  render(request, 'workload/deployment.html')

def deployment_api(request):
    # 命名空间选择和命名空间表格使用
    if request.method == "GET":
        code = 0
        msg = ""
        auth_type = request.session.get("auth_type")
        token = request.session.get("token")
        k8s.load_auth_config(auth_type, token)
        apps_api = client.AppsV1Api()
        search_key = request.GET.get("search_key")
        namespace = request.GET.get("namespace")
        data = []
        try:
            for dp in apps_api.list_namespaced_deployment(namespace=namespace).items:
                name = dp.metadata.name
                namespace = dp.metadata.namespace
                replicas = dp.spec.replicas
                available_replicas = ( 0 if dp.status.available_replicas is None else dp.status.available_replicas)
                labels = dp.metadata.labels
                selector = dp.spec.selector.match_labels
                if len(dp.spec.template.spec.containers) > 1:
                    images = ""
                    n = 1
                    for c in dp.spec.template.spec.containers:
                        status = ("运行中" if dp.status.conditions[0].status == "True" else "异常")
                        image = c.image
                        images += "[%s]: %s / %s" % (n, image, status)
                        images += "<br>"
                        n += 1
                else:
                    status = (
                        "运行中" if dp.status.conditions[0].status == "True" else "异常")
                    image = dp.spec.template.spec.containers[0].image
                    images = "%s / %s" % (image, status)

                create_time = dp.metadata.creation_timestamp
                dp = {"name": name, "namespace": namespace, "replicas":replicas,
                             "available_replicas":available_replicas , "labels":labels, "selector":selector,
                             "images":images, "create_time": create_time}
                # 根据搜索值返回数据
                if search_key:
                    if search_key in name:
                        data.append(dp)
                else:
                    data.append(dp)
                code = 0
                msg = "获取数据成功"
        except Exception as e:
            code = 1
            status = getattr(e, "status")
            if status == 403:
                msg = "没有访问权限"
            else:
                msg = "获取数据失败"
        count = len(data)

        page = int(request.GET.get('page',1))
        limit = int(request.GET.get('limit'))
        start = (page - 1) * limit
        end = page * limit
        data = data[start:end]

        res = {'code': code, 'msg': msg, 'count': count, 'data': data}
        return JsonResponse(res)

    elif request.method == "DELETE":
        request_data = QueryDict(request.body)
        name = request_data.get("name")
        namespace = request_data.get("namespace")
        auth_type = request.session.get("auth_type")
        token = request.session.get("token")
        k8s.load_auth_config(auth_type, token)
        apps_api = client.AppsV1Api()
        try:
            apps_api.delete_namespaced_deployment(namespace=namespace, name=name)
            code = 0
            msg = "删除成功."
        except Exception as e:
            code = 1
            status = getattr(e, "status")
            if status == 403:
                msg = "没有删除权限"
            else:
                msg = "删除失败！"
        res = {'code': code, 'msg': msg}
        return JsonResponse(res)


def daemonset(request):
    return render(request, 'workload/daemonset.html')


def statefulset(request):
    return render(request, 'workload/statefulset.html')


def pod(request):
    return render(request, 'workload/pod.html')