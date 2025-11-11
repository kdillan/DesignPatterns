#In this exercise:

# SessionManager class uses the Singleton pattern to manage user
# login sessions. Each user has a username, password, and role.
# I simulate user logins and logouts, demonstrating the singleton behavior
# of the SessionManager class to maintain a single instance across the application.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SessionManager(metaclass=SingletonMeta):
    def __init__(self):
        self._logged_in_users = {}

    def login(self, username, role):
        if username not in self._logged_in_users:
            self._logged_in_users[username] = role
            print(f"{username} logged in with role: {role}")
        else:
            print(f"{username} is already logged in")

    def logout(self, username):
        if username in self._logged_in_users:
            del self._logged_in_users[username]
            print(f"{username} logged out")
        else:
            print(f"{username} is not logged in")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = "Admin"

class RegularUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = "Regular"

class PremiumUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = "Premium"

if __name__ == "__main__":
    session_manager = SessionManager()

    # Create user instances
    admin = Admin("admin", "admin123")
    regular_user = RegularUser("user1", "user123")
    premium_user = PremiumUser("user2", "user123")

    # Login users
    session_manager.login(admin.username, admin.role)
    session_manager.login(regular_user.username, regular_user.role)
    session_manager.login(premium_user.username, premium_user.role)

    # Attempt to login again
    session_manager.login(admin.username, admin.role)

    # Logout users
    session_manager.logout(admin.username)
    session_manager.logout(regular_user.username)
    session_manager.logout(premium_user.username)
