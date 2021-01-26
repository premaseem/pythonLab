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


