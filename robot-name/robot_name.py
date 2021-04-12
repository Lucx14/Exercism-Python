import random
import string


class Robot:
    robot_names = set()

    def __init__(self):
        self.name = Robot.generate_name()

    def reset(self):
        new_name = Robot.generate_name()
        Robot.robot_names.remove(self.name)
        self.name = new_name

    @classmethod
    def generate_name(cls):
        name = cls.name_prefix() + cls.name_suffix()
        if name not in cls.robot_names:
            cls.robot_names.add(name)
            return name

        return cls.generate_name()

    @staticmethod
    def name_prefix():
        return "".join(random.choice(string.ascii_uppercase) for _ in range(0, 2))

    @staticmethod
    def name_suffix():
        return "".join(str(random.randint(0, 9)) for _ in range(0, 3))
