#!/bin/bash

if [ "$ENV_PROC" == "dev" ]; then
    
    kind delete cluster --name spark-cluster  # Delete the cluster if it exists
    sh kind/kind.sh

    helm repo add spark-operator https://kubeflow.github.io/spark-operator
    helm repo update

    helm install spark-operator spark-operator/spark-operator \
        --namespace spark-operator --create-namespace --wait

    # token criado especificamente para DEV
    kubectl create secret generic github-credentials --from-literal=username=viniciushsantos \
    --from-literal=password=TOKEN \
    -n spark-operator

    # chave ssh criada especificamente para DEV
    kubectl create secret generic github-ssh-key \
    --from-file=id_rsa=/Users/viniciussantos/.ssh/id_rsa \
    -n spark-operator

elif [ "$ENV_PROC" == "prod" ]; then

    helm repo add spark-operator https://kubeflow.github.io/spark-operator
    helm repo update

    helm install spark-operator spark-operator/spark-operator \
        --namespace spark-operator --create-namespace --wait

else
    echo "Error: ENV_PROC must be 'dev' or 'prod'."
    exit 1
fi