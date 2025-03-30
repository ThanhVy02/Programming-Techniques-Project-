import json


def read_invoices(invoices_path):
    """Đọc và hiển thị thông tin từ file invoices.json."""
    try:
        # Mở file invoices.json và tải nội dung
        with open(invoices_path, "r", encoding="utf-8") as file:
            invoices = json.load(file)

        # Hiển thị từng hóa đơn
        print("Danh sách hóa đơn trong invoices.json:")
        for invoice in invoices:
            print(f"----------------------------")
            print(f"Mã hóa đơn: {invoice['invoice_id']}")
            print(f"Tên khách hàng: {invoice['customer_name']}")
            print(f"Số điện thoại: {invoice['phone_number']}")
            print(f"Ngày đến: {invoice['arrival_date']}")
            print(f"Ngày đi: {invoice['departure_date']}")
            print(f"Số ngày lưu trú: {invoice['days_of_stay']}")
            print(f"Loại phòng: {invoice['room_type']}")
            print(f"Giá phòng mỗi ngày: {invoice['room_price_per_day']} VND")
            print(f"Tổng tiền: {invoice['total_price']} VND")
        print("----------------------------")
    except FileNotFoundError:
        print(f"Không tìm thấy file: {invoices_path}")
    except json.JSONDecodeError:
        print("Dữ liệu trong invoices.json không hợp lệ.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {str(e)}")


# Gọi hàm để đọc file invoices.json
read_invoices("../dataset/invoices.json")
