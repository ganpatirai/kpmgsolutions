import requests
import sys
from requests.packages.urllib3 import Retry
import json

def get_instance_metadata():
    url = "http://169.254.169.254/latest/dynamic/instance-identity/document"
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=0.3)
    metadata_adapter = requests.adapters.HTTPAdapter(max_retries=retries)
    session.mount("http://169.254.169.254/", metadata_adapter)
    try:
        req = requests.get(instance_identity_url, timeout=(2, 5))
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError) as err:
        print("Check your EC2Instance (http://169.254.169.254/)")
        sys.exit(1)

    responseJSON = req.json()
    region = responseJSON.get("region")
    accountID = responseJSON.get("accountId")
    imageID = responseJSON.get("imageId")
    aZ = responseJSON.get("availabilityZone")
    privateIP = responseJSON.get("privateIp")
    version = responseJSON.get("version")
    pTime = responseJSON.get("pendingTime")
    arch = responseJSON.get("architecture")
    instanceID = responseJSON.get("instanceId")
    InstanceType = responseJSON.get("instanceType")

    metadata_res = [region, accountID, imageID, aZ, privateIP, version, pTime, arch, instanceID, InstanceType]
    json_result = json.dump(metadata_res)
    return json_result

print(get_instance_metadata())
