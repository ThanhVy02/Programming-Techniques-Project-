import json
import random
from datetime import timedelta, date

# Danh sách giá phòng
ROOM_PRICES = {
    "Classic Room": 2400000,
    "Deluxe Room": 2600000,
    "Family Room": 3000000,
    "Master Suite": 5000000
}


def load_rooms(filename):
    """
    Đọc dữ liệu danh sách phòng từ file JSON.
    :param filename: Đường dẫn đến file JSON.
    :return: Danh sách phòng.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def generate_bookings(rooms):
    """
    Tạo danh sách đặt phòng từ các phòng đã được đặt (status: 'unavailable').
    :param rooms: Danh sách phòng.
    :return: Danh sách đơn đặt phòng.
    """
    bookings = []
    vietnamese_names = ["Nguyễn Văn A", "Trần Thị B", "Lê Văn C", "Hoàng Minh D", "Phạm Văn E",
                        "Đinh Thị F", "Ngô Minh G", "Huỳnh Văn H", "Lý Thị I", "Vũ Văn J",
                        "Nguyễn Thị K", "Phạm Minh L", "Lê Thị M", "Bùi Văn N", "Hồ Thị O",
                        "Đào Văn P", "Đặng Thị Q", "Trịnh Văn R", "Nguyễn Minh S", "Trần Văn T"]

    booking_id_counter = 1  # Đánh số booking ID bắt đầu từ 1

    for room in rooms:
        if room["status"] == "unavailable":  # Chỉ xử lý các phòng đã được đặt
            full_name = vietnamese_names[booking_id_counter % len(vietnamese_names)]  # Lấy tên luân phiên
            phone = f"09{random.randint(100000000, 999999999)}"  # Số điện thoại ngẫu nhiên

            # Tạo ngày đến và ngày đi ngẫu nhiên
            arrival = date(2025, 5, random.randint(1, 20))
            departure = arrival + timedelta(days=random.randint(1, 5))  # Số ngày ở từ 1 đến 5

            # Tính giá phòng
            number_of_days = (departure - arrival).days
            room_price_per_day = ROOM_PRICES[room["room_type"]]
            total_price = number_of_days * room_price_per_day

            # Tạo thông tin booking
            booking = {
                "booking_id": f"{booking_id_counter:05}",  # ID 5 chữ số
                "full_name": full_name,
                "phone": phone,
                "arrival": arrival.strftime("%Y-%m-%d"),
                "departure": departure.strftime("%Y-%m-%d"),
                "adults": random.randint(1, 4),  # Số người lớn từ 1 đến 4
                "children": random.randint(0, 2),  # Số trẻ em từ 0 đến 2
                "room_type": room["room_type"],
                "room_id": room["room_id"],
                "total_price": total_price  # Tổng giá
            }
            bookings.append(booking)
            booking_id_counter += 1  # Tăng ID cho lần tiếp theo

    return bookings


def write_bookings(filename, bookings):
    """
    Ghi danh sách đặt phòng vào file JSON.
    :param filename: Đường dẫn tới file JSON.
    :param bookings: Danh sách đơn đặt phòng.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(bookings, file, ensure_ascii=False, indent=4)
    print(f"Danh sách đặt phòng đã được ghi vào {filename}.")


if __name__ == "__main__":
    # Đọc danh sách phòng từ file rooms.json
    rooms = load_rooms("../dataset/rooms.json")

    # Tạo danh sách đặt phòng
    bookings = generate_bookings(rooms)

    # Ghi danh sách đặt phòng vào file bookings.json
    write_bookings("../dataset/bookings.json", bookings)
