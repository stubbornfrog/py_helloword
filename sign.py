# -*- coding:utf-8 -*-
# @author:zmm
# @date:2023/5/29
import hmac
import base64
import hashlib
from hashlib import *


def hash_hmac_sha1_base64(key, code, sha1):
    hmac_code = hmac.new(key.encode(), code.encode(), sha1).digest()
    print("length of hmac_sha1 is ", len(hmac_code))
    return base64.b64encode(hmac_code).decode()


def hash_hmac_sha1(key, code, sha1):
    hmac_code = hmac.new(key.encode(), code.encode(), sha1)
    return hmac_code.hexdigest()


def hash_hmac_sha256_base64(key, code, sha256):
    hmac_code = hmac.new(key.encode(), code.encode(), sha256).digest()
    print("length of hmac_sha256 is ", len(hmac_code))
    return base64.b64encode(hmac_code).decode()


def hash_hmac_sha256(key, code, sha256):
    hmac_code = hmac.new(key.encode(), code.encode(), sha256)
    return hmac_code.hexdigest()


def hash_hmac_sha3_256_base64(key, code, sha3_256):
    hmac_code = hmac.new(key.encode(), code.encode(), sha3_256).digest()
    print("length of hmac_sha3_256 is ", len(hmac_code))
    return base64.b64encode(hmac_code).decode()


def hash_hmac_sha3_256(key, code, sha3_256):
    hmac_code = hmac.new(key.encode(), code.encode(), sha3_256)
    return hmac_code.hexdigest()


def sha256_base64(message):
    hash_str = hashlib.sha256(message.encode())
    sig = base64.b64encode(hash_str.digest()).decode()
    print("length of sha256_base64 is ", len(sig))
    return sig


# appKey=Jm2c3n0IDyCFYZ9UoAM&timestamp=1685085074&nonce=1234&body={
#     "fileTitle": "OnlyForTest",
#     "filePath": "/mnt/data/remote/805nfs/event_small/temp/Upload/2023-05-25/88bb9ef9f663561a15a2da5b9628a9bd.mp4",
#     "fileType": 3000,
#     "dataWay": 11,
#     "username": "zhumiaomiao",
#     "taskId": "6634",
#     "isAsset": 1
# }

if __name__ == '__main__':
    body = "{    \"fileTitle\": \"OnlyForTest\"," \
           "    \"filePath\": \"/mnt/data/remote/805nfs/event_small/temp/Upload/2023-05-25/88bb9ef9f663561a15a2da5b9628a9bd.mp4\"," \
           "    \"fileType\": 3000," \
           "    \"dataWay\": 11," \
           "    \"username\": \"zhumiaomiao\"," \
           "    \"taskId\": \"6634\"," \
           "    \"isAsset\": 1" \
           "}"
        # body = {
    #     "fileTitle": "OnlyForTest",
    #     "filePath": "/mnt/data/remote/805nfs/event_small/temp/Upload/2023-05-25/88bb9ef9f663561a15a2da5b9628a9bd.mp4",
    #     "fileType": 3000,
    #     "dataWay": 11,
    #     "username": "zhumiaomiao",
    #     "taskId": "6634",
    #     "isAsset": 1
    # }
    code = "appKey=Jm2c3n0IDyCFYZ9UoAM&timestamp=1685085074&nonce=1234&body=" + body
    print(code)
    print(hash_hmac_sha1_base64("2GoTpGE8KHxmmPkheus", code, sha1))
