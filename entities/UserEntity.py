class UserEntity():
    id = 0
    username = None
    password = None
    date_joined = None

    def __init__(self):
        id = 0
        username = None
        password = None
        date_joined = None

    def __init__(self, un, pw, dt=datetime.utcnow()):
        # match returns null if the pattern is not matched
        if not valid_username(un):
            raise Exception("Username must begin with a letter and contain only letters, numbers, and underscore")

        # password must contain at least 4 characters
        if not valid_password(pw):
            raise Exception("Password does not meet requirements")

        pw_hash = generate_password_hash(pw + SALT)
        self.id = hash(un)
        self.password = pw_hash
        self.password = pw_hash
        self.date_joined = dt
