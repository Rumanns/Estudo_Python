"""
 * Project: Traffic Ticket.
 * Objective: To calculate how much will be the traffic ticket.
 * Author: José Valdeir
 * Date: 08/01/2021
"""
vm = int(input('Type the velocity: '))
if vm > 80:
    ticket = (vm-80)*7
    print(f'Speed not allowed. The ticket to pay will be {ticket}.\n'
          f'Thank you.')
