from utils import table, response

def handler(event, context):
    result = table.scan()
    items = result.get("Items", [])
    return response(200, items)