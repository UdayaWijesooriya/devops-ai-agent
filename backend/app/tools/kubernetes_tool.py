from app.core.kubernetes_client import KubernetesClient

class KubernetesTool:

    def __init__(self):
        self.client = KubernetesClient()

    def get_pods(self, namespace):
        
        pods = self.client.get_pods(namespace)

        result = []

        for pod in pods:

            result.append(
                {
                    "name": pod.metadata.name,
                    "status": pod.status.phase,
                    "node": pod.spec.node_name
                }
            )
        return result