# Task 1
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

# Task 2
    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password

# Task 3


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

# Task 4

    def show_balance(self):
        print(self.name, "has a balance of: ", self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


# Task 5

    def transfer(self, User, amount):
        print("You are transfering $", amount, "to", User)
        print("Authentication required")
        pinnumber = input(int("Enter your PIN: "))
        if self.pin == pinnumber:
            print("Transer Authorized")
            print("Transfering $" + amount + "to" + User)
            self.balance -= amount
            User.balance += amount
            return True
        else:
            print("Invalid PIN")
            return False

    def request_money(self, user, amount):
        print(" You are requesting $" + amount, "from", user)
        print("User Authentication is required...")
        pinnumber = input("Enter", user.name, "PIN: ")
        print("Request authorized" if (pinnumber == user.pin +
                                       password == self.password)else "Invalid Credentials")


# Task 1 Driver Code
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)


# Task 2 Driver code
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)
# user1.change_name("Bob")
# user1.change_pin(1234)
# user1.change_password("password")
# print(user1.name, user1.pin, user1.password)


# Task 3 driver code
# user1 = BankUser("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password, user1.balance)


# Task 4 Driver code
# user1 = Bankuser("Bob", 1234, "password")
# user1.show_balance()
# user1.deposit(1000)
# user1.show_balance()
# user1.withdraw(500)
# user1.show_balance()

# Task 5 Drive Code
# user1 = Bankuser("Bob", 1234, "password")
# user2 = Bankuser("Amy", 1234, "amypassword")
# user2.deposit(500)
# user2.show_balance()
# user1.show_balance()
# user2.transfer_money(user1, 500)
# user1.show_balance()
# user2.show_balance()
# user1.request_money(user2, 500)
