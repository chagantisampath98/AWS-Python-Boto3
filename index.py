import boto3

# create an object for s3 service
s3_client = boto3.client('s3',
                         aws_access_key_id = 'AKIAZBHAAVKKZW6SDK4G',
                         aws_secret_access_key = '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',
                         region_name = 'us-east-1')

#creation of bucket
#response = s3_client.create_bucket(
#    Bucket='my-python-boto3-s3bucket'
#)
#print(response)

'''
#uploading a file in bucket
response = s3_client.put_object(
    Body=open("index.py", "r").read(),
    Bucket='my-python-boto3-s3bucket',
    Key='index-modified.py'
)
print(response) 

# downloading file from s3 to local
response = s3_client.get_object(
    Bucket='my-python-boto3-s3bucket',
    Key='index-modified.py'
)
data = response.get("Body").read().decode()
file = open("index-modified.py", "w")
file.writelines(data)
file.close()

#list s3 buckets

response = s3_client.list_buckets()
buckets = response.get("Buckets")
print("Total buckets: ", len(buckets))
print(buckets) 

# list objects

response = s3_client.list_objects(
    Bucket='my-python-boto3-s3bucket'
)
objects = response.get("Contents")
print("Total objects: ", len(objects))
print(objects) 

#deleting objects

response = s3_client.delete_object(
    Bucket='my-python-boto3-s3bucket',
    Key='index.py'
)
print(response) '''

#deleting the bucket

response = s3_client.delete_bucket(
    Bucket='my-python-boto3-s3bucket'
)
print(response)