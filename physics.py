import math

class PhysicsEngine:

    @staticmethod
    def apply_forces(bodies):
        gravitational_constant = 1 # Can be adjusted accordingly
        softening_distance = 5
        for body in bodies:
            total_acceleration_x = 0
            total_acceleration_y = 0
            for other_body in bodies:
                if body == other_body:
                    continue
            
                distance_x = other_body.x - body.x
                distance_y = other_body.y - body.y
                distance = math.sqrt(distance_x ** 2 + distance_y **2)

                if distance == 0:
                    continue

                acceleration_magnitude = (gravitational_constant * other_body.mass) / (distance ** 2 + softening_distance ** 2)

                total_acceleration_x += acceleration_magnitude * (distance_x / distance)
                total_acceleration_y += acceleration_magnitude * (distance_y / distance)
        
            body.acceleration_x = total_acceleration_x
            body.acceleration_y = total_acceleration_y

    @staticmethod
    def apply_velocities(bodies):
        for body in bodies:
            body.x += body.velocity_x
            body.y += body.velocity_y

    @staticmethod
    def apply_accelerations(bodies):
        for body in bodies:
            body.velocity_x += body.acceleration_x
            body.velocity_y += body.acceleration_y

                
        
