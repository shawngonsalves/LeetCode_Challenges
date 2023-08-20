import heapq
from datetime import datetime
from dateutil import parser

class Customer:
    def __init__(self, Name, email, BirthDate):
        self.Name = Name
        self.email = email
        self.BirthDate = parser.parse(BirthDate)  # Parse the date here

class Event:
    def __init__(self, ID, Name, City, Date):
        self.ID = ID
        self.Name = Name
        self.City = City
        self.Date = parser.parse(Date)  # Parse the date here

class Marketing:
    def __init__(self):
        self.events = []  # Store events here

    def add_event(self, event):
        self.events.append(event)

    def marketing_events(self, customer):
        customer_events = []
        for event in self.events:
            if customer.City == event.City:
                customer_events.append((event.City, event.Date))
        print(f"Hi {customer.Name}")
        for event in customer_events:
            print(f"Event occurring nearby you is: {event[0]} on {event[1].strftime('%Y-%m-%d')}")

    def customer_birthday_events(self, k, customer):
        EventDates = [(event.Date, event.Name) for event in self.events]
        heapq.heapify(EventDates)
        birthday = customer.BirthDate
        customer_birthday_event = []
        while k > 0 and EventDates:
            e_date, e_name = heapq.heappop(EventDates)
            days_to_birthday = (birthday - e_date).days
            if 0 <= days_to_birthday <= 30:
                customer_birthday_event.append((e_name, e_date))  # Fixed order of tuple elements
                k -= 1
        print(f"Hi {customer.Name}, here are {len(customer_birthday_event)} upcoming events closer to your birthday:")
        for event_name, event_date in customer_birthday_event:
            print(f"Event: {event_name}, Date: {event_date.strftime('%Y-%m-%d')}")

# Create instances
customer = Customer("John", "john@gmail.com", "1998-02-03")
marketing = Marketing()

# Add events
marketing.add_event(Event(1, "Event A", "SF", "2023-01-22"))
marketing.add_event(Event(2, "Event AB", "SF2", "2023-04-22"))
marketing.add_event(Event(3, "Event AC", "SF3", "2023-05-22"))
marketing.add_event(Event(4, "Event AD", "SF4", "2023-09-22"))

# Perform marketing tasks
marketing.marketing_events(customer)
marketing.customer_birthday_events(3, customer)