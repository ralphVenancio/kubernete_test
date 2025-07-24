import os
from kubernetes import client, config

def update_configmap():
    # Load the kubeconfig
    config.load_incluster_config()

    # Define the API client
    v1 = client.CoreV1Api()

    # Define the name and namespace of the ConfigMap
    configmap_name = "my-config"
    namespace = os.getenv("NAMESPACE", "default")

    # Retrieve the existing ConfigMap
    configmap = v1.read_namespaced_config_map(configmap_name, namespace)

    # Update the values in the ConfigMap
    configmap.data['key1'] = 'new_value1'
    configmap.data['key2'] = 'new_value2'
    configmap.data['key3'] = 'new_value3'

    # Update the ConfigMap in Kubernetes
    v1.patch_namespaced_config_map(configmap_name, namespace, configmap)

if __name__ == "__main__":
    update_configmap()