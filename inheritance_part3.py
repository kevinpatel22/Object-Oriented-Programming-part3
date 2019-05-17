class System:

    bodies = []
    
    def add(self, body):
        if body in System.bodies:
            return
        else:
            System.bodies.append(body)

    def __repr__(self):
        return f'{System.bodies} {self.total_mass()}'
    
    def total_mass(self):
        total_mass = 0
        for body in System.bodies:
            total_mass += body.mass
        return f'{total_mass:.2f}'

class Body(System):

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __repr__(self):
        return f'{self.name} {self.mass}'

class Planet(Body):

    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year
    
    @classmethod
    def all_planets(cls, system):
        planets = []
        for planet in System.bodies:
            if hasattr(planet, 'day') == True:
                planets.append(planet)
        return planets

class Star(Body):

    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type

class Moon(Body):

    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet

milkyway = System()
jupiter = Planet('Jupiter', 10,3, 94)
saturn = Planet('Saturn', 3.4,1.2,30)
neptune = Planet('Neptune', 4, 5, 50)
earth = Planet('Earth', 3.9, 7, 1)
sun = Star('Sun', 100.9,'G2V')
rigel = Star('Rigel', 59, 'B8lab')
earth_moon = Moon('Moon', 1, 7.3, 'Earth')
mars_moon = Moon('Phobos', 1,6.7, 'Mars')
neptune_moon = Moon('Triton', 0.48,4.39,'Neptune')

milkyway.add(jupiter)
milkyway.add(saturn)
milkyway.add(neptune)
milkyway.add(earth)
milkyway.add(sun)
milkyway.add(rigel)
milkyway.add(earth_moon)
milkyway.add(mars_moon)
milkyway.add(neptune_moon)

alphacentauri = System()
a1 = Body('Asteriods', 10)
print(milkyway.bodies)
print(milkyway.total_mass())

print()
print(Planet.all_planets(milkyway))
