from strategy import RouteStrategy


class CarRouteStrategy(RouteStrategy):
    def build_route(self, origin: str, destination: str) -> list[str]:
        return [
            f"Start driving from {origin}",
            "Take the central highway",
            "Exit at city center junction",
            f"Arrive at {destination}",
        ]


class WalkingRouteStrategy(RouteStrategy):
    def build_route(self, origin: str, destination: str) -> list[str]:
        return [
            f"Start walking from {origin}",
            "Walk through the pedestrian boulevard",
            "Cross the central park path",
            f"Arrive at {destination}",
        ]


class PublicTransportStrategy(RouteStrategy):
    def build_route(self, origin: str, destination: str) -> list[str]:
        return [
            f"Walk to nearest metro station from {origin}",
            "Take Line 1 to Central Station",
            "Transfer to Bus #301",
            f"Arrive at {destination}",
        ]


class CyclingRouteStrategy(RouteStrategy):
    def build_route(self, origin: str, destination: str) -> list[str]:
        return [
            f"Start cycling from {origin}",
            "Follow the riverside bike lane",
            "Turn onto Green Avenue cycle track",
            f"Arrive at {destination}",
        ]