class Transport:
    """Базовый класс для всех транспортных средств."""
    def move(self):
        pass


class WaterTransport(Transport):
    """Водный транспорт."""
    def sail(self):
        pass


class Ship(WaterTransport):
    def carry_cargo(self):
        pass


class Boat(WaterTransport):
    def row(self):
        pass


class Submarine(WaterTransport):
    def dive(self):
        pass


class AirTransport(Transport):
    """Воздушный транспорт."""
    def fly(self):
        pass


class Aviation(AirTransport):
    """Авиация (самолёты, вертолёты)."""
    def take_off(self):
        pass


class Airplane(Aviation):
    pass


class Helicopter(Aviation):
    def hover(self):
        pass


class LighterThanAir(AirTransport):
    """Воздухоплавание (дирижабли, воздушные шары)."""
    def ascend(self):
        pass


class Airship(LighterThanAir):
    pass


class HotAirBalloon(LighterThanAir):
    pass


class GroundTransport(Transport):
    """Наземный транспорт."""
    def move_on_ground(self):
        pass


class RailTransport(GroundTransport):
    """Железнодорожный транспорт."""
    def run_on_tracks(self):
        pass


class Train(RailTransport):
    pass


class RoadTransport(GroundTransport):
    """Автомобильный транспорт."""
    def drive(self):
        pass


class Car(RoadTransport):
    pass


class Bicycle(GroundTransport):
    def pedal(self):
        pass


class AnimalPoweredTransport(GroundTransport):
    """Транспорт, движимый животными."""
    def harness(self):
        pass


class HorseDrawnCarriage(AnimalPoweredTransport):
    pass


class SpaceTransport(Transport):
    """Космический транспорт."""
    def launch(self):
        pass

    def orbit(self):
        pass


class Rocket(SpaceTransport):
    pass


class SpaceShuttle(SpaceTransport):
    def land_horizontally(self):
        pass


class Satellite(SpaceTransport):
    def stabilize(self):
        pass
