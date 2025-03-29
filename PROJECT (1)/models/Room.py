
class Room:
    def __init__(self, room_id, floor, room_number, room_type, price, status="available"):
        """
        Khởi tạo đối tượng Room.
        :param room_id: Mã phòng (ví dụ: 405, 707)
        :param floor: Tầng của phòng (1-10)
        :param room_type: Loại phòng (Classic Room, Deluxe Room, Family Room, Master Suite)
        :param price: Giá phòng (theo loại phòng)
        :param status: Trạng thái phòng ('available' hoặc 'unavailable')
        """
        self.room_id = room_id
        self.floor = floor
        self.room_type = room_type
        self.price = price
        self.status = status

    def update_status(self, new_status):
        """
        Cập nhật trạng thái phòng.
        :param new_status: Trạng thái mới ('available' hoặc 'unavailable')
        """
        if new_status in ["available", "unavailable"]:
            self.status = new_status
        else:
            raise ValueError("Trạng thái không hợp lệ. Chỉ chấp nhận 'available' hoặc 'unavailable'.")

    def to_dict(self):
        """
        Chuyển đổi đối tượng Room thành dictionary.
        :return: Dictionary chứa thông tin phòng.
        """
        return {
            "room_id": self.room_id,
            "floor": self.floor,
            "room_type": self.room_type,
            "price": self.price,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        """
        Tạo đối tượng Room từ dictionary.
        :param data: Dictionary chứa thông tin phòng.
        :return: Đối tượng Room.
        """
        return Room(
            room_id=data.get("room_id"),
            floor=data.get("floor"),
            room_type=data.get("room_type"),
            price=data.get("price"),
            status=data.get("status", "available")
        )
