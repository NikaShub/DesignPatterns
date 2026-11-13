from strategy import RouteStrategy


class Navigator:
    def __init__(self, strategy: RouteStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: RouteStrategy) -> None:
        self._strategy = strategy

    def navigate(self, origin: str, destination: str) -> list[str]:
        checkpoints = self._strategy.build_route(origin, destination)
        print(f"Route ({self._strategy.__class__.__name__}):")
        for step, checkpoint in enumerate(checkpoints, start=1):
            print(f"  {step}. {checkpoint}")
        return checkpoints