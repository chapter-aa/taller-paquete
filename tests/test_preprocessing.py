import pandas as pd

from hotel_booking.preprocessing import add_arrival_month, clean_column_names


def test_clean_column_names() -> None:
    df = pd.DataFrame(columns=["lead time", "room-type", "Booking_ID"])

    result = clean_column_names(df)

    assert list(result.columns) == ["lead_time", "room_type", "Booking_ID"]


def test_add_arrival_month() -> None:
    df = pd.DataFrame(
        {"date_of_reservation": ["1/15/2018", "2018-2-29"], "lead_time": [20, 0]}
    )

    result = add_arrival_month(df)

    assert list(result["arrival_month"]) == [2, 3]
