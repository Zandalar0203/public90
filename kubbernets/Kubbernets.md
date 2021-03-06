# Команди які необхідні при старті роботи з "Кубіком"

## Робота з PODs

+ __kubectl get pods -o wide__ - команда для виводу списку PODs з розширеними параметрами

```
kubectl get pods -o wide
```

```
NAME                              READY   STATUS    RESTARTS        AGE     IP           NODE       NOMINATED NODE   READINESS GATES
hello-minikube-6ddfcc9757-4h5d8   1/1     Running   1 (3h16m ago)   25h     172.17.0.5   minikube   <none>           <none>
nginx                             1/1     Running   0               3h15m   172.17.0.6   minikube   <none>           <none>
```

+ __kubectl get pods__ - команда для виводу списку PODs

```
kubectl get pods 
NAME                              READY   STATUS    RESTARTS        AGE
hello-minikube-6ddfcc9757-4h5d8   1/1     Running   1 (4h22m ago)   26h
nginx                             1/1     Running   0               4h22m
```

+ __kubectl describe pods nginx__ - команда для опису певного PODa

```
Name:         nginx
Namespace:    default
Priority:     0
Node:         minikube/192.168.59.100
Start Time:   Tue, 28 Dec 2021 20:18:22 +0200
Labels:       run=nginx
Annotations:  <none>
Status:       Running
IP:           172.17.0.7
IPs:
  IP:  172.17.0.7
Containers:
  nginx:
    Container ID:   docker://30086362f6a4d1e51b95dc7fb0d6cb414476857bc242dd03eaeb61ac34937ba6
    Image:          nginx
    Image ID:       docker-pullable://nginx@sha256:366e9f1ddebdb844044c2fafd13b75271a9f620819370f8971220c2b330a9254
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Tue, 28 Dec 2021 20:18:26 +0200
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-nxph4 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-nxph4:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  28s   default-scheduler  Successfully assigned default/nginx to minikube
  Normal  Pulling    27s   kubelet            Pulling image "nginx"
  Normal  Pulled     24s   kubelet            Successfully pulled image "nginx" in 3.210992925s
  Normal  Created    24s   kubelet            Created container nginx
  Normal  Started    24s   kubelet            Started container nginx
```

+ __kubectl run  pods nginx --image nginx__- cтворення POD з образу(image) nginx і надання імені nginx

```
kubectl run  pods nginx --image nginx
pod/pods created
```

+ __kubectl delete pods nginx__ - виделення POD

```
kubectl delete pods nginx
pod "nginx" deleted
```

+ __kubectl edit pod redis__ - редагування запущеного POD .
  
+ __kubectl apply -f pod.yml__ - створення POD  з yml файлу

```
kubectl apply -f ./kubbernets/POD.yml 
pod/redis configured
```

___

## Робота з replicacontroller(rc) & replicaset

+ __kubectl create -f  /home/ts90/DATA/git_reposit/Myprogect/kubbernets/rc_definition.yaml__ - створення реплік-контроллера з файлу .yaml
+ створення реплікасету (replicaset) відбувається таким же чином
  
```
kubectl create -f  /home/ts90/DATA/git_reposit/Myprogect/kubbernets/rc_definition.yaml 
replicationcontroller/myapp-rc created
```

+ __kubectl get replicationcontroller__ - перевірка працюючих реплік-контроллера

```
NAME       DESIRED   CURRENT   READY   AGE
myapp-rc   3         3         3       49s
```

+ __kubectl get pod__ перевірка робочих PODs

```
kubectl get pod
NAME                              READY   STATUS    RESTARTS      AGE
hello-minikube-6ddfcc9757-xr28x   1/1     Running   1 (37m ago)   4d17h
myapp-rc-k45h4                    1/1     Running   0             66s
myapp-rc-kbndl                    1/1     Running   0             66s
myapp-rc-kxhlm                    1/1     Running   0             66s
nginx2                            1/1     Running   0             33m
```

+ kubectl delete rc myapp-rc - видалення PODs за назвою replicacontroller(rc)

```
 kubectl delete rc myapp-rc
replicationcontroller "myapp-rc" deleted
```

### Відмінності replicaset

+ __kubectl create -f  /home/ts90/DATA/git_reposit/Myprogect/kubbernets/replicaset-denition.yml__ - створення реплікасету  з .yml файлу

```
kubectl create -f  /home/ts90/DATA/git_reposit/Myprogect/kubbernets/replicaset-denition.yml 
replicaset.apps/myapp-replicaset created
```

+ __kubectl delete replicaset myapp-rc__-  видалення PODs за назвою replicaset

```
kubectl delete replicaset myapp-rc
replicaset.apps "myapp-rc" deleted
```

+ __kubectl replace -f  /home/ts90/DATA/git_reposit/Myprogect/kubbernets/replicaset-denition.yml__ - перезапуск реплікасету після його(файлу) змінення.

```
kubectl replace -f  /home/ts90/DATA/git_reposit/Myprogect/kubbernets/replicaset-denition.yml 
replicaset.apps/myapp-replicaset replaced
```

+ __kubectl scale --replicas=7 -f ./DATA/git_reposit/Myprogect/kubbernets/replicaset-denition.yml__ - змінення параметрів реплікасету зі зміною файлу .yml

```
kubectl scale --replicas=7 -f ./DATA/git_reposit/Myprogect/kubbernets/replicaset-denition.yml 
replicaset.apps/myapp-replicaset scaled
```

+ __kubectl scale --replicas=9 replicaset myapp-replicaset__ - зміна параметру реплікасету на льоту (без збереження в файл)

```
kubectl scale --replicas=9 replicaset myapp-replicaset
replicaset.apps/myapp-replicaset scaled
```

___

### Команди для Deployment

+ __kubectl create -f deploy.yml__ - створення deployment файлу .yml

```
kubectl create -f deploy.yml 
deployment.apps/myapp-deloy created
```

+ __kubectl get deploy__ - інформація про деплоймент

```  
kubectl get deploy 
NAME          READY   UP-TO-DATE   AVAILABLE   AGE
myapp-deloy   3/3     3            3           2m23s
```

+ kubectl apply -f deploy.yml  - оновити деплоймент по замовчуванню використовується стратегія  rollingupdate

```
kubectl apply -f deploy.yml 
deployment.apps/myapp-deloy configured
```

+ __kubectl set image deployment/myapp-deloy  ts90-nginx-containers=nginx:1.7.1__ - зміна образу(заміна на іншу версію) в деплойменті на льоту (без збреження у файл)

```
kubectl set image deployment/myapp-deloy  ts90-nginx-containers=nginx:1.7.1
deployment.apps/myapp-deloy image updated
```

+ __kubectl  scale deploy myapp-deloy --replicas=5__ - встановлення(масштабування) PODs в деплої в кількості 5 без зюереження в файл .

```
kubectl  scale deploy myapp-deloy --replicas=5
deployment.apps/myapp-deloy scaled
```

+ kubectl rollout status deploy/myapp-deploy - перегляд статусу роботи деплоймента

```
kubectl rollout status deploy/myapp-deploy
deployment "myapp-deploy" successfully rolled out
```

+ __kubectl rollout history deploy/myapp-deploy__ - перегляд істороії деплойменту

```
kubectl rollout history deploy/myapp-deploy
deployment.apps/myapp-deploy 
REVISION  CHANGE-CAUSE
1         <none>
2         <none>
```

+ kubectl rollout undo deploy/myapp-deploy - відкат до попередньої версії(REVISION) деплойменту

```
kubectl rollout undo deploy/myapp-deploy
deployment.apps/myapp-deploy rolled back
```
+ __kubectl get all__ -вся інфа про PODs реплікасети та деплої
```
kubectl get all
NAME                                READY   STATUS              RESTARTS   AGE
pod/myapp-deploy-774dff58f5-29gh4   1/1     Running             0          4m5s
pod/myapp-deploy-774dff58f5-2x9vl   1/1     Terminating         0          3m52s
pod/myapp-deploy-774dff58f5-lxfgq   1/1     Running             0          4m9s
pod/myapp-deploy-774dff58f5-p584n   1/1     Running             0          3m52s
pod/myapp-deploy-78856849c7-682wd   0/1     ContainerCreating   0          1s
pod/myapp-deploy-78856849c7-dgdrr   0/1     ContainerCreating   0          4s
pod/myapp-deploy-78856849c7-rb85z   0/1     ContainerCreating   0          4s
pod/myapp-deploy-78856849c7-wxs9r   1/1     Running             0          4s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   13d

NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/myapp-deploy   4/5     4            4           11m

NAME                                      DESIRED   CURRENT   READY   AGE
replicaset.apps/myapp-deploy-774dff58f5   3         3         3       4m9s
replicaset.apps/myapp-deploy-78856849c7   4         4         1       11m
ts90@ts90:~/DATA/git_reposit/zandalar/public90/kubbernets/Deployment$ kubectl get all
NAME                                READY   STATUS    RESTARTS   AGE
pod/myapp-deploy-78856849c7-682wd   1/1     Running   0          19s
pod/myapp-deploy-78856849c7-dgdrr   1/1     Running   0          22s
pod/myapp-deploy-78856849c7-h8vz8   1/1     Running   0          16s
pod/myapp-deploy-78856849c7-rb85z   1/1     Running   0          22s
pod/myapp-deploy-78856849c7-wxs9r   1/1     Running   0          22s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   13d

NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/myapp-deploy   5/5     5            5           11m

NAME                                      DESIRED   CURRENT   READY   AGE
replicaset.apps/myapp-deploy-774dff58f5   0         0         0       4m27s
replicaset.apps/myapp-deploy-78856849c7   5         5         5       11m
```