# musinsub
## 구성
Src : iam_list.py , requirements.txt   
Manifast : manifest/AWS_Credential.yaml musinsub_pod.yaml
## DockerImage
docker:musin:t3

## 실행법
1. AWS_Credential.yaml (Secret 파일에 AWS 키 입력)    
2. kubectl apply -f manifest/*   
3. (Local에서 실행 시)   
   kubectl exec musinsub -- python iam_list.py [파라미터]   
   kubectl cp musinsub:app/iam_list.txt .
4. kubectl exec -it musinsub sh (파드 접근)   
   python iam_list.py [파라미터] && cat iam_list.txt
