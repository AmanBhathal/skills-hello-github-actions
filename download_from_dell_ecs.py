import boto3
import os

# Dell ECS credentials and endpoint from environment variables
DELL_ECS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
DELL_ECS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
DELL_ECS_ENDPOINT = 'https://nrs.objectstore.gov.bc.ca'
BUCKET_NAME = 'tneelb'  # Replace with your bucket name
OBJECT_KEY = 'BCWC'  # Replace with the object you want to download
LOCAL_FILE_PATH = 'BCWC'  # Local file path for saving the downloaded file

# Initialize the S3 client with Dell ECS endpoint
s3_client = boto3.client('s3', 
                         aws_access_key_id=DELL_ECS_ACCESS_KEY, 
                         aws_secret_access_key=DELL_ECS_SECRET_KEY,
                         endpoint_url=DELL_ECS_ENDPOINT,
                         region_name='us-east-1')  # Adjust region if needed

# Download the file from Dell ECS
try:
    s3_client.download_file(BUCKET_NAME, OBJECT_KEY, LOCAL_FILE_PATH)
    print(f"Downloaded {OBJECT_KEY} from Dell ECS to {LOCAL_FILE_PATH}.")
except Exception as e:
    print(f"Error downloading file: {e}")
