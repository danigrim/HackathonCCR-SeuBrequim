import boto3

def up(image_name):

    s3 = boto3.client('s3')
    s3.upload_file(str(image_name),'ccr-hack'
                            '-2020',str(image_name),ExtraArgs={'ContentType':'image/jpeg','ACL':'public-read'})
    s3_url = 'https://ccr-hack-2020.s3.us-east-2.amazonaws.com/'+str(image_name)

    return s3_url