#!/bin/bash

brew install kind 
brew upgrade kind 
kind create cluster --name spark-cluster --config kind/kind-config.yaml
docker ps

