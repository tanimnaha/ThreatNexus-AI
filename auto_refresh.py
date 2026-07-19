from datetime import datetime


def get_last_refresh():

    return datetime.now().strftime("%d %b %Y • %I:%M:%S %p")


def get_refresh_interval():

    return 30


def get_refresh_status():

    return {
        "status": "ACTIVE",
        "interval": get_refresh_interval(),
        "last_refresh": get_last_refresh(),
    }