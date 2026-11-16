
import pytest

from parcel_tracking import (
    calculate_delivery_charge,
    track_parcel,
    update_status
)


def test_delivery_charge():
    assert calculate_delivery_charge(2) == 100


def test_track_parcel():
    assert track_parcel("CR123") == "In Transit"


def test_invalid_tracking_id():
    assert track_parcel("CR999") == "Parcel Not Found"


def test_update_status():
    assert update_status("Delivered") == "Parcel Status: Delivered"


def test_invalid_weight():
    with pytest.raises(ValueError):
        calculate_delivery_charge(0)
