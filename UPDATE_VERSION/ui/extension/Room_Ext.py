
import json
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem, QInputDialog, QDialog, QVBoxLayout, QLineEdit, QPushButton, QComboBox, QLabel
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt

from libs.DataConnector import DataConnector
from ui.customer_management.customer_management import Ui_CustomerManagement
from ui.home_screen.home_screen import Ui_MainWindow
from ui.login_screen.login_screen import Ui_LoginWindow
from ui.room_management.room_management import Ui_RoomManagement


class Room_Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)

    def process_login(self):
        self.MainWindow.close()
        self.loginWindow = QMainWindow()
        self.uiLogin = Ui_LoginWindow()
        self.uiLogin.setupUi(self.loginWindow)
        self.uiLogin.pushButtonSignIn.clicked.connect(self.login_success)
        self.loginWindow.show()

    def login_success(self):
        dc = DataConnector()
        username = self.uiLogin.lineEditUserName.text()
        password = self.uiLogin.lineEditPassWord.text()

        if not self.uiLogin.radioButtonRooms.isChecked() and not self.uiLogin.radioButtonCustomers.isChecked():
            QMessageBox.warning(self.loginWindow, "Thông báo", "Vui lòng chọn chức năng muốn đăng nhập.")
            return

        if dc.login_manager(username, password):
            self.loginWindow.close()
            if self.uiLogin.radioButtonRooms.isChecked():
                self.mainwindow = RoomManager()
                self.mainwindow.show()
            elif self.uiLogin.radioButtonCustomers.isChecked():
                self.mainwindow = QMainWindow()
                self.myui = Ui_CustomerManagement()
                self.myui.setupUi(self.mainwindow)
                self.mainwindow.show()
        else:
            QMessageBox.warning(self.loginWindow, "Đăng nhập thất bại", "Tài khoản hoặc mật khẩu không đúng.")


class SearchDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tìm kiếm phòng")
        self.setFixedSize(400, 220)
        layout = QVBoxLayout(self)

        self.input_id = QLineEdit(self)
        self.input_id.setPlaceholderText("Nhập mã phòng (ví dụ: 101)")
        layout.addWidget(QLabel("Mã phòng:"))
        layout.addWidget(self.input_id)

        self.input_type = QComboBox(self)
        self.input_type.addItem("", "")
        self.input_type.addItem("Classic Room")
        self.input_type.addItem("Deluxe Room")
        self.input_type.addItem("Family Room")
        self.input_type.addItem("Master Suite")
        layout.addWidget(QLabel("Loại phòng:"))
        layout.addWidget(self.input_type)

        self.input_status = QComboBox(self)
        self.input_status.addItem("", "")
        self.input_status.addItem("available")
        self.input_status.addItem("unavailable")
        layout.addWidget(QLabel("Trạng thái:"))
        layout.addWidget(self.input_status)

        btn = QPushButton("Tìm", self)
        layout.addWidget(btn)
        btn.clicked.connect(self.accept)


class RoomManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RoomManagement()
        self.ui.setupUi(self)
        self.rooms = self.load_rooms("../dataset/rooms.json")
        self.current_room = None

        self.ui.listWidgetRoomList.clear()
        self.populate_room_list()
        self.ui.listWidgetRoomList.itemClicked.connect(self.display_room_info)
        self.ui.pushButtonUpdate.clicked.connect(self.update_room_status)

    def load_rooms(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_rooms(self, filename="../dataset/rooms.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.rooms, f, indent=4, ensure_ascii=False)

    def populate_room_list(self, filtered=None):
        self.ui.listWidgetRoomList.clear()
        rooms_to_display = filtered if filtered is not None else self.rooms
        for room in rooms_to_display:
            text = f"Phòng {room['room_id']} - {room['room_type']} - {room['status']}"
            item = QListWidgetItem(text)
            item.setData(1000, room['room_id'])
            self.ui.listWidgetRoomList.addItem(item)

    def display_room_info(self, item):
        room_id = item.data(1000)  # Lấy mã phòng được chọn
        room = next((r for r in self.rooms if r["room_id"] == room_id), None)
        if room:
            self.current_room = room

            # Đảm bảo comboBoxRoomType có đầy đủ các loại phòng trước khi cập nhật
            if self.ui.comboBoxRoomType.findText(room["room_type"]) == -1:
                self.ui.comboBoxRoomType.addItem(room["room_type"])

            # Cập nhật giá trị hiển thị trong comboBoxRoomType
            self.ui.comboBoxRoomType.setCurrentText(room["room_type"])

            # Cập nhật các thông tin khác
            self.ui.comboBoxFloor.setCurrentText(str(room["floor"]))
            self.ui.comboBoxRoomNumber.setCurrentText(str(room["room_id"])[-2:])  # Lấy 2 chữ số cuối của mã phòng
            if room["status"] == "available":
                self.ui.radioButtonAvailable.setChecked(True)
            else:
                self.ui.radioButtonUnavailable.setChecked(True)

    def update_room_status(self):
        if not self.current_room:
            return
        new_status = "available" if self.ui.radioButtonAvailable.isChecked() else "unavailable"
        self.current_room["status"] = new_status
        self.save_rooms()
        self.populate_room_list()
        QMessageBox.information(self, "Thành công", "Cập nhật trạng thái phòng thành công!")

    def keyPressEvent(self, event: QKeyEvent):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier and event.key() == Qt.Key.Key_F:
            dlg = SearchDialog(self)
            if dlg.exec():
                room_id = dlg.input_id.text().strip()
                room_type = dlg.input_type.currentText()
                status = dlg.input_status.currentText()

                filtered = self.rooms
                if room_id:
                    filtered = [r for r in filtered if str(r["room_id"]) == room_id]
                if room_type:
                    filtered = [r for r in filtered if r["room_type"] == room_type]
                if status:
                    filtered = [r for r in filtered if r["status"] == status]

                self.populate_room_list(filtered if any([room_id, room_type, status]) else None)


    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Xác nhận thoát",
            "Bạn có chắc chắn muốn thoát không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

