from utils import table, response

def handler(event, context):
    todo_id = event["pathParameters"]["id"]
    result = table.get_item(Key={"id": todo_id})
    
    if "Item" not in result:
        return response(404, {"message": f"TODO {todo_id} no existe"})
        
    return response(200, result["Item"])