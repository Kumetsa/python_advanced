from typing import List

from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots: List = []
        self.services: List = []

    def add_service(self, service_type: str, name: str) -> str:
        if service_type not in ["MainService", "SecondaryService"]:
            raise Exception("Invalid service type!")

        if service_type == "MainService":
            service = MainService(name)
            self.services.append(service)

        elif service_type == "SecondaryService":
            service = SecondaryService(name)
            self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        if robot_type not in ["MaleRobot", "FemaleRobot"]:
            raise Exception("Invalid robot type!")

        if robot_type == "MaleRobot":
            robot = MaleRobot(name, kind, price)
            self.robots.append(robot)
        elif robot_type == "FemaleRobot":
            robot = FemaleRobot(name, kind, price)
            self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]

        if isinstance(service, MainService) and isinstance(robot, MaleRobot):
            if len(service.robots) >= service.capacity:
                raise Exception("Not enough capacity for this robot!")

            self.robots.remove(robot)
            service.robots.append(robot)

            return f"Successfully added {robot.name} to {service.name}."

        elif isinstance(service, SecondaryService) and isinstance(robot, FemaleRobot):
            if len(service.robots) >= service.capacity:
                raise Exception("Not enough capacity for this robot!")

            self.robots.remove(robot)
            service.robots.append(robot)

            return f"Successfully added {robot.name} to {service.name}."

        else:
            return "Unsuitable service."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        service = [s for s in self.services if s.name == service_name][0]
        try:
            robot_in_service = [r for r in service.robots if r.name == robot_name][0]
        except IndexError:
            raise Exception("No such robot in this service!")

        # TODO failing test #20 fail

        service.robots.remove(robot_in_service)
        self.robots.append(robot_in_service)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = [s for s in self.services if s.name == service_name][0]
        number_of_robots_fed = 0
        for r in service.robots:
            r.eating()
            number_of_robots_fed += 1

        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        total_price = 0

        for r in service.robots:
            total_price += r.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        info = ""
        for service in self.services:
            info += f"{service.details()}\n"
        return info.strip()
