#!/usr/bin/env python3 

from raytracer.tuple import *
import time

class Environment:
    def __init__(self, gravity: Vector, wind: Vector):
        self.gravity = gravity
        self.wind = wind

class Projectile:
    def __init__(self, position: Point, velocity: Vector):
        self.position = position
        self.velocity = velocity

def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.wind + env.gravity
    return Projectile(position, velocity)


print("PROJECTILE SIMULATION STARTING")

starting_position = Point(0, 1, 0)
starting_velocity = Vector(1, 1, 0)

gravity = Vector(0, -0.1, 0)
wind = Vector(-0.01, 0, 0)

p = Projectile(starting_position, starting_velocity)
e = Environment(gravity, wind)

while p.position.y >= 0:
    print(f"Position: {p.position}")
    p = tick(e, p)
    time.sleep(0.1)