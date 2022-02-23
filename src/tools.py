import json
import re


# STATIC HELPER FUNCTIONS

@staticmethod
def toDict(result, row):
    dict(zip([c[0] for c in result.description], row))
    # set the arguments to be parsed out of the request (JSON)
    #

@staticmethod
def valid_username(user_name):
    # returns true if the is alphanumeric (plus _)and starts with a letter
    un = str(user_name)

    # match returns null if the pattern is not matched
    match = re.match('^[A-Za-z]+[A-Za-z0-9_]{2,15}$', un)
    if match is None:
        return False
    return True


@staticmethod
def valid_password(password):
    # returns true if password is at least 4 characters
    pw = str(password)
    return len(pw) >= 4


@staticmethod
def decode_auth_token(auth_token):
    try:
        jwt_payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return jwt_payload['sub']
    except jwt.ExpiredSignatureError:
        return json.dumps({'error': 'Signature expired. Please log in again.'})
    except jwt.InvalidTokenError:
        return json.dumps({'error': 'Invalid token. Please log in again.'})


@staticmethod
def encode_auth_token(user_name):
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': user_name
        }
        return jwt.encode(
            payload, app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e
