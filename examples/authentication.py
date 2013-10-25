from requests import Session
from urlparse import urljoin
import json
import hashlib
import hmac

LIVEBLOG_URL = 'http://www.example.org/liveblog'
USERNAME = 'test'
PASSWORD = 'test'

session = Session()

step1_url = urljoin(LIVEBLOG_URL, '/resources/Security/Authentication')
step1 = session.post(
    url=step1_url,
    data={
	'userName': USERNAME,
    }
)
token = json.loads(step1.text)['Token']

sha_password = hashlib.sha512(PASSWORD).hexdigest()
hashed_username = hmac.new(
    USERNAME,
    sha_password,
    hashlib.sha512
).hexdigest()
hashed_token = hmac.new(
    bytes(hashed_username),
    bytes(token),
    hashlib.sha512
).hexdigest()

step2_url = urljoin(LIVEBLOG_URL, '/resources/Security/Authentication/Login')
step2 = session.post(
    url=step2_url,
    data={
	'UserName': USERNAME,
	'Token': token,
	'HashedToken': hashed_token
    }
)
session_key = json.loads(step2.text)['Session']
user = json.loads(step2.text)['User']
