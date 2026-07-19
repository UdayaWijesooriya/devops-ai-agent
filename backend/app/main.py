from app.core.kubernetes_client import KubernetesClient

def main():

    kubernetes_client = KubernetesClient()

    pods = kubernetes_client.get_pods(
        namespace="demo"
    )

    for pod in pods:

        print(
            f"Pod Name: {pod.metadata.name}"
        )

        print(
            f"Pod Status: {pod.status.phase}"
        )

        print(
            f"Pod Node: {pod.spec.node_name}"
        )


        print("-------------------------------------")


if __name__ == "__main__":
    main()