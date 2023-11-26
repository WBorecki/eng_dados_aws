import boto3
import pandas as pd

s3_client = boto3.client('s3')

s3_client.download_file('solutions-in-bi',
                        'data/Metas.xlsx',
                        'excelFiles/Metas_S3.xlsx') 

##df = pd.read_excel('excelFiles/Metas_S3.xlsx')
##print(df)
