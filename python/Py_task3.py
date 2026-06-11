import time
from datetime import datetime
def audit(func):
    def wrapper(*args,**kwargs):
        start_time=datetime.now()
        print(f"started {func.__name__}")
        print(f"start time: {start_time}")
        try:
            result=func(*args,**kwargs)
        except Exception as e:
            print(f"error: {e}")
            return None
        end_time=datetime.now()
        print(f"end time: {end_time}")
        duration=end_time-start_time
        print(f"duration: {duration}")

        return result
    return wrapper

@audit
def generate_report(user_id):
    time.sleep(2)
    print("generating report")
    return {"status":"done"}

@audit
def process_payment(payment_id):
    time.sleep(1)
    print("processing payment")
    return {"payment":"success"}

report=generate_report(101)
print(report)

payment=process_payment(500)
print(payment)
