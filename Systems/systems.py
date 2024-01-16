import Components.components as components
import sdl2

class MovementSystem:
    def __init__(self):
        mov = components.TransformComponent()
        vel = components.VelocityComponent()
        
def update(dt):
    for entity in get_entities():
        velocity = entity.get_component("VelocityComponent")
        transform = entity.get_component("TransformComponent")

        transform.position.x += velocity.x + dt
        transform.position.y += velocity.y + dt