这是一个基于django开发的k8s管理平台
项目架构：Django+Layui+Redis+Mysql+Kubernets
项目功能：
1.登录认证：通过对Kubernets API的客户端提供认证的方式进行调用，可以使用token或者config文件进行登录实现了集成RBAC的Kubernets登录认证。
2.资源展示：Django依据Kubernets API客户端提供的方式编写相对应资源的API接口，获取相应数据，使用Layui从接口获取JSON数据，动态渲染表格。
3.资源创建：通过Django编写的相应资源API，使用Layui调用其API完成相应的资源创建工作。
4.查看YAML：使用Ajax调用导出yaml的接口并把相应的YAML文件内容填充到当前编辑器，对其YAML文件进行查看或编辑操作。
5.容器终端：利用前端库xterm.js模拟shell终端，利用Django框架中的websocket通道实现对容器终端的操作。
6.仪表盘：利用百度开源的ECharts的可视化图标库，对接Kuernets相关API操作，将集群资源信息可视化的展示到前端页面。
效果展示图：https://www.aliyundrive.com/s/abPWxKD8WQq
