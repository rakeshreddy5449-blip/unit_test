
def calculate_delivery_charge(weight):
    if weight <= 0:
        raise ValueError("Weight must be positive")

    return weight * 50


def track_parcel(tracking_id):
    if tracking_id == "CR123":
        return "In Transit"
    return "Parcel Not Found"


def update_status(status):
    return "Parcel Status: " + status
