from datetime import datetime

#Check Order Data entered by the user
def validate_order(order_id, previous_orders):

    current_year = datetime.now().year

    parts = order_id.split('-')

    if order_id == '':
        result = False
        result_msg = "OrderID cannot be empty."
        return result, result_msg

    if not order_id.startswith("ORD-"):
        result = False
        result_msg = "OrderID must start with 'ORD-'."
        return result, result_msg

    if not parts[1].isdigit():
        result = False
        result_msg = "OrderID year must be numeric."
        return result, result_msg
    else:
        if int(parts[1]) != current_year:
            result = False
            result_msg = f"OrderID year is equal to {current_year}."
            return result, result_msg

    if not parts[2].isdigit():
        result = False
        result_msg = "OrderID sequence must be numeric."
        return result, result_msg

    if len(order_id) != 13:
        result = False
        result_msg = "OrderID format is invalid."
        return result, result_msg    

    for orders in previous_orders:
        if order_id == orders["Order ID"]:
            result = False
            result_msg = f"{order_id} has already been created. Enter a different OrderID!"
            return result, result_msg


    return True, "OrderID is valid."

        


    