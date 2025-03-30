from libs.JsonFileFactory import JsonFileFactory
from models.Room import Room


class DataConnector:
    def get_all_rooms(self):
        """
        Lấy danh sách tất cả các phòng từ file JSON.
        """
        jff = JsonFileFactory()
        filename = "../dataset/rooms.json"
        rooms = jff.read_data(filename, Room)
        return rooms

    # def get_all_customers(self):
    #     """
    #     Lấy danh sách tất cả các khách hàng từ file JSON.
    #     """
    #     jff = JsonFileFactory()
    #     filename = "../dataset/customers.json"
    #     customers = jff.read_data(filename, Customer)
    #     return customers
    #
    # def get_all_bookings(self):
    #     """
    #     Lấy danh sách tất cả các đặt phòng từ file JSON.
    #     """
    #     jff = JsonFileFactory()
    #     filename = "../dataset/bookings.json"
    #     bookings = jff.read_data(filename, Booking)
    #     return bookings

    def login_manager(self, username, password):
        """
        Kiểm tra thông tin đăng nhập của người quản lý.
        """
        managers = [
            {"username": "externaluxe", "password": "doraemon"}
        ]
        for manager in managers:
            if manager["username"] == username and manager["password"] == password:
                return True
        return False
