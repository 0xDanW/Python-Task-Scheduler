import schedule
from schedule import every, repeat
import time as tm
from datetime import time, timedelta, datetime



# @repeat(every(5).seconds, message = "Hai Ho")
# @repeat(every(2).seconds, message = "Hai Hooooo")
# def job(message):
#     print("Hello World! Message is: " + message)

# # j = schedule.every(5).seconds.do(job)
# # schedule.every().second.do(job)
# # schedule.every().day.at("17:30").do(job)
# # schudule.every().minute.at(":40").do(job)                 --> run at every 40s
# # schudule.every().hour.until(time(11, 33, 42)).do(job)     --> Run until specific time   
# # schudule.every().hour.until(timedelta(hours=8)).do(job)   --> Run for 8 hours
# # schedule.every(1).to(5).seconds.do(job)                   --> Random

# # counter = 0


# schedule.every().second.do(job, message = "HELLO")

# while True:
#     schedule.run_pending()
#     tm.sleep(1)
#     # counter += 1
#     # if counter == 10:
#     #     schedule.cancel_job(j)



# BreaK Reminder Example

@repeat(every(30).minutes)
def break_reminder():
    print("Take a break! You have been working for 30 minutes!")

while True:
    schedule.run_pending()
