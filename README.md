# push-container-image-to-docker-registry 

# 概要  
push-container-image-to-docker-registry は、エッジコンピューティング環境において、特定のエッジ端末上の Private Docker Registry に特定のコンテナイメージを追加するマイクロサービスです。  
用途としては、例えばコンテナデプロイメントシステムにおいて、デプロイ先のエッジ端末でデプロイされたコンテナイメージを、デプロイ先のエッジ端末の Private Docker Registry に追加する用途に用いられます。


# 動作環境  
push-container-image-to-docker-registry は、AION のプラットフォーム上での動作を前提としています。   
使用する際は、事前に下記の通り AION の動作環境を用意してください。  
・ Kubernetes  
・ AION のリソース  


