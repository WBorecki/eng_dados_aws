import boto3

def upload_to_s3(file_name, bucket, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        return True
    except Exception as e:
        print(e)
        return False

bucket= 'solutions-in-bi'
file_name = 'excelFiles/Produtos.xlsx'
object_name = 'data/Produtos.xlsx'

