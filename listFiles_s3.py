import boto3

def list_files_in_bucket(bucket_name, folder_name):
    s3 = boto3.client('s3')

    try:
        response = s3.list_objects(Bucket=bucket_name, Prefix=folder_name)
        file = [content['Key'] for content in response['Contents']]
        return response
    except Exception as e:
        print(e)
        return []

bucket_name = 'solutions-in-bi'
folder_name = 'pyt'

files = list_files_in_bucket(bucket_name, folder_name)
for file in files:
    print(file) 