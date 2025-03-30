import json

def load_bookings(filename):
    """
    Đọc dữ liệu danh sách đặt phòng từ file JSON.
    :param filename: Đường dẫn tới file JSON chứa thông tin đặt phòng.
    :return: Danh sách các đơn đặt phòng.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def write_customers(bookings, filename):
    """
    Ghi dữ liệu khách hàng vào file JSON từ thông tin đặt phòng.
    :param bookings: Danh sách đặt phòng (liên kết với khách hàng).
    :param filename: Đường dẫn tới file JSON cần ghi.
    """
    customers = []

    for booking in bookings:
        # Tạo đối tượng Customer khớp với thông tin trong Booking
        customer = {
            "booking_id": booking["booking_id"],
            "full_name": booking["full_name"],
            "phone": booking["phone"]
        }
        customers.append(customer)

    # Ghi dữ liệu vào file JSON
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(customers, file, ensure_ascii=False, indent=4)

    print(f"Danh sách khách hàng đã được ghi vào '{filename}'.")

if __name__ == "__main__":
    # Đọc dữ liệu từ file bookings.json
    bookings = load_bookings("../dataset/bookings.json")

    # Ghi khách hàng vào file customers.json
    write_customers(bookings, "../dataset/customers.json")
