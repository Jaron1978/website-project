import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("website-visitor-counter")


def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={"id": "visitor-count"},
            UpdateExpression="ADD #count :increment",
            ExpressionAttributeNames={
                "#count": "count"
            },
            ExpressionAttributeValues={
                ":increment": 1
            },
            ReturnValues="UPDATED_NEW"
        )

        count = int(response["Attributes"]["count"])

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "https://www.ron-jackson.co.uk"
            },
            "body": json.dumps({
                "count": count
            })
        }

    except Exception as error:
        print(f"Error updating visitor counter: {error}")

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "https://www.ron-jackson.co.uk"
            },
            "body": json.dumps({
                "error": "Unable to update visitor counter"
            })
        }
