import json

def read_bookings(filename):
    """
    Đọc và hiển thị danh sách đặt phòng từ file JSON.
    :param filename: Đường dẫn tới file JSON.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            bookings = json.load(file)
            print(f"Đã đọc {len(bookings)} đơn đặt phòng từ '{filename}':\n")
            for i, booking in enumerate(bookings, start=1):
                print(f"Đơn đặt phòng {i}:")
                print(f"  Booking ID: {booking['booking_id']}")
                print(f"  Full Name: {booking['full_name']}")
                print(f"  Phone: {booking['phone']}")
                print(f"  Arrival: {booking['arrival']}")
                print(f"  Departure: {booking['departure']}")
                print(f"  Adults: {booking['adults']}")
                print(f"  Children: {booking['children']}")
                print(f"  Room Type: {booking['room_type']}")
                print(f"  Room ID: {booking['room_id']}")
                print("-" * 50)
    except FileNotFoundError:
        print(f"Lỗi: File '{filename}' không tồn tại.")
    except json.JSONDecodeError:
        print(f"Lỗi: File '{filename}' không phải định dạng JSON hợp lệ.")

if __name__ == "__main__":
    # Đường dẫn tới file bookings.json
    filename = "../dataset/bookings.json"
    read_bookings(filename)
