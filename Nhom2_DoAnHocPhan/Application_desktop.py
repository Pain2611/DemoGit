import pickle
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyodbc

server = 'PHUC\SQLEXPRESS'
database = 'HSBNThanManTinh'
user = 'sa'
password = '123'
conn = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+password)
tendangnhap=''

#Cửa sổ giao diện đăng nhập
login_window = tk.Tk()
login_window.title('Đăng nhập')

#Kích thước cửa sổ
window_width = 500
window_height = 400

#Kíck thước màn hình
screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()

#Vị trí hiển thị cửa sổ
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

#Vị trí cửa sổ
login_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#Tạo giao diện đăng nhập
label_user = tk.Label(login_window, text="Tên đăng nhập")
label_user.pack()
entry_user = tk.Entry(login_window)
entry_user.pack()

label_password = tk.Label(login_window, text="Mật khẩu")
label_password.pack()
entry_password = tk.Entry(login_window, show="*")
entry_password.pack()

label_phone = tk.Label(login_window, text="Số điện thoại")
label_phone.pack()
entry_phone = tk.Entry(login_window)
entry_phone.pack()

#Hàm đăng ký
def Reg():
    user = entry_user.get()
    password = entry_password.get()
    phone = entry_phone.get()

    if user == "" or password == "" or phone == "":
        messagebox.showerror("Lỗi đăng nhập", "Vui lòng nhập lại tên đăng nhập hoặc mật khẩu hoặc số điện thoại!")
    else:
        cursor = conn.cursor()
        query = "SELECT * FROM TaiKhoan WHERE TenDN=?"
        params = (user,)
        result = cursor.execute(query.params).fetchone()
        if result:
            messagebox.showerror("Tên đăng nhập đã tồn tại!")
        else:
            query = "INSERT INTO TaiKhoan (TenDN, MatKhau, SDT) VALUES (?, ?, ?)"
            params = (user, password, phone)
            cursor.execute(query, params)
            cursor.commit()
            messagebox.showinfo("Đăng ký thành công!")
        cursor.close()

#Hàm đăng nhập
def login():
    user = entry_user.get()
    password = entry_password.get()

    if user == "" or password == "":
        messagebox.showerror("Lỗi đăng nhập", "Vui lòng nhập lại tên đăng nhập hay mật khẩu!")
    else:
        if ktra_dang_nhap(user, password):
            login_window.destroy()
            if user == "Admin" and password == "123":
                show_admin_window()
            else:
                show_predict_window(user)

#Kiểm tra thông tin đăng nhập trong cơ sở dữ liệu
def ktra_dang_nhap(user, password):
    cursor = conn.cursor()
    query = "SELECT * FROM TaiKhoan WHERE TenDN=? AND MatKhau=?"
    params = (user, password)
    result = cursor.execute(query, params).fetchone()
    cursor.close()

    if result:
        return True
    else:
        return False

button_login = tk.Button(login_window, text="Đăng nhập", command=login, bg="#5783db", fg="white", font=("Arial", 12, "bold"), width=15)
button_login.pack(pady=10)

button_register = tk.Button(login_window, text="Đăng ký", command=Reg, bg="#55c2da", fg="white", font=("Arial", 12, "bold"), width=15)
button_register.pack(pady=10)

button_login.pack(pady=10)
button_register.pack(pady=10)

#
def show_admin_window():
    admin_window = tk.Tk()
    admin_window.title("Form quản lý")

    treeview = tk.ttk.Treeview(admin_window)
    treeview.pack()

    #Thiệt lập cột
    treeview["columns"] = ("TenDN", "Ngay", "age", "bp", "sg", "al", "su", "rbc", "pc", "pcc", "ba", "bgr", "bu", "sc", "sod", "pot", "hemo", "pcv", "wc", "rc", "htn", "dm", "cad", "appet", "pe", "ane", "KetQua")
    treeview.column("#0", width=0, stretch=tk.NO)
    treeview.column("TenDN", width=100, anchor=tk.W)
    treeview.column("Ngay",width=100, anchor=tk.W)
    treeview.column("age", width=50, anchor=tk.CENTER)
    treeview.column("bp", width=50, anchor=tk.CENTER)
    treeview.column("sg", width=50, anchor=tk.CENTER)
    treeview.column("al", width=50, anchor=tk.CENTER)
    treeview.column("su", width=50, anchor=tk.CENTER)
    treeview.column("rbc", width=50, anchor=tk.CENTER)
    treeview.column("pc", width=50, anchor=tk.CENTER)
    treeview.column("pcc", width=50, anchor=tk.CENTER)
    treeview.column("ba", width=50, anchor=tk.CENTER)
    treeview.column("bgr", width=50, anchor=tk.CENTER)
    treeview.column("bu", width=50, anchor=tk.CENTER)
    treeview.column("sc", width=50, anchor=tk.CENTER)
    treeview.column("sod", width=50, anchor=tk.CENTER)
    treeview.column("pot", width=50, anchor=tk.CENTER)
    treeview.column("hemo", width=50, anchor=tk.CENTER)
    treeview.column("pcv", width=50, anchor=tk.CENTER)
    treeview.column("rc", width=50, anchor=tk.CENTER)
    treeview.column("htn", width=50, anchor=tk.CENTER)
    treeview.column("dm", width=50, anchor=tk.CENTER)
    treeview.column("cad", width=50, anchor=tk.CENTER)
    treeview.column("appet", width=50, anchor=tk.CENTER)
    treeview.column("pe", width=50, anchor=tk.CENTER)
    treeview.column("ane", width=50, anchor=tk.CENTER)
    treeview.column("KetQua", width=100, anchor=tk.W)

    #Tiêu đề cho côt
    treeview.heading("TenDN", text="Tên đăng nhập")
    treeview.heading("Ngay", text="Ngày")
    treeview.heading("age", text="Tuổi")
    treeview.heading("bp", text="bp")
    treeview.heading("sg", text="sg")
    treeview.heading("al", text="al")
    treeview.heading("su", text="su")
    treeview.heading("rbc", text="rbc")
    treeview.heading("pc", text="pc")
    treeview.heading("pcc", text="pcc")
    treeview.heading("ba", text="pa")
    treeview.heading("bgr", text="bgr")
    treeview.heading("bu", text="bu")
    treeview.heading("sc", text="sc")
    treeview.heading("sod", text="sod")
    treeview.heading("pot", text="pot")
    treeview.heading("hemo", text="hemo")
    treeview.heading("pcv", text="pcv")
    treeview.heading("rc", text="rc")
    treeview.heading("htn", text="htn")
    treeview.heading("dm", text="dm")
    treeview.heading("cad", text="cad")
    treeview.heading("appet", text="appet")
    treeview.heading("pe", text="pe")
    treeview.heading("ane", text="ane")
    treeview.heading("KetQua", text="Kết quả dự đoán")

    #Lấy dữ liệu từ bảng bệnh án
    cursor = conn.cursor()
    query = "SELECT * FROM BenhAn"
    result = cursor.execute(query).fetchall()
    cursor.close()

    #Hiển thị lên Treeview
    for row in result:
        kq = str(row[-1])
        treeview.insert("", tk.END, values=row[:-1] + (kq,))
    tree = ttk.Treeview(admin_window)
    tree["columns"] = ("TenDN", "SDT")
    tree.heading("TenDN", text="Tên đăng nhập")
    tree.heading("SDT", text="Số điện thoại")

    #Lấy dữ liệu từ bảng tài khoản
    cursor = conn.cursor()
    query = "SELECT TenDN, SDT FROM TaiKhoan"
    result = cursor.execute(query).fetchall()
    cursor.close()

    #Hiển thị dữ liệu từ bảng tài khoản trong Treeview
    for row in result:
        tree.insert("", "end", values=(row[0], row[1]))

    #Hiển thị Treeview trong form quản lý
    tree.pack()
    admin_window.mainloop()

#
def show_predict_window(user):
    predict_window = tk.Tk()
    predict_window.title('Chuẩn đoán thận mãn tính')

    chart_frame = tk.Frame(predict_window)
    chart_frame.grid(row=0, column=3, rowspan=26)

    Than_model = pickle.load(open('ThanManTinh_Reg.sav', 'rb'))

    def predict():
        if any([
            not entry_age.get(),
            not entry_bp.get(),
            not entry_sg.get(),
            not entry_al.get(),
            not entry_su.get(),
            not entry_rbc.get(),
            not entry_pc.get(),
            not entry_pcc.get(),
            not entry_ba.get(),
            not entry_bgr.get(),
            not entry_bu.get(),
            not entry_sc.get(),
            not entry_sod.get(),
            not entry_pot.get(),
            not entry_hemo.get(),
            not entry_pcv.get(),
            not entry_wc.get(),
            not entry_rc.get(),
            not entry_htn.get(),
            not entry_dm.get(),
            not entry_cad.get(),
            not entry_appet.get(),
            not entry_pe.get(),
            not entry_ane.get()
        ]):
            messagebox.showerror("Vui lòng nhập đầy đủ thông tin")
            return
        age = float(entry_age.get())
        bp = float(entry_bp.get())
        sg = float(entry_sg.get())
        al = float(entry_al.get())
        su = float(entry_su.get())
        rbc = float(entry_rbc.get())
        pc = float(entry_pc.get())
        pcc = float(entry_pcc.get())
        ba = float(entry_ba.get())
        bgr = float(entry_bgr.get())
        bu = float(entry_bu.get())
        sc = float(entry_sc.get())
        sod = float(entry_sod.get())
        pot = float(entry_pot.get())
        hemo = float(entry_hemo.get())
        pcv = float(entry_pcv.get())
        wc = float(entry_wc.get())
        rc = float(entry_rc.get())
        htn = float(entry_htn.get())
        dm = float(entry_dm.get())
        cad = float(entry_cad.get())
        appet = float(entry_appet.get())
        pe = float(entry_pe.get())
        ane = float(entry_ane.get())

        Than_prediction = Than_model.predict([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]])

        if Than_prediction[0] == 0:
            dudoan = 'Không bị thận mãn tính'
        else:
            dudoan = 'Bị thận mãn tính'

        result_label.config(text=dudoan)
        cursor = conn.cursor()
        query = "INSERT INTO BenhAn (TenDn, Ngay, Tuoi, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane, KetQuaChuanDoan) VALUES (?, GETDATE(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        params = (user, age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane, dudoan)

        cursor.execute(query, params)
        cursor.commit()
        cursor.close()
    #
    label_age = tk.Label(predict_window, text= "Nhập tuổi của bạn")
    label_age.grid(row=1, column=0, columnspan=2)

    label_user = tk.Label(predict_window, text="Tên đăng nhập" + user)
    label_user.grid(row=0, column=0, columnspan=2)

    label_bp = tk.Label(predict_window, text="Nhập bp của bạn")
    label_bp.grid(row=2, column=0, columnspan=2)

    label_sg = tk.Label(predict_window, text="Nhập sg của bạn")
    label_sg.grid(row=3, column=0, columnspan=2)

    label_al = tk.Label(predict_window, text="Nhập al của bạn")
    label_al.grid(row=4, column=0, columnspan=2)

    label_su = tk.Label(predict_window, text="Nhập su của bạn")
    label_su.grid(row=5, column=0, columnspan=2)

    label_rbc = tk.Label(predict_window, text="Nhập rbc của bạn")
    label_rbc.grid(row=6, column=0, columnspan=2)

    label_pc = tk.Label(predict_window, text="Nhập pc của bạn")
    label_pc.grid(row=7, column=0, columnspan=2)

    label_pcc = tk.Label(predict_window, text="Nhập pcc của bạn")
    label_pcc.grid(row=8, column=0, columnspan=2)

    label_ba = tk.Label(predict_window, text="Nhập ba của bạn")
    label_ba.grid(row=9, column=0, columnspan=2)

    label_bgr = tk.Label(predict_window, text="Nhập bgr của bạn")
    label_bgr.grid(row=10, column=0, columnspan=2)

    label_bu = tk.Label(predict_window, text="Nhập bu của bạn")
    label_bu.grid(row=11, column=0, columnspan=2)

    label_sc = tk.Label(predict_window, text="Nhập sc của bạn")
    label_sc.grid(row=12, column=0, columnspan=2)

    label_sod = tk.Label(predict_window, text="Nhập sod của bạn")
    label_sod.grid(row=13, column=0, columnspan=2)

    label_pot = tk.Label(predict_window, text="Nhập pot của bạn")
    label_pot.grid(row=14, column=0, columnspan=2)

    label_hemo = tk.Label(predict_window, text="Nhập hemo của bạn")
    label_hemo.grid(row=15, column=0, columnspan=2)

    label_pcv = tk.Label(predict_window, text="Nhập pcv của bạn")
    label_pcv.grid(row=16, column=0, columnspan=2)

    label_wc = tk.Label(predict_window, text="Nhập wc của bạn")
    label_wc.grid(row=17, column=0, columnspan=2)

    label_rc = tk.Label(predict_window, text="Nhập rc của bạn")
    label_rc.grid(row=18, column=0, columnspan=2)

    label_htn = tk.Label(predict_window, text="Nhập htn của bạn")
    label_htn.grid(row=19, column=0, columnspan=2)

    label_dm = tk.Label(predict_window, text="Nhập dm của bạn")
    label_dm.grid(row=20, column=0, columnspan=2)

    label_cad = tk.Label(predict_window, text="Nhập cad của bạn")
    label_cad.grid(row=21, column=0, columnspan=2)

    label_appet = tk.Label(predict_window, text="Nhập appet của bạn")
    label_appet.grid(row=22, column=0, columnspan=2)

    label_pe = tk.Label(predict_window, text="Nhập tpe của bạn")
    label_pe.grid(row=23, column=0, columnspan=2)

    label_ane = tk.Label(predict_window, text="Nhập ane của bạn")
    label_ane.grid(row=24, column=0, columnspan=2)

    entry_age = tk.Entry(predict_window)
    entry_age.grid(row=1, column=2)

    entry_bp = tk.Entry(predict_window)
    entry_bp.grid(row=2, column=2)

    entry_sg = tk.Entry(predict_window)
    entry_sg.grid(row=3, column=2)

    entry_al = tk.Entry(predict_window)
    entry_al.grid(row=4, column=2)

    entry_su = tk.Entry(predict_window)
    entry_su.grid(row=5, column=2)

    entry_rbc = tk.Entry(predict_window)
    entry_rbc.grid(row=6, column=2)

    entry_pc = tk.Entry(predict_window)
    entry_pc.grid(row=7, column=2)

    entry_pcc = tk.Entry(predict_window)
    entry_pcc.grid(row=8, column=2)

    entry_ba = tk.Entry(predict_window)
    entry_ba.grid(row=9, column=2)

    entry_bgr = tk.Entry(predict_window)
    entry_bgr.grid(row=10, column=2)

    entry_bu = tk.Entry(predict_window)
    entry_bu.grid(row=11, column=2)

    entry_sc = tk.Entry(predict_window)
    entry_sc.grid(row=12, column=2)

    entry_sod = tk.Entry(predict_window)
    entry_sod.grid(row=13, column=2)

    entry_pot = tk.Entry(predict_window)
    entry_pot.grid(row=14, column=2)

    entry_hemo = tk.Entry(predict_window)
    entry_hemo.grid(row=15, column=2)

    entry_pcv = tk.Entry(predict_window)
    entry_pcv.grid(row=16, column=2)

    entry_wc = tk.Entry(predict_window)
    entry_wc.grid(row=17, column=2)

    entry_rc = tk.Entry(predict_window)
    entry_rc.grid(row=18, column=2)

    entry_htn = tk.Entry(predict_window)
    entry_htn.grid(row=19, column=2)

    entry_dm = tk.Entry(predict_window)
    entry_dm.grid(row=20, column=2)

    entry_cad = tk.Entry(predict_window)
    entry_cad.grid(row=21, column=2)

    entry_appet = tk.Entry(predict_window)
    entry_appet.grid(row=22, column=2)

    entry_pe = tk.Entry(predict_window)
    entry_pe.grid(row=23, column=2)

    entry_ane = tk.Entry(predict_window)
    entry_ane.grid(row=24, column=2)

    button_predict = tk.Button(predict_window, text='Dự đoán', command=predict)
    button_predict.grid(row=25, column=0, columnspan=3)

    result_label = tk.Label(predict_window, text='')
    result_label.grid(row=26, column=0, columnspan=3)

    #Chạy ứng dụng dự đoán
    predict_window.mainloop()

#Chạy ứng dụng đăng nhập
login_window.mainloop()
