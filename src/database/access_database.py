import boto3

session = boto3.Session(profile_name="awscc-admin", region_name="ap-southeast-1")
dynamodb = session.client("dynamodb")


def get_id(gmail):
    response = dynamodb.query(
        TableName="awscc_members",
        IndexName="email-index",
        KeyConditionExpression='email = :val',
        ExpressionAttributeValues={
            ':val': {'S': gmail}
        }
    )
    if not response["Items"]:
        return "Email isn't connected to any record in the database. Please try again."
    return response["Items"][0]["clubId"]["S"]


if __name__ == "__main__":
    print(get_id("markachilesflores2004@gmail.com"))
