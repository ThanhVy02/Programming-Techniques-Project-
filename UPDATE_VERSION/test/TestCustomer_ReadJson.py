import json

def read_customers(filename):
    """
    Đọc và hiển thị danh sách khách hàng từ file JSON.
    :param filename: Đường dẫn tới file JSON.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            customers = json.load(file)
            print(f"Đã đọc {len(customers)} khách hàng từ '{filename}':\n")
            for i, customer in enumerate(customers, start=1):
                print(f"Khách hàng {i}:")
                print(f"  Booking ID: {customer['booking_id']}")
                print(f"  Full Name: {customer['full_name']}")
                print(f"  Phone: {customer['phone']}")
                print("-" * 40)
    except FileNotFoundError:
        print(f"Lỗi: File '{filename}' không tồn tại.")
    except json.JSONDecodeError:
        print(f"Lỗi: File '{filename}' không phải định dạng JSON hợp lệ.")

if __name__ == "__main__":
    # Đọc và hiển thị khách hàng từ file customers.json
    read_customers("../dataset/customers.json")
