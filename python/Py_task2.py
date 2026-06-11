import logging
logging.basicConfig(filename="payment.log",
                    level=logging.INFO,
                    format="%(asctime)s -%(levelname)s -%(message)s")
def call_gateway(payment_id):
    raise Exception("gateway timeout")
def process_payment(payment_id):
    try:
        
        logging.info(f"processing payment {payment_id}")
        result=call_gateway(payment_id)
        logging.info(f"gateway response: {result}")
        return result
    except Exception as e:
        logging.error(f"payment failed: {e}")
process_payment(101)
