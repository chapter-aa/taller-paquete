import pandas as pd

from hotel_booking.preprocessing import (
    add_arrival_month,
    add_total_nights,
    clean_column_names,
)


def test_clean_column_names() -> None:
    df = pd.DataFrame(columns=["lead time", "room-type", "Booking_ID"])

    result = clean_column_names(df)

    assert list(result.columns) == ["lead_time", "room_type", "Booking_ID"]


def test_add_total_nights() -> None:
    df = pd.DataFrame(
        {"number_of_weekend_nights": [1, 0], "number_of_week_nights": [2, 3]}
    )
    result = add_total_nights(df)
    assert list(result["total_nights"]) == [3, 3]


def test_add_arrival_month() -> None:
    df = pd.DataFrame(
        {"date_of_reservation": ["1/15/2018", "2018-2-29"], "lead_time": [20, 0]}
    )

    result = add_arrival_month(df)

    assert list(result["arrival_month"]) == [2, 3]
