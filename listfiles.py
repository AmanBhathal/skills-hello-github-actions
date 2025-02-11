# -------------------------------------------------------------------------------
# Name:        list_bucket_files.py
# Purpose:     the purpose of the script is to scan an object storage bucket for 
#              filenames and write them (if any) to a text document for review :
#              1.) you will need an .env file for key/value pairs and a constant.py file to successfully run this script
#              2.) connect to S3 Object Storage bucket
#              3.) read object keys to list
#              4.) iterate over list, write filenames to text file
#
# Author:      HHAY, PPLATTEN
#
# Created:     2023-08-09
# Copyright:   (c) OPTIMIZATION TEAM 2023
# Licence:     mine
#
#
# usage: 'list_bucket_files.py
# example: 'list_bucket_files.py'
# -------------------------------------------------------------------------------

# import python libraries
import boto3
import os


# create a client with S3, the access key, secret key, and public endpoint.
s3_client = boto3.client(
    "s3",
     aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
     aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    # endpoint_url=os.getenv('AWS_S3_ENDPOINT'),
    # aws_access_key_id= 'nr-bcwc-env',
    # aws_secret_access_key= 'mvEJNlzgkf8H/H6yQuOc9HtL5QP8NUeKp35MFJlz',
     endpoint_url= 'https://nrs.objectstore.gov.bc.ca',
)

#bucket = os.getenv('AWS_S3_BUCKET')
bucket = 'tneelb'

# placeholder list for the filenames
filenames = []
bucket_name = 'tneelb'  
local_file_path = 'folder/'
# get a list of bucket file names
def get_filenames(s3_client):
    result = s3_client.list_objects_v2(Bucket=bucket)
    for item in result["Contents"]:
        files = item["Key"]
        print(files)
        s3.download_file(bucket,item["Key"], local_file_path)
        filenames.append(files)
        print(f"File downloaded successfully from S3 bucket '{bucket_name}' to '{local_file_path}'")


    return filenames


list_file_names = get_filenames(s3_client)



