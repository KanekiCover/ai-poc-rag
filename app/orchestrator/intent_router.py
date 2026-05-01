from typing import Set


class IntentRouter:
    """Simple intent router for classifying chat messages."""

    METRICS_KEYWORDS: Set[str] = {
        "latency",
        "traffic",
        "packet",
        "packets",
        "usage",
        "bandwidth",
        "utilization",
    }

    @classmethod
    def classify_intent(cls, message: str) -> str:
        """Return intent based on the user message.

        If the message contains any metrics-related keywords, return "metrics".
        Otherwise, return "kb" for knowledge base lookup.
        """
        lowered = message.lower()
        for keyword in cls.METRICS_KEYWORDS:
            if keyword in lowered:
                return "metrics"
        return "kb"
