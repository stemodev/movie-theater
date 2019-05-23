from db.SQLite import *

def reserve(schedule, amount):
    #Check for available movies for that schedule
    sched_remaining = model.available - amount
    if sched_remaining  < 0:
        print("You can't reserve more than available tickets:{}".format(model.available))
    elif sched_remaining > model.total:
        print("You can't cancel more than total tickets:{}".format(model.total))
        return

    reservation = Reservation(schedule, amount)
    db.SQLite.save_reservation(reservation)