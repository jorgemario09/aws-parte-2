import json
import os
import uuid
import boto3
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")

TABLE_NAME = os.environ.get("TABLE_NAME")
AUDIT_TABLE_NAME = os.environ.get("AUDIT_TABLE_NAME")
TOPIC_ARN = os.environ.get("TOPIC_ARN")

table = dynamodb.Table(TABLE_NAME) if TABLE_NAME else None
audit_table = dynamodb.Table(AUDIT_TABLE_NAME) if AUDIT_TABLE_NAME else None

def response(status_code, body=None):
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST,PUT,DELETE"
    }
    if status_code == 204:
        return {"statusCode": status_code, "headers": headers}
    return {
        "statusCode": status_code,
        "headers": headers,
        "body": json.dumps(body, default=decimal_default)
    }

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError

def parse_body(event):
    try:
        body = event.get("body")
        if not body:
            return None
        return json.loads(body)
    except Exception:
        return None

def publish_event(event_type, data):
    if not TOPIC_ARN:
        return
    event_payload = {
        "eventType": event_type,
        "eventId": str(uuid.uuid4()),
        "occurredAt": data.get("updatedAt", data.get("createdAt")),
        "data": data
    }

    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=json.dumps(event_payload, default=decimal_default),
        MessageAttributes={
            "eventType": {
                "DataType": "String",
                "StringValue": event_type
            }
        }
    )