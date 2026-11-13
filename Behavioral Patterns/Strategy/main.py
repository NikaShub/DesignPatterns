from navigator import Navigator
from strategies import (
    CarRouteStrategy,
    CyclingRouteStrategy,
    PublicTransportStrategy,
    WalkingRouteStrategy,
)


def main() -> None:
    origin = "Freedom Square"
    destination = "Vake Park"

    navigator = Navigator(CarRouteStrategy())
    navigator.navigate(origin, destination)

    print()
    navigator.set_strategy(WalkingRouteStrategy())
    navigator.navigate(origin, destination)

    print()
    navigator.set_strategy(PublicTransportStrategy())
    navigator.navigate(origin, destination)

    print()
    navigator.set_strategy(CyclingRouteStrategy())
    navigator.navigate(origin, destination)


if __name__ == "__main__":
    main()