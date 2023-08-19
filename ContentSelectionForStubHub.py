class Customer:
    def __init__(self, customer):
        self.customer  = customer

        customer.Name = Name
        customer.email = email
        customer.BirthDate = BirthDate





class Event:
    def __init__(self, events):
        self.events = events
        events.ID = ID
        events.Name = Name
        events.City = City
        events.Date = Date



class Marketing:
    def marketingEvents(events):
        customer_events = [] #list of tuple with City and date of event
        for event in events:
            if self.customer.City == event.City:
                customer_cities.append((event.City, event.Date))
        print("Hi ", self.customer.Name)
        for _ in range(len(customer_events)):
            print("Event occuring nearby you is:{event.Name} on {event.Date}")

    def customer_birthday_events(events, k):
        while k > 1:
        EventDates = [event.Date for event.Date in events]
        heapq.heapify(EventDates)



def main():
    events: Event = [(1, "Event A", "SF", parser.parse('2023-01-22')), (2, "Event AB", "SF2", parser.parse('2023-04-22')),
            (3, "Event AC", "SF3", parser.parse('2023-05-22')),
                (4, "Event AD", "SF4", parser.parse('2023-09-22'))]

    customers: Customer = [("John", "john@gmail.com",'1998-02-03')]

    marketingEvents = Marketing()
    Event.marketingEvents(events)
    Event.customer_birthday_events(events, 3)


