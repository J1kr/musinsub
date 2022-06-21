import boto3
import datetime , re
import sys
from dateutil.parser import parse

client = boto3.client('iam') 
response = client.list_users()
datetime_now = datetime.datetime.now(datetime.timezone.utc) # 'CreateDate': datetime.datetime(2021, 4, 21, 9, 10, 12, tzinfo=tzutc())

try:
    N = int(sys.argv[1])
    f=open('./iam_list.txt', 'w')
    f.write("생성된지 "+str(N)+"시간을 초과하는 IAM USER\n")
    print("생성된지 "+str(N)+"시간을 초과하는 IAM USER")
    for x in response['Users']:
        datetime_obj = (x['CreateDate'])
        if (datetime_now - datetime_obj) > datetime.timedelta(hours=N):
            if (re.match('^AIDA',x['UserId'])) :
                print (x['UserId'],x['UserName'],str(x['CreateDate']))
                iamlist = ("Access Key ID:",x['UserId']," User Name:",x['UserName']," CreateTime:",str(x['CreateDate']), "\n")
                f.writelines(iamlist)
    f.close()
except:
    print("인자 값을 입력하세요 -- iam_list.py N)")   