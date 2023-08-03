from project.robots.base_robot import BaseRobot
from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        # Call the superclass constructor with a capacity of 30 for MainService
        super().__init__(name, capacity=30)

    def details(self):
        # Get the names of all robots in the service
        robot_names = [robot.name for robot in self.robots]

        # Generate the details string based on whether robots exist in the service
        if robot_names:
            robots_string = " ".join(robot_names)
        else:
            robots_string = "none"

        return f"{self.name} Main Service:\nRobots: {robots_string}"

