class Customer:
    def __init__(self, booking_id, full_name, phone):
        """
        Khởi tạo đối tượng Customer
        :param booking_id: ID chung với Booking, đảm bảo sự liên kết
        :param full_name: Họ và tên của khách hàng
        :param phone: Số điện thoại của khách hàng
        """
        self.booking_id = booking_id  # ID chung cho cả Customer và Booking
        self.full_name = full_name
        self.phone = phone

    def to_dict(self):
        """
        Chuyển đổi đối tượng Customer thành dictionary
        :return: Dictionary chứa thông tin khách hàng
        """
        return {
            "booking_id": self.booking_id,
            "full_name": self.full_name,
            "phone": self.phone
        }

    @staticmethod
    def from_dict(data):
        """
        Tạo một đối tượng Customer từ dictionary
        :param data: Dictionary chứa thông tin khách hàng
        :return: Đối tượng Customer
        """
        return Customer(
            booking_id=data.get("booking_id"),
            full_name=data.get("full_name"),
            phone=data.get("phone")
        )
