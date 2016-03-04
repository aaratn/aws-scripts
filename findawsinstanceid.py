try:
    import boto3
except:
    print "You must install boto3 module in order to run this script"
import sys
from boto3.session import Session
import argparse
parser = argparse.ArgumentParser(description="This script can be used to find \
                                EC2 instance id from AWS Name Tags")
parser.add_argument('-a', '--akey', dest='akey', help='AWS Access Key',
                    required=True)
parser.add_argument('-s', '--skey', dest='skey', help='AWS Secret Key',
                    required=True)
parser.add_argument('-r', '--region', dest='region', help='AWS Region',
                    required=True)
parser.add_argument('-n', '--name', dest='name', help='AWS Instance Name',
                    required=True)
if len(sys.argv) < 4:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()
akey = args.akey
skey = args.skey
region = args.region
name = args.name
try:
    session = Session(aws_access_key_id=str(akey),
                      aws_secret_access_key=str(skey))
except:
    sys.exc_info()


def findawsinstanceid(servername):
    try:
        client = session.client('ec2', region)
        response = client.describe_instances(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': [
                        servername,
                        ]
                        }
                ]
            )
        for r in response.get('Reservations'):
            for q in r['Instances']:
                return q['InstanceId']
    except Exception as ex:
        print ex
instanceid = findawsinstanceid(name)
if instanceid is not None:
    print "\n", instanceid
