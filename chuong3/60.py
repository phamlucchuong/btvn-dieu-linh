# Câu 60: Phần mềm quản lý Sinh viên

from datetime import datetime


class sinhVien :
    def __init__(self, mssv, hoTen, ngaySinh, ho, ten, tuoi):
        self.mssv = mssv
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.ho = ho
        self.ten = ten
        self.tuoi = tuoi

    def getHoTen(self) :
        return self.hoTen
    
    def getNgaySinh(self):
        return self.ngaySinh
    
    def getTuoi(self):
        return self.tuoi
    
    def __str__(self):
        return f"MSSV: {self.mssv}, Họ Tên: {self.hoTen}, Ngày Sinh: {self.ngaySinh}, Tuổi: {self.tuoi}"



class dsSinhVien :
    def __init__(self):
        self.ds = []

    def themSV(self, sv) :
        self.ds.append(sv)

    def xoaSV(self, pos) :
        if 0 <= pos < len(self.ds):
            del self.ds[pos]
        else:
            print("Vị trí không hợp lệ!")

    def tongSV(self) :
        return len(self.ds)
    
    def timSV(self, hoTen) :
        for sv in self.ds:
            if sv.getHoTen().lower() == hoTen.lower():
                print(sv)
                return True
        
        print(f"khong tim thay sinh vien {hoTen}")
        return False
        
    def timSVCoNgaySinhTrongThangHienTai(self) :
        now = datetime.now()
        flag = False
        for sv in self.ds:
            if sv.getNgaySinh().month == now.month :
                print(sv)
                flag = True
        if not flag :
            print(f"khong tim thay sinh vien nao co ngay sinh trong thang {now.month}")
                
    def sapXepSV(self):
        n = len(self.ds)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.ds[j].tuoi > self.ds[j + 1].tuoi:
                    self.ds[j], self.ds[j + 1] = self.ds[j + 1], self.ds[j]

        for sv in self.ds:
            print(sv)



ds = dsSinhVien()
ds.themSV(sinhVien("1", "luc chuong", datetime(2004, 12, 21), "luc", "chuong", 21))
ds.themSV(sinhVien("2", "dieu linh", datetime(2005, 1, 25), "dieu", "linh", 20))

print(ds.tongSV())
ds.xoaSV(1)
print(ds.tongSV())
ds.timSV("luc chuong")
ds.timSVCoNgaySinhTrongThangHienTai()
ds.sapXepSV()