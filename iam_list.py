import boto3
import datetime , re
import sys
from dateutil.parser import parse

client = boto3.client('iam') 
response_user = client.list_users()
datetime_now = datetime.datetime.now(datetime.timezone.utc) # 'CreateDate': datetime.datetime(2021, 4, 21, 9, 10, 12, tzinfo=tzutc())

try:
    N = int(sys.argv[1])
    f=open('./iam_list.txt', 'w')
    f.write("Access Key Pair가 생성된지 "+str(N)+"시간을 초과하는 IAM USER\n")
    print("Access Key Pair가 생성된지 "+str(N)+"시간을 초과하는 IAM USER")
    for x in response_user['Users']:
        user_name = (x['UserName'])
        response_access = client.list_access_keys(UserName=user_name)
        for y in response_access['AccessKeyMetadata']:
            datetime_obj = (y['CreateDate'])
            if (datetime_now - datetime_obj) > datetime.timedelta(hours=N):
                if (re.match('^AKIA',y['AccessKeyId'])) : 
                    print (y['AccessKeyId'],y['UserName'],str(y['CreateDate']))
                    iamlist = ("Access Key ID:",y['AccessKeyId']," User Name:",y['UserName']," CreateTime:",str(y['CreateDate']), "\n")
                    f.writelines(iamlist)
    f.close()

except:
    print("인자 값을 입력하세요 -- iam_list.py N)")   
