import json

def read_rooms():
    file_path = "../dataset/rooms.json"
    with open(file_path, "r", encoding="utf-8") as f:
        rooms = json.load(f)

    print(f"Đọc thành công danh sách phòng khách sạn Externa Luxe từ '{file_path}':\n")

    for room in rooms:
        print(f"Phòng {room['room_id']} | Tầng {room['floor']} | Loại: {room['room_type']} | "
              f"Giá: {room['price']:,}đ | Trạng thái: {room['status']}")


if __name__ == "__main__":
    read_rooms()
