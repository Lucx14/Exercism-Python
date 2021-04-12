class SpaceAge:
    EARTH_ORBITAL_PERIOD_SECONDS = 31557600
    ORBITAL_PERIOD = {
        "MERCURY": 0.2408467,
        "VENUS": 0.61519726,
        "EARTH": 1,
        "MARS": 1.8808158,
        "JUPITER": 11.862615,
        "SATURN": 29.447498,
        "URANUS": 84.016846,
        "NEPTUNE": 164.79132,
    }

    def __init__(self, seconds):
        self.earth_years = seconds / self.EARTH_ORBITAL_PERIOD_SECONDS

    def on_earth(self):
        return self.age_on("EARTH")

    def on_mercury(self):
        return self.age_on("MERCURY")

    def on_venus(self):
        return self.age_on("VENUS")

    def on_mars(self):
        return self.age_on("MARS")

    def on_jupiter(self):
        return self.age_on("JUPITER")

    def on_saturn(self):
        return self.age_on("SATURN")

    def on_uranus(self):
        return self.age_on("URANUS")

    def on_neptune(self):
        return self.age_on("NEPTUNE")

    def age_on(self, planet, R=2):
        return round(self.earth_years / self.ORBITAL_PERIOD[planet], R)
