python3 -m venv venv 
source venv/bin/activate
brew install openjdk@11

docker build -t viniciusdossantos21/flow-processor:0.0.3 .
docker push viniciusdossantos21/flow-processor:0.0.3

docker run --rm -it viniciusdossantos21/flow-processor:0.0.3 bash

kubectl delete sparkapplications --all -n default
kubectl delete sparkapplications --all -n default
