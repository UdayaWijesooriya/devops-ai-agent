class PodHealthAnalyzer:
    
    def analyze(self, pods):

        report = []

        for pod in pods:

            if pod['status'] == "Running":
                health = "HEALTHY"
                reason = "Pod is Running"

            else:
                health = "UNHEALTHY"
                reason = f"Pod status is {pod['status']}"

            report.append(
                {
                    "name": pod["name"],
                    "health": health,
                    "reason": reason
                }
            )
        return report