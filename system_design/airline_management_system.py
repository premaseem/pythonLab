"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

We will focus on the following set of requirements while designing the Airline Management System:

Customers should be able to search for flights for a given date and source/destination airport.
Customers should be able to reserve a ticket for any scheduled flight. Customers can also build a multi-flight itinerary.
Users of the system can check flight schedules, their departure time, available seats, arrival time, and other flight details.
Customers can make reservations for multiple passengers under one itinerary.
Only the admin of the system can add new aircrafts, flights, and flight schedules. Admin can cancel any pre-scheduled flight (all stakeholders will be notified).
Customers can cancel their reservation and itinerary.
The system should be able to handle the assignment of pilots and crew members to flights.
The system should be able to handle payments for reservations.
The system should be able to send notifications to customers whenever a reservation is made/modified or there is an update for their flights.


We have five main Actors in our system:

Admin: Responsible for adding new flights and their schedules, canceling any flight, maintaining staff-related work, etc.
Front desk officer: Will be able to reserve/cancel tickets.
Customer: Can view flight schedule, reserve and cancel tickets.
Pilot/Crew: Can view their assigned flights and their schedules.
System: Mainly responsible for sending notifications regarding itinerary changes, flight status updates, etc.

Here are the top use cases of the Airline Management System:

Search Flights: To search the flight schedule to find flights for a suitable date and time.
Create/Modify/View reservation: To reserve a ticket, cancel it, or view details about the flight or ticket.
Assign seats to passengers: To assign seats to passengers for a flight instance with their reservation.
Make payment for a reservation: To pay for the reservation.
Update flight schedule: To make changes in the flight schedule, and to add or remove any flight.
Assign pilots and crew: To assign pilots and crews to flights.
"""
from enum import Enum

class FlightStatus(Enum):
    ACTIVE, SCHEDULED, DELAYED, DEPARTED, LANDED, IN_AIR, ARRIVED, CANCELLED, DIVERTED, UNKNOWN = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, ABANDONED, SETTLING, SETTLED, REFUNDED = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


class ReservationStatus(Enum):
    REQUESTED, PENDING, CONFIRMED, CHECKED_IN, CANCELLED, ABANDONED = 1, 2, 3, 4, 5, 6


class SeatClass(Enum):
    ECONOMY, ECONOMY_PLUS, PREFERRED_ECONOMY, BUSINESS, FIRST_CLASS = 1, 2, 3, 4, 5


class SeatType(Enum):
    REGULAR, ACCESSIBLE, EMERGENCY_EXIT, EXTRA_LEG_ROOM = 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5, 6


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country

# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.

class Account:
    def __init__(self, id, password, status=AccountStatus.Active):
        self.__id = id
        self.__password = password
        self.__status = status

    def reset_password(self):
        None

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account


class Customer(Person):
    def __init__(self, frequent_flyer_number):
        self.__frequent_flyer_number

    def get_itineraries(self):
        None


class Passenger:
    def __init__(self, name, passport_number, date_of_birth):
        self.__name = name
        self.__passport_number = passport_number
        self.__date_of_birth = date_of_birth

    def get_passport_number(self):
        return self.__passport_number

class Airport:
    def __init__(self, name, address, code):
        self.__name = name
        self.__address = address
        self.__code = code

    def get_flights(self):
        None


class Aircraft:
    def __init__(self, name, model, manufacturing_year):
        self.__name = name
        self.__model = model
        self.__manufacturing_year = manufacturing_year
        self.__seats = []

    def get_flights(self):
        None


class Seat:
    def __init__(self, seat_number, type, seat_class):
        self.__seat_number = seat_number
        self.__type = type
        self.__seat_class = seat_class


class FlightSeat(Seat):
    def __init__(self, fare):
        self.__fare = fare

    def get_fare(self):
        return self.__fare

class WeeklySchedule:
    def __init__(self, day_of_week, departure_time):
        self.__day_of_week = day_of_week
        self.__departure_time = departure_time


class CustomSchedule:
    def __init__(self, custom_date, departure_time):
        self.__custom_date = custom_date
        self.__departure_time = departure_time


class Flight:
    def __init__(self, flight_number, departure, arrival, duration_in_minutes):
        self.__flight_number = flight_number
        self.__departure = departure
        self.__arrival = arrival
        self.__duration_in_minutes = duration_in_minutes

        self.__weekly_schedules = []
        self.__custom_schedules = []
        self.__flight_instances = []


class FlightInstance:
    def __init__(self, departure_time, gate, status, aircraft):
        self.__departure_time = departure_time
        self.__gate = gate
        self.__status = status
        self.__aircraft = aircraft

    def cancel(self):
        None

    def update_status(self, status):
        None


class FlightReservation:
    def __init__(self, reservation_number, flight, aircraft, creation_date, status):
        self.__reservation_number = reservation_number
        self.__flight = flight
        self.__seat_map = {}
        self.__creation_date = creation_date
        self.__status = status

    def fetch_reservation_details(self, reservation_number):
        None

    def get_passengers(self):
        None


class Itinerary:
    def __init__(self, customer_id, starting_airport, final_airport, creation_date):
        self.__customer_id = customer_id
        self.__starting_airport = starting_airport
        self.__final_airport = final_airport
        self.__creation_date = creation_date
        self.__reservations = []

    def get_reservations(self):
        None

    def make_reservation(self):
        None

    def make_payment(self):
        None