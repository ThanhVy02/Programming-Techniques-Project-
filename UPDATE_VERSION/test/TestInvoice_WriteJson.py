import json
from datetime import datetime

def calculate_days(arrival, departure):
    """Tính số ngày lưu trú dựa trên ngày đến và ngày đi."""
    date_format = "%Y-%m-%d"
    arrival_date = datetime.strptime(arrival, date_format)
    departure_date = datetime.strptime(departure, date_format)
    return (departure_date - arrival_date).days

def generate_invoices(bookings_path, invoices_path):
    """Tạo file invoices.json từ dữ liệu trong bookings.json."""
    room_prices = {
        "Classic Room": 2400000,
        "Deluxe Room": 2600000,
        "Family Room": 3000000,
        "Master Suite": 5000000
    }

    with open(bookings_path, "r", encoding="utf-8") as file:
        bookings = json.load(file)

    invoices = []
    for booking in bookings:
        days_of_stay = calculate_days(booking["arrival"], booking["departure"])
        room_price = room_prices[booking["room_type"]]
        total_price = days_of_stay * room_price

        invoice = {
            "invoice_id": booking["booking_id"],
            "customer_name": booking["full_name"],
            "phone_number": booking["phone"],
            "arrival_date": booking["arrival"],
            "departure_date": booking["departure"],
            "days_of_stay": days_of_stay,
            "room_type": booking["room_type"],
            "room_price_per_day": room_price,
            "total_price": total_price
        }
        invoices.append(invoice)

    with open(invoices_path, "w", encoding="utf-8") as file:
        json.dump(invoices, file, indent=4, ensure_ascii=False)

# Gọi hàm để tạo file invoices.json
generate_invoices("../dataset/bookings.json", "../dataset/invoices.json")
