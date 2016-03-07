# AWS Scripts
###### Collection of small scripts for various AWS purposes

# AWS Regions  
The name of the regions can be found at http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region  
I am also listing them here so that they can be handy  
**US East (N. Virginia)**	us-east-1  
**US West (N. California)**	us-west-1  	
**US West (Oregon)**	us-west-2  	
**EU (Ireland)**	eu-west-1  	
**EU (Frankfurt)**	eu-central-1  
**Asia Pacific (Tokyo)**	ap-northeast-1  
**Asia Pacific (Seoul)**	ap-northeast-2  
**Asia Pacific (Singapore)**	ap-southeast-1  
**Asia Pacific (Sydney)**	ap-southeast-2  
**South America (Sao Paulo)**	sa-east-1  

##findawsinstanceid.py
###### This script can be used to find the EC2 Instance id from the name tag.
**Example Usage**:  
```findec2instanceid.py -a <your aws access key> -s <your aws secret key> -r <aws-region> -n <nametag of the ec2 instance```
