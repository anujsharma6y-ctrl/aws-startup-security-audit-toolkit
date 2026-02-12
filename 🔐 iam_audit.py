import boto3

def check_iam_users():
    iam = boto3.client('iam')
    users = iam.list_users()['Users']

    risky_users = []

    for user in users:
        attached_policies = iam.list_attached_user_policies(
            UserName=user['UserName']
        )['AttachedPolicies']

        for policy in attached_policies:
            if "AdministratorAccess" in policy['PolicyName']:
                risky_users.append(user['UserName'])

    if risky_users:
        print("⚠ Users with AdministratorAccess:")
        for user in risky_users:
            print("-", user)
    else:
        print("✅ No over-permissive IAM users found")

if __name__ == "__main__":
    check_iam_users()
