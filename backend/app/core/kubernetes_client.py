from kubernetes import client, config

class KubernetesClient:

    def __init__(self):
        # Load the kubernetes configuration from the defult location
        self._initialize_client()

    def _initialize_client(self):
        # Load kubernetes configuration from the defult location
        config.load_kube_config()
        self.core_api = client.CoreV1Api()

    def get_pods(self, namespace):
        # get pods from the kubernetes cluster
        try:
            pods = self.core_api.list_namespaced_pod(
                namespace=namespace
            )
            
            return pods.items
        
        except Exception as error:
            print(f"Error fetching pods: {error}")
            return []
        