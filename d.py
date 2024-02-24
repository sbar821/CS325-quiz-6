# Imagine you're developing a web application and need a robust logging system.
# Currently, your code directly utilizes a specific logging library like logging, loguru,
# Google_auth, throughout your application.
# Question:
# WAP to adhere to the Dependency Inversion Principle (DIP) in regards to logging.
# Focus on the following aspects and Name your program d.py.:
# ● Tight coupling with a specific logging library: Can you decouple your
# application logic from the chosen library, making it easier to switch or extend
# logging capabilities later?
# ● Testing concerns: How can DIP improve the testability of your application's
# logging functionality?
# ● Enhancing flexibility: Can you introduce mechanisms to dynamically configure
# logging behavior based on different environments or user preferences?

from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def debug(self, message):
        print("successfully debugged")

    @abstractmethod
    def info(self, message):
        print("you are using ... logging library!")

    @abstractmethod
    def warning(self, message):
        print("warning, something is wrong")

    @abstractmethod
    def error(self, message):
        print("error found!")

class Application:
    def __init__(self, logger: Logger):
        self.logger = logger

    def perform_action(self):
        # Example application logic
        self.logger.debug("Performing action")
        # Perform action
        self.logger.info("Action performed successfully")