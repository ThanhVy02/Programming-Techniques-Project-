import json
import os

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication

from ui.confirm_and_thanks.confirm_and_thanks import Ui_Dialog
from ui.customer_management.customer_management import Ui_CustomerManagement
from ui.room_list.room_list import Ui_RoomListMainWindow
from ui.booking_screen.booking_screen import Ui_BookingWindow
from ui.home_screen.home_screen import Ui_MainWindow


class Booking_Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonBookNow_Home.clicked.connect(self.list_room)

    def list_room(self):
        self.MainWindow.close()
        self.listWindow = QMainWindow()
        self.uiList = Ui_RoomListMainWindow()
        self.uiList.setupUi(self.listWindow)
        self.listWindow.show()

        # Gắn các nút đặt phòng
        self.uiList.pushButtonBookClassic.clicked.connect(
            lambda: self.open_booking_window("CLASSIC ROOM"))
        self.uiList.pushButtonBookDeluxe.clicked.connect(
            lambda: self.open_booking_window("DELUXE ROOM"))
        self.uiList.pushButtonBookFamily.clicked.connect(
            lambda: self.open_booking_window("FAMILY ROOM"))
        self.uiList.pushButtonBookMaster.clicked.connect(
            lambda: self.open_booking_window("MASTER SUITE"))
        self.listWindow.show()

    def open_booking_window(self, selected_room_type):
        self.bookingWindow = QMainWindow()
        self.uiBooking = Ui_BookingWindow()
        self.uiBooking.setupUi(self.bookingWindow)

        # Gán loại phòng vào ComboBox
        index = self.uiBooking.comboBoxRoom.findText(selected_room_type)
        if index != -1:
            self.uiBooking.comboBoxRoom.setCurrentIndex(index)

        # Gắn sự kiện nút BOOK NOW
        self.uiBooking.pushButtonBookNow.clicked.connect(self.save_booking_data)
        self.bookingWindow.show()

    def generate_new_booking_id(self, path="../dataset/booking.json"):
        """Tạo booking_id mới dựa trên dữ liệu hiện có"""
        if not os.path.exists(path):
            return "00001"

        with open(path, "r", encoding="utf-8") as f:
            try:
                bookings = json.load(f)
            except json.JSONDecodeError:
                bookings = []

        if not bookings:
            return "00001"

        last_id = max([
            int(b["booking_id"]) for b in bookings
            if "booking_id" in b and b["booking_id"].isdigit()
        ])
        return str(last_id + 1).zfill(5)

    def save_booking_data(self):
        # Lấy thông tin từ form
        full_name = self.uiBooking.lineEditFullName.text()
        phone_number = self.uiBooking.lineEditPhone.text()
        arrival = self.uiBooking.dateEditArrival.date().toString("yyyy-MM-dd")
        departure = self.uiBooking.dateEditDeparture.date().toString("yyyy-MM-dd")
        adults = self.uiBooking.spinBoxAdults.value()
        children = self.uiBooking.spinBoxChildren.value()
        room_type = self.uiBooking.comboBoxRoom.currentText()

        if not full_name or not phone_number:
            QMessageBox.warning(self.bookingWindow, "Thiếu thông tin", "Vui lòng nhập đầy đủ họ tên và số điện thoại.")
            return

        # Tạo booking_id mới nối tiếp
        booking_file = "../dataset/bookings.json"
        if os.path.exists(booking_file):
            with open(booking_file, 'r', encoding='utf-8') as f:
                try:
                    booking_list = json.load(f)
                    last_id = max([int(item['booking_id']) for item in booking_list]) if booking_list else 0
                except Exception:
                    booking_list = []
                    last_id = 0
        else:
            booking_list = []
            last_id = 0

        new_id = last_id + 1
        booking_id = f"{new_id:05d}"  # Định dạng 5 chữ số, ví dụ: 00023

        # Tạo dữ liệu mới
        customer_data = {
            "booking_id": booking_id,
            "full_name": full_name,
            "phone": phone_number
        }

        booking_data = {
            "booking_id": booking_id,
            "full_name": full_name,
            "phone_number": phone_number,
            "arrival_date": arrival,
            "departure_date": departure,
            "adults": adults,
            "children": children,
            "room_type": room_type
        }

        # Lưu dữ liệu
        self.append_to_json("../dataset/customers.json", customer_data)
        self.append_to_json("../dataset/bookings.json", booking_data)

        # Hiển thị thông báo với tùy chọn xuất hóa đơn
        confirmation_dialog = QMessageBox(self.bookingWindow)
        confirmation_dialog.setWindowTitle("Booking Successful")
        confirmation_dialog.setText(f"Đặt phòng thành công!\n\nMã đặt phòng: {booking_id}")
        confirmation_dialog.setIcon(QMessageBox.Icon.Information)

        # Thêm nút "Generate Invoice"
        generate_invoice_button = confirmation_dialog.addButton("Xuất hóa đơn", QMessageBox.ButtonRole.ActionRole)
        confirmation_dialog.setStandardButtons(QMessageBox.StandardButton.Ok)

        # Kết nối nút xuất hóa đơn
        generate_invoice_button.clicked.connect(lambda: self.generate_invoice(booking_id, booking_data))

        confirmation_dialog.exec()

        # Đóng cửa sổ đặt phòng và hiển thị màn hình cảm ơn
        self.bookingWindow.close()
        self.show_confirm_and_thanks_screen()

    def generate_invoice(self, booking_id, booking_data):
        """Lưu hóa đơn vào file invoices.json trong thư mục dataset với giá tiền."""
        # Bảng giá phòng (VNĐ)
        room_prices = {
            "CLASSIC ROOM": 2400000,
            "DELUXE ROOM": 2600000,
            "FAMILY ROOM": 3000000,
            "MASTER SUITE": 5000000
        }

        # Tính toán số ngày lưu trú
        from PyQt6.QtCore import QDate  # Đảm bảo import QDate để xử lý ngày tháng
        arrival_date = QDate.fromString(booking_data["arrival_date"], "yyyy-MM-dd")
        departure_date = QDate.fromString(booking_data["departure_date"], "yyyy-MM-dd")
        days_of_stay = arrival_date.daysTo(departure_date)

        # Kiểm tra nếu số ngày <= 0
        if days_of_stay <= 0:
            QMessageBox.warning(
                self.bookingWindow,
                "Lỗi ngày tháng",
                "Ngày trả phòng phải lớn hơn ngày nhận phòng!"
            )
            return

        # Lấy giá phòng và tính tổng chi phí
        room_type = booking_data["room_type"]
        room_price = room_prices.get(room_type, 0)
        total_price = room_price * days_of_stay

        # Dữ liệu hóa đơn
        invoice_data = {
            "invoice_id": booking_id,
            "customer_name": booking_data['full_name'],
            "phone_number": booking_data['phone_number'],
            "arrival_date": booking_data['arrival_date'],
            "departure_date": booking_data['departure_date'],
            "days_of_stay": days_of_stay,
            "room_type": room_type,
            "room_price_per_day": room_price,
            "total_price": total_price
        }

        # Đường dẫn đến file invoices.json
        invoices_path = "../dataset/invoices.json"
        os.makedirs(os.path.dirname(invoices_path), exist_ok=True)

        # Đọc nội dung hiện tại của invoices.json, nếu tồn tại
        if os.path.exists(invoices_path):
            with open(invoices_path, "r", encoding="utf-8") as file:
                try:
                    all_invoices = json.load(file)
                except json.JSONDecodeError:
                    all_invoices = []  # Nếu file không có dữ liệu hợp lệ, tạo danh sách mới
        else:
            all_invoices = []  # Nếu file chưa tồn tại, tạo danh sách mới

        # Thêm hóa đơn mới vào danh sách
        all_invoices.append(invoice_data)

        # Ghi lại toàn bộ hóa đơn vào invoices.json
        with open(invoices_path, "w", encoding="utf-8") as file:
            json.dump(all_invoices, file, indent=4, ensure_ascii=False)

        # Thông báo hóa đơn đã được lưu
        QMessageBox.information(
            self.bookingWindow,
            "Hóa đơn đã lưu",
            f"Hóa đơn đã được lưu trong file {invoices_path}\n"
            f"Tổng tiền: {total_price:,} VNĐ"
        )

    def append_to_json(self, path, data):
        os.makedirs(os.path.dirname(path), exist_ok=True)

        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                try:
                    old_data = json.load(f)
                except json.JSONDecodeError:
                    old_data = []
        else:
            old_data = []

        old_data.append(data)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(old_data, f, indent=4, ensure_ascii=False)

    def show_confirm_and_thanks_screen(self):
        """Hiển thị màn hình cảm ơn."""
        self.confirmAndThanksWindow = QMainWindow()
        self.uiConfirmAndThanks = Ui_Dialog()  # Sử dụng giao diện từ file confirm_and_thanks.py
        self.uiConfirmAndThanks.setupUi(self.confirmAndThanksWindow)
        self.confirmAndThanksWindow.show()
        # Kết nối các nút với chức năng tương ứng
        self.uiConfirmAndThanks.pushButtonHome.clicked.connect(self.go_to_home_screen)  # Nút HOME
        self.uiConfirmAndThanks.pushButtonExit.clicked.connect(self.exit_application)  # Nút EXIT

    def go_to_home_screen(self):
        """Xử lý khi người dùng nhấn nút HOME."""
        self.confirmAndThanksWindow.close()
        self.MainWindow.show()  # Hiển thị lại màn hình chính (home screen)

    def exit_application(self):
        """Xử lý khi người dùng nhấn nút EXIT."""
        reply = QMessageBox.question(
            self.confirmAndThanksWindow,
            "Xác nhận thoát",
            "Bạn có chắc chắn muốn thoát phần mềm?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.confirmAndThanksWindow.close()
            QApplication.quit()  # Đóng ứng dụng
        else:
            # Nếu người dùng chọn "No", chỉ đóng hộp thoại xác nhận
            return

def save_booking_data(self):
    # Lấy thông tin từ form
    full_name = self.uiBooking.lineEditFullName.text()
    phone_number = self.uiBooking.lineEditPhone.text()
    arrival = self.uiBooking.dateEditArrival.date().toString("yyyy-MM-dd")
    departure = self.uiBooking.dateEditDeparture.date().toString("yyyy-MM-dd")
    adults = self.uiBooking.spinBoxAdults.value()
    children = self.uiBooking.spinBoxChildren.value()
    room_type = self.uiBooking.comboBoxRoom.currentText()

    if not full_name or not phone_number:
        QMessageBox.warning(self.bookingWindow, "Thiếu thông tin", "Vui lòng nhập đầy đủ họ tên và số điện thoại.")
        return

    # Tạo booking_id mới nối tiếp
    booking_file = "../dataset/bookings.json"
    if os.path.exists(booking_file):
        with open(booking_file, 'r', encoding='utf-8') as f:
            try:
                booking_list = json.load(f)
                last_id = max([int(item['booking_id']) for item in booking_list]) if booking_list else 0
            except Exception:
                booking_list = []
                last_id = 0
    else:
        booking_list = []
        last_id = 0

    new_id = last_id + 1
    booking_id = f"{new_id:05d}"  # Định dạng 5 chữ số, ví dụ: 00023

    # Tạo dữ liệu mới
    customer_data = {
        "booking_id": booking_id,
        "full_name": full_name,
        "phone": phone_number
    }

    booking_data = {
        "booking_id": booking_id,
        "full_name": full_name,
        "phone_number": phone_number,
        "arrival_date": arrival,
        "departure_date": departure,
        "adults": adults,
        "children": children,
        "room_type": room_type
    }

    # Lưu dữ liệu
    self.append_to_json("../dataset/customers.json", customer_data)
    self.append_to_json("../dataset/bookings.json", booking_data)

    # Hiển thị thông báo với tùy chọn xuất hóa đơn
    confirmation_dialog = QMessageBox(self.bookingWindow)
    confirmation_dialog.setWindowTitle("Booking Successful")
    confirmation_dialog.setText(f"Đặt phòng thành công!\n\nMã đặt phòng: {booking_id}")
    confirmation_dialog.setIcon(QMessageBox.Icon.Information)

    # Thêm nút "Generate Invoice"
    generate_invoice_button = confirmation_dialog.addButton("Xuất hóa đơn", QMessageBox.ButtonRole.ActionRole)
    confirmation_dialog.setStandardButtons(QMessageBox.StandardButton.Ok)

    # Kết nối nút xuất hóa đơn
    generate_invoice_button.clicked.connect(lambda: self.generate_invoice(booking_id, booking_data))

    confirmation_dialog.exec()

    # Đóng cửa sổ đặt phòng và hiển thị màn hình cảm ơn
    self.bookingWindow.close()
    self.show_confirm_and_thanks_screen()



def  generate_invoice(self, booking_id, booking_data):
    """Xuất hóa đơn dựa trên thông tin đặt phòng và lưu dưới dạng JSON."""
    # Dữ liệu hóa đơn
    invoice_data = {
        "invoice_id": booking_id,
        "customer_name": booking_data['full_name'],
        "phone_number": booking_data['phone_number'],
        "arrival_date": booking_data['arrival_date'],
        "departure_date": booking_data['departure_date'],
        "adults": booking_data['adults'],
        "children": booking_data['children'],
        "room_type": booking_data['room_type']
    }

    # Đường dẫn lưu hóa đơn
    invoice_path = f"../invoices/invoice_{booking_id}.json"
    os.makedirs(os.path.dirname(invoice_path), exist_ok=True)

    # Lưu hóa đơn vào file JSON
    with open(invoice_path, "w", encoding="utf-8") as file:
        json.dump(invoice_data, file, indent=4, ensure_ascii=False)

    # Thông báo hóa đơn đã được lưu
    QMessageBox.information(
        self.bookingWindow,
        "Hóa đơn đã lưu",
        f"Hóa đơn đã được lưu tại: {invoice_path}"
    )


def append_to_json(self, path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            try:
                old_data = json.load(f)
            except json.JSONDecodeError:
                old_data = []
    else:
        old_data = []

    old_data.append(data)

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(old_data, f, indent=4, ensure_ascii=False)


def show_confirm_and_thanks_screen(self):
    """Hiển thị màn hình cảm ơn."""
    self.confirmAndThanksWindow = QMainWindow()
    self.uiConfirmAndThanks = Ui_Dialog()  # Sử dụng giao diện từ file confirm_and_thanks.py
    self.uiConfirmAndThanks.setupUi(self.confirmAndThanksWindow)
    self.confirmAndThanksWindow.show()
    # Kết nối các nút với chức năng tương ứng
    self.uiConfirmAndThanks.pushButtonHome.clicked.connect(self.go_to_home_screen)  # Nút HOME
    self.uiConfirmAndThanks.pushButtonExit.clicked.connect(self.exit_application)  # Nút EXIT


def go_to_home_screen(self):
    """Xử lý khi người dùng nhấn nút HOME."""
    self.confirmAndThanksWindow.close()
    self.MainWindow.show()  # Hiển thị lại màn hình chính (home screen)


def exit_application(self):
    """Xử lý khi người dùng nhấn nút EXIT."""
    reply = QMessageBox.question(
        self.confirmAndThanksWindow,
        "Xác nhận thoát",
        "Bạn có chắc chắn muốn thoát phần mềm?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No
    )

    if reply == QMessageBox.StandardButton.Yes:
        self.confirmAndThanksWindow.close()
        QApplication.quit()  # Đóng ứng dụng
    else:
        # Nếu người dùng chọn "No", chỉ đóng hộp thoại xác nhận
        return

