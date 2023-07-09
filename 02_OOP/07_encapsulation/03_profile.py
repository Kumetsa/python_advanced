class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if not 4 < len(username) < 16:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if len(password) < 8 or not any(char.isdigit() for char in password) or not any(
                char.isupper() for char in password):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = password

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"".join(["*"] * len(self.password))}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# # profile_with_invalid_username = Profile('Too_long_username', 'Any')

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)

