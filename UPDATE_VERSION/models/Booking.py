class Booking:
    def __init__(self, booking_id, full_name, phone, arrival, departure, adults, children, room_type):
        """
        Khởi tạo đối tượng Booking
        :param booking_id: ID chung với Customer, đảm bảo sự liên kết
        :param full_name: Tên khách hàng
        :param phone: Số điện thoại liên lạc
        :param arrival: Ngày đến
        :param departure: Ngày đi
        :param adults: Số người lớn
        :param children: Số trẻ em
        :param room_type: Loại phòng
        """
        self.booking_id = booking_id  # ID chung cho Customer và Booking khi chung 1 đơn đặt
        self.full_name = full_name
        self.phone = phone
        self.arrival = arrival
        self.departure = departure
        self.adults = adults
        self.children = children
        self.room_type = room_type

    def to_dict(self):
        """
        Chuyển đổi đối tượng Booking thành dictionary
        :return: Dictionary chứa thông tin đặt phòng
        """
        return {
            "booking_id": self.booking_id,
            "full_name": self.full_name,
            "phone": self.phone,
            "arrival": self.arrival,
            "departure": self.departure,
            "adults": self.adults,
            "children": self.children,
            "room_type": self.room_type
        }

    @staticmethod
    def from_dict(data):
        """
        Tạo một đối tượng Booking từ dictionary
        :param data: Dictionary chứa thông tin đặt phòng
        :return: Đối tượng Booking
        """
        return Booking(
            booking_id=data.get("booking_id"),
            full_name=data.get("full_name"),
            phone=data.get("phone"),
            arrival=data.get("arrival"),
            departure=data.get("departure"),
            adults=data.get("adults"),
            children=data.get("children"),
            room_type=data.get("room_type")
        )
