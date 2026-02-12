import boto3

def check_s3_buckets():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']

    for bucket in buckets:
        bucket_name = bucket['Name']
        try:
            acl = s3.get_bucket_acl(Bucket=bucket_name)
            for grant in acl['Grants']:
                if "AllUsers" in str(grant):
                    print(f"⚠ Public bucket detected: {bucket_name}")
        except Exception as e:
            print(f"Error checking bucket {bucket_name}: {e}")

if __name__ == "__main__":
    check_s3_buckets()
