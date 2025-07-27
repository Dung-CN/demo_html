def check_number(DTB):
    if DTB >=8.5:
       return "Xuất sắc"
    elif DTB>=7.0 and DTB <8.5:
       return "Giỏi"
    elif DTB>=5.5 and DTB <7.0:
       return "Khá"
    elif DTB>=4.0 and DTB <5.5:
       return "Trung bình"
    else:
       return "Yếu"

try:
   so_luong_mon_hoc = int(input("Nhập số lượng môn học: "))
   if so_luong_mon_hoc <=0 or so_luong_mon_hoc > 13:
      print("Số lượng môn học không hợp lệ.")
   else:
      tong_diem = 0
      for i in range(so_luong_mon_hoc):
         diem_mon_hoc = float(input(f"Nhập điểm trung bình của môn học thứ {i+1}:"))
         if diem_mon_hoc < 0 or diem_mon_hoc > 10:
            print("Điểm không hợp lệ. Vui lòng nhập điểm từ 0 đến 10.")
            break
         tong_diem += diem_mon_hoc
      else:
         DTB = tong_diem / so_luong_mon_hoc
         xep_loai = check_number(DTB)
         print(f"Điểm trung bình: {DTB:.2f}")
         print(f"Xếp loại: {xep_loai}")
except ValueError:
   print("Vui lòng nhập một số hợp lệ.")
