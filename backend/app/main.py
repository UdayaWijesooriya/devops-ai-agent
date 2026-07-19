from app.tools.kubernetes_tool import KubernetesTool

def main():

    kubernetes_tool = KubernetesTool()

    pods = kubernetes_tool.get_pods(
        namespace="demo"
    )

    for pod in pods:

        print(
            f"Pod Name: {pod['name']}"
        )

        print(
            f"Pod Status: {pod['status']}"
        )

        print(
            f"Pod Node: {pod['node']}"
        )


        print("-------------------------------------")


if __name__ == "__main__":
    main()