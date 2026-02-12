import boto3

def check_security_groups():
    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups()

    for sg in response['SecurityGroups']:
        for permission in sg['IpPermissions']:
            for ip_range in permission.get('IpRanges', []):
                if ip_range.get('CidrIp') == "0.0.0.0/0":
                    print(f"⚠ Security Group {sg['GroupName']} allows open access on port {permission.get('FromPort')}")

if __name__ == "__main__":
    check_security_groups()
