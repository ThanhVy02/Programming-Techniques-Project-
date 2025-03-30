import json
import os
import random

def generate_rooms():
    rooms = []

    room_types = {
        "Classic Room": 2400000,
        "Deluxe Room": 2600000,
        "Family Room": 3000000,
        "Master Suite": 5000000
    }

    for floor in range(1, 11):  # Tầng 1 đến 10
        if floor <= 3:
            room_type = "Classic Room"
        elif floor <= 6:
            room_type = "Deluxe Room"
        elif floor <= 8:
            room_type = "Family Room"
        else:
            room_type = "Master Suite"

        price = room_types[room_type]

        for room in range(1, 9):  # Mỗi tầng có 8 phòng
            room_id = floor * 100 + room
            status = "unavailable" if random.random() < 0.25 else "available"  # 20/80 phòng sẽ được đặt (unavailable)

            rooms.append({
                "room_id": room_id,
                "floor": floor,
                "room_type": room_type,
                "price": price,
                "status": status
            })

    # Đảm bảo thư mục dataset tồn tại
    os.makedirs("../../dataset", exist_ok=True)

    # Ghi ra file JSON
    with open("../dataset/rooms.json", "w", encoding="utf-8") as f:
        json.dump(rooms, f, ensure_ascii=False, indent=4)

    print("Tạo thành công danh sách phòng khách sạn Externa Luxe.")

if __name__ == "__main__":
    generate_rooms()
