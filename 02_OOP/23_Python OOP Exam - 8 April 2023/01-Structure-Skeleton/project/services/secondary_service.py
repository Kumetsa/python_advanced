from project.robots.base_robot import BaseRobot
from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        # Call the superclass constructor with a capacity of 15 for SecondaryService
        super().__init__(name, capacity=15)

    def details(self):
        # Get the names of all robots in the service
        robot_names = [robot.name for robot in self.robots]

        # Generate the details string based on whether robots exist in the service
        if robot_names:
            robots_string = " ".join(robot_names)
        else:
            robots_string = "none"

        return f"{self.name} Secondary Service:\nRobots: {robots_string}"