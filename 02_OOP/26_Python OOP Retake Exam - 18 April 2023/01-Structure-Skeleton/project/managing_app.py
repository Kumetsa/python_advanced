from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_TYPE = ["PassengerCar", "CargoVan"]

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def _get_user_by_dln(self, dln):
        for user in self.users:
            if user.driving_license_number == dln:
                return user
        return None

    def _get_vehicle_by_lpn(self, lpn):
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == lpn:
                return vehicle
        return None

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self._get_user_by_dln(driving_license_number)
        if user:
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ManagingApp.VALID_TYPE:
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = self._get_vehicle_by_lpn(license_plate_number)
        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        if vehicle_type == "PassengerCar":
            vehicle = PassengerCar(brand, model, license_plate_number)
            self.vehicles.append(vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."
        elif vehicle_type == "CargoVan":
            vehicle = CargoVan(brand, model, license_plate_number)
            self.vehicles.append(vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

        route_id = len(self.routes) + 1
        route = Route(start_point, end_point, length, route_id)
        self.routes.append(route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = self._get_user_by_dln(driving_license_number)
        vehicle = self._get_vehicle_by_lpn(license_plate_number)
        route = [r for r in self.routes if r.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        damaged_vehicles.sort(key=lambda v: (v.brand, v.model))

        if count == 0:
            return f"{count} vehicles were successfully repaired!"

        count_repaired = min(len(damaged_vehicles), count)

        for vehicle in damaged_vehicles[:count_repaired]:
            vehicle.is_damaged = False
            vehicle.battery_level = 100

        return f"{count_repaired} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = list(sorted(self.users, key=lambda x: -x.rating))

        final = [f"*** E-Drive-Rent ***"]
        for user in sorted_users:
            final.append(str(user))

        return '\n'.join(final)
