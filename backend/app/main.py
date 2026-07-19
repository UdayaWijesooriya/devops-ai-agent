from app.tools.kubernetes_tool import KubernetesTool
from app.analyzers.pod_health_analyzer import PodHealthAnalyzer


def main():

    kubernetes_tool = KubernetesTool()

    analyzer = PodHealthAnalyzer()

    pods = kubernetes_tool.get_pods(
        namespace="demo"
    )

    report = analyzer.analyze(
        pods
    )

    for report in report:

        print("-------------------------------------")

        print(
            f"Application: {report['name']}"
        )

        print(
            f"Health: {report['health']}"
        )

        print(
            f"Reason: {report['reason']}"
        )

        print("-------------------------------------")


if __name__ == "__main__":
    main()