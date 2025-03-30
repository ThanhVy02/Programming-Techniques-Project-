from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.extension.Room_Ext import Room_Ext
from ui.extension.Booking_Ext import Booking_Ext

class CombinedApplication:
    def __init__(self):
        # Khởi tạo giao diện chính từ Room_Ext
        self.mainWindow = QMainWindow()
        self.roomUI = Room_Ext()  # Giao diện quản lý phòng
        self.roomUI.setupUi(self.mainWindow)
        self.roomUI.showWindow()
        # Gắn sự kiện nút để mở Booking_Ext
        self.roomUI.pushButtonBookNow_Home.clicked.connect(self.open_booking_window)

    def open_booking_window(self):
        self.mainWindow.close()

        # Khởi tạo cửa sổ Booking_Ext
        self.bookingWindow = QMainWindow()
        self.bookingUI = Booking_Ext()
        self.bookingUI.setupUi(self.bookingWindow)
        self.bookingWindow.show()

# Chạy phần mềm
app = QApplication([])
application = CombinedApplication()
app.exec()

