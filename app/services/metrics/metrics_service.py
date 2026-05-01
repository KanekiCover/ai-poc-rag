class MetricsService:
    """Mock metrics service for intent-based routing.

    This service returns deterministic mock responses for metrics questions
    and is a placeholder for future database-backed metrics integration.
    """

    def generate_metrics_response(self, message: str, user_id: str) -> str:
        """Generate a simple mock response for metrics-related questions."""
        lowered = message.lower()

        if "latency" in lowered:
            return (
                f"Mock latency insight for user {user_id}: "
                "Your current latency is simulated at 15 ms over the last hour. "
                "This is mock data and will be replaced with real metrics DB integration later."
            )

        if any(keyword in lowered for keyword in ["traffic", "bandwidth", "utilization"]):
            return (
                f"Mock traffic insight for user {user_id}: "
                "Network traffic is simulated at 72% of capacity and bandwidth usage is stable. "
                "This is mock data and will be replaced with real metrics DB integration later."
            )

        if any(keyword in lowered for keyword in ["packet", "packets"]):
            return (
                f"Mock packet insight for user {user_id}: "
                "Packet counts are simulated at 1.2M packets in the last 30 minutes. "
                "This is mock data and will be replaced with real metrics DB integration later."
            )

        return (
            f"Mock metrics response for user {user_id}: "
            "I detected a metrics-related request but do not have real database access yet. "
            "This is mock data and will be replaced with real metrics DB integration later."
        )
