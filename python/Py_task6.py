import logging
def get_order(order_id):
    try:
        order=db.get(order_id)
        if order is None:
            return{ "success": False,"error": "order not found"},404
        return{"success": True,"data":order},200
    except Exception as e:
        logging.error(f"database error: {e}")
        return{ "success": False,"error": "internal server error"},500

# to run create a fake db and run

'''
import logging
db={
    101:{"id":101, "item":"laptop"},
    102:{"id":102, "item":"phone"}}
def get_order(order_id):
    try:
        order=db.get(order_id)
        if order is None:
            return{ "success": False,"error": "order not found"},404
        return{"success": True,"data":order},200
    except Exception as e:
        logging.error(f"database error: {e}")
        return{ "success": False,"error": "internal server error"},500
print(get_order(101))
print(get_order(999))

'''

''' output
({'success': True, 'data': {'id': 101, 'item': 'laptop'}}, 200)
({'success': False, 'error': 'order not found'}, 404)

'''
