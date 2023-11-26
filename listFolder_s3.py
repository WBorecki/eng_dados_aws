import boto3

def list_folders(bucket):

    s3_client = boto3.client('s3')

    folders = []

    paginator = s3_client.get_paginator('list_objects_v2')

    for page in paginator.paginate(Bucket=bucket, Delimiter='/'):

        if 'CommonPrefixes' not in page:
            continue

        for folder in page['CommonPrefixes']:
            folders.append(folder['Prefix'])
        
        return folders

bucket = 'solutions-in-bi'

for folders in list_folders(bucket):
    print(folders)