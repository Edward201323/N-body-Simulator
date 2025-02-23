import math

class PhysicsEngine:
    @staticmethod
    def calculate_acceleration(gravitational_constant, mass, distance):
        if distance == 0:
            return 0
        return (gravitational_constant * mass) / (distance ** 2)

    @staticmethod
    def apply_forces(bodies):
        gravitational_constant = 1 # Can be adjusted accordingly
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

                acceleration_magnitude = PhysicsEngine.calculate_acceleration(gravitational_constant, other_body.mass, distance)

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

                
        
