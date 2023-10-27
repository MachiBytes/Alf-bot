import json
from json.decoder import JSONDecodeError

def get_user_from_message(message_id):
    with open("data/tickets.json", "r") as file:
        tickets = json.load(file)
        for ticket in tickets:
            if ticket[0] == str(message_id):
                user_id = int(ticket[1])
                return user_id

def remove_ticket(message_id):
    with open("data/tickets.json", "r") as file:
        tickets = json.load(file)
    
    for i, ticket in enumerate(tickets):
        if ticket[0] == str(message_id):
            index = i
            break
    else:
        return
    del tickets[index]

    with open("data/tickets.json", "w") as file:
        json.dump(tickets, file)

def add_ticket(message_id, user_id):
    with open("data/tickets.json", "r") as file:
        tickets = json.load(file)

    tickets.append((str(message_id), str(user_id)))
    with open("data/tickets.json", "w") as file:
        json.dump(tickets, file)