from db.SQLite import *

def reserve(schedule_id, amount):
    #Check for available movies for that schedule
    sched_available = SQLite.get_available_schedules(schedule_id)
    sched_remaining = sched_free - amount
    sched_total = SQLite.get_schedule().total
    if sched_remaining  < 0:
        print("You can't reserve more than available tickets:{}".format(sched_available))
    elif sched_remaining > sched_total:
        print("You can't cancel more than total tickets:{}".format(sched_total))
        return

    reservation = Reservation(schedule_id, amount)
    SQLite.save_reservation(reservation)

