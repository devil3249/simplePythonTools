import os

class clearScreenCmd:
    """Usage: type 'cls' in your python script or interactive shell running in cmd and watch your screen get cleared"""
    def __repr__(self):
        os.system("cls")
        return '0'

class clearScreenBash:
    """Usage: type 'clear' in your python script or interactive shell running in bash and watch your screen get cleared"""
    def __repr__(self):
        os.system("clear")
        return '0'

cls = clearScreenCmd()
clear = clearScreenBash()
