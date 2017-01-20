from hashlib import md5
from pyramid.security import Allow, Deny
from pyramid.security import Authenticated

USERS = {'admin':'admin'}
GROUPS = {'admin':['group:admin']}

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])

def hash_password(pw):
    pwhash=md5(pw.encode('utf-8')).hexdigest()
    return pwhash

def check_password(pw, hashed_pw):
    expected_hash = hashed_pw.encode('utf-8')
    return expected_hash==pw.encode('utf-8')

class MyFactory(object):
    def __init__(self, request):
        self.__acl__ = [(Allow, Authenticated, "admin")]