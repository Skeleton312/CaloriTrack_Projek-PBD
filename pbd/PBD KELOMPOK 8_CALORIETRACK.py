import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import customtkinter
import mysql.connector
from tkinter import font as tkfont
from tkinter import messagebox
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from datetime import datetime
from tkcalendar import DateEntry
from datetime import datetime


customtkinter.set_appearance_mode("light")


class CalorieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CALORIE TRACK")
        
        self.login_page(self.root)
    def db_connect(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bmi"
    )
        return db
    def login_page(self, root):
        self.root = root
        self.root.title("CaloriTrack")
        self.root.geometry("820x498")
        self.root.config(bg="white")

        img1 = ImageTk.PhotoImage(Image.open("./assets/bgcalorie.png"))
        l1 = customtkinter.CTkLabel(master=self.root, image=img1)
        l1.image = img1  
        l1.pack()

        frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        l2 = customtkinter.CTkLabel(master=frame, text="Hello! CalorieTrack", font=('Century Gothic', 20))
        l2.place(x=50, y=45)

        self.entry_name = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Nama')
        self.entry_name.place(x=50, y=110)

        self.entry_password = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
        self.entry_password.place(x=50, y=165)

        # l3 = customtkinter.CTkLabel(master=frame, text="Lupa Password?", font=('Century Gothic', 12))
        # l3.place(x=155, y=195)

        button1 = customtkinter.CTkButton(master=frame, width=220, text="Masuk", command=self.button_function, corner_radius=6)
        button1.place(x=50, y=240)
        self.root.mainloop()

        # img2 = customtkinter.CTkImage(Image.open("./assets/Google__G__Logo.svg.webp").resize((20, 20)))
        # img3 = customtkinter.CTkImage(Image.open("./assets/instagram.jpeg").resize((20, 20)))
        # button2 = customtkinter.CTkButton(master=frame, image=img2, text="Google", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        # button2.place(x=50, y=290)

        # button3 = customtkinter.CTkButton(master=frame, image=img3, text="Instagram", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        # button3.place(x=170, y=290)

    def button_function(self):
        self.email = self.entry_name.get()
        password = self.entry_password.get()
        conn=self.db_connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user_data WHERE nama = %s', (self.email,))
        user = cursor.fetchone()
        conn.close()

        if user and user[8] == password:
            messagebox.showinfo("Success", "Login successful! Redirecting to homepage.")
            self.root.destroy()
            new_root = customtkinter.CTk()
            self.main_page(new_root)
        elif user and user[8] != password:
            messagebox.showerror("Error", "Login failed. Incorrect username or password.")
        else:
            self.root.destroy()
            new_root = customtkinter.CTk()
            self.registration(new_root)
    def main_page(self, root):
        self.root = root
        self.root.title("CaloriTrack")
        self.root.geometry("820x498")
        self.root.config(bg="white")

        self.style = ttk.Style()
        self.style.configure('TNotebook', background='#0e8c80')
        self.style.configure('TFrame', background='#047b64')
        self.style.configure('TButton', background='#aed6d5', font=('Helvetica', 12))
        self.style.configure('TLabel', background='#ffffff', font=('Helvetica', 12))
        self.style.configure('TEntry', font=('Helvetica', 12))
        self.style.configure('TCombobox', font=('Helvetica', 12))

        self.user_data = {}
        self.food_data = {
            "Ringan(Buah,Sayur, Makanan Satuan)": {"calories": 100},
            "Sedang(Nasi Dan Lauk)": {"calories": 350},
            "Berat(Nasi Lauk Lebih dari 1)": {"calories": 500}
        }
        self.calorie_intake = []

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        notebook = ttk.Notebook(self.root, style='TNotebook')
        
        self.user_frame = ttk.Frame(notebook, style='TFrame')
        self.home_frame= ttk.Frame(notebook, style='TFrame')
        self.intake_frame = ttk.Frame(notebook, style='TFrame')
        self.report_frame = ttk.Frame(notebook, style='TFrame')

        notebook.add(self.home_frame, text="Home")
        notebook.add(self.intake_frame, text="Asupan Kalori")
        notebook.add(self.report_frame, text="Laporan")

        notebook.pack(expand=1, fill="both")
        self.create_window()
        self.create_user_frame()
        self.create_intake_frame()
        self.create_report_frame()
    def create_window(self):
        header_font = tkfont.Font(family="Helvetica", size=30, weight="bold")
        subheader_font = tkfont.Font(family="Helvetica", size=11)
        body_font = tkfont.Font(family="Helvetica", size=20)
        small_font = tkfont.Font(family="Helvetica", size=10)
        headline_font = tkfont.Font(family="Helvetica", size=20,weight='bold')
        conn=self.db_connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user_data WHERE nama = %s', (self.email,))
        user = cursor.fetchone()
        conn.close()
        # Top bar buttons
        self.top_bar_frame = tk.Frame(self.home_frame, bg="white")
        self.top_bar_frame.pack(side="top", fill="x", pady=(10, 0))

        registration_label = tk.Button(self.top_bar_frame, text=user[1], font=subheader_font,  bg="lightblue", bd=0)
        registration_label.pack(side="right", padx=(0, 20))

        # Main content
        self.main_frame = tk.Frame(self.home_frame, bg="white")
        self.main_frame.pack(fill="both", expand=True)

        # Load the image using Pillow
        img_path = "pbd2.jpg"  # Update this with the path to your image
        pil_image = Image.open(img_path)
        img = ImageTk.PhotoImage(pil_image)

        # Create a canvas for the image
        canvas = tk.Canvas(self.main_frame, width=820, height=300, bg="white", highlightthickness=0)
        canvas.create_image(0, 0, anchor='nw', image=img)
        canvas.pack(pady=(10, 10), padx=(20,20))

        # Keep a reference to the image to prevent garbage collection
        canvas.image = img

        # Content below the image
        self.content_frame = tk.Frame(self.main_frame, bg="white")
        self.content_frame.pack(fill="x", padx=20)

        # Headline on the left
        headline = tk.Label(self.content_frame, text="Selamat Datang di CaloriTrack!", font=headline_font, bg="white", width=25, anchor="w")
        headline.pack(side="left", pady=20, padx=5)

    def create_user_frame(self):
        ttk.Label(self.user_frame, text="Nama:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.user_name = ttk.Entry(self.user_frame)
        self.user_name.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.user_frame, text="Tinggi Badan (cm):").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.user_height = ttk.Entry(self.user_frame)
        self.user_height.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.user_frame, text="Berat Badan (kg):").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.user_weight = ttk.Entry(self.user_frame)
        self.user_weight.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.user_frame, text="Usia:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.user_age = ttk.Entry(self.user_frame)
        self.user_age.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self.user_frame, text="Jenis Kelamin:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.user_gender = ttk.Combobox(self.user_frame, values=["Pria", "Wanita"])
        self.user_gender.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(self.user_frame, text="Tingkat Keaktifan:").grid(row=5, column=0, padx=10, pady=5, sticky='w')
        self.user_activity = ttk.Combobox(self.user_frame, values=["Tidak Pernah Olahraga", "Jarang", "Sering"])
        self.user_activity.grid(row=5, column=1, padx=10, pady=5)

        ttk.Button(self.user_frame, text="Simpan Data Pengguna", command=self.save_user_data).grid(row=6, columnspan=2, pady=10)

    def save_user_data(self):
        self.user_data = {
            "name": self.user_name.get(),
            "height": float(self.user_height.get()),
            "weight": float(self.user_weight.get()),
            "age": int(self.user_age.get()),
            "gender": self.user_gender.get(),
            "activity": self.user_activity.get()
        }
        self.user_data["BMR"] = self.calculate_bmr(self.user_data)
        print("Data Pengguna Disimpan:", self.user_data)
        print("BMR (Target Kalori Harian):", self.user_data["BMR"])

    def calculate_bmr(self, data):
        if data["gender"] == "Pria":
            bmr = 66.5 + (13.7 * data["weight"]) + (5 * data["height"]) - (6.8 * data["age"])
        else:
            bmr = 655.1 + (9.563 * data["weight"]) + (1.850 * data["height"]) - (4.676 * data["age"])

        activity_factor = {
            "Tidak Pernah Olahraga": 1.2,
            "Jarang": 1.3,
            "Sering": 1.4
        }
        return bmr * activity_factor[data["activity"]]

    def create_intake_frame(self):
        conn=self.db_connect()
        cursor = conn.cursor()
        # Execute the first query
        cursor.execute('SELECT * FROM user_data WHERE nama = %s limit 1', (self.email,))
        user = cursor.fetchone()  # Read the result
        cursor.execute('SELECT time, food, calories FROM intake WHERE id_user = %s', (user[0],))
        intake = cursor.fetchall()  
        # Execute the second query
        cursor.execute('SELECT * FROM food')
        self.food = cursor.fetchall()  # Read the result
        cursor.execute("""
            SELECT DATE(time) AS tanggal, SUM(calories) AS total_calories
            FROM intake
            GROUP BY tanggal
            ORDER BY tanggal
        """)
        total_calories_rows = cursor.fetchall()
        # Close the connection
        conn.close()
        self.user_id=user[0]
        self.input_frame = tk.Frame(self.intake_frame, bg="white")
        self.input_frame.pack(side="top", pady=5, padx=10)
        data_makanan=[]
        for i in self.food:
            data_makanan.append(i[1])

        # ttk.Label(self.input_frame, text="Tanggal (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        # self.intake_date = ttk.Entry(self.input_frame)
        # self.intake_date.grid(row=0, column=1, padx=10, pady=5)

        # ttk.Label(self.input_frame, text="Waktu (HH:MM):").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        # self.intake_time = ttk.Entry(self.input_frame)
        # self.intake_time.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.input_frame, text="Jenis Makanan:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.intake_food = ttk.Combobox(self.input_frame, values=data_makanan)
        self.intake_food.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.input_frame, text="Jumlah Porsi:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.intake_serving = ttk.Entry(self.input_frame)
        self.intake_serving.grid(row=3, column=1, padx=10, pady=5)

        ttk.Button(self.input_frame, text="Simpan Asupan Kalori", command=self.save_calorie_intake).grid(row=4, columnspan=2, pady=10)
        self.tree = ttk.Treeview(self.intake_frame)
        self.tree.pack(fill="x")

        # Add columns
        self.tree["columns"] = ("tanggal", "food", "calories")
        self.tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column
        self.tree.column("tanggal", width=100, anchor=tk.W)
        self.tree.column("food", width=200, anchor=tk.W)
        self.tree.column("calories", width=100, anchor=tk.W)

        # Set column headings
        self.tree.heading("tanggal", text="Tanggal")
        self.tree.heading("food", text="Food")
        self.tree.heading("calories", text="Calories")
        # Create Treeview for total calories per day
        self.tree_total_calories = ttk.Treeview(self.intake_frame)
        self.tree_total_calories.pack(fill=tk.BOTH, expand=True)

        # Set columns for total calories per day
        self.tree_total_calories["columns"] = ("tanggal", "total_calories")
        self.tree_total_calories.column("#0", width=0, stretch=tk.NO)  # Hide the first column
        self.tree_total_calories.column("tanggal", width=100, anchor=tk.W)
        self.tree_total_calories.column("total_calories", width=100, anchor=tk.W)

        # Set column headings for total calories per day
        self.tree_total_calories.heading("tanggal", text="Tanggal")
        self.tree_total_calories.heading("total_calories", text="Total Calories")

        # Insert total calories per day data into Treeview
        for row in intake:
            self.tree.insert("", tk.END, values=row)
        for row in total_calories_rows:
            self.tree_total_calories.insert("", tk.END, values=row)
         # Insert data into Treeview


    def save_calorie_intake(self):
        conn=self.db_connect()
        cursor = conn.cursor()
        cursor.execute('SELECT kalori FROM food WHERE nama= %s',
            (self.intake_food.get(),))
        kalori=cursor.fetchone()  
        calories = kalori[0] * float(self.intake_serving.get())
        food= self.intake_food.get()
        serving = float(self.intake_serving.get())
        cursor.execute('SELECT id FROM user_data WHERE nama = %s limit 1', (self.email,))
        user = cursor.fetchone() 
        cursor.execute('INSERT INTO intake (id_user, food, serving, calories) VALUES (%s, %s, %s, %s)',
            (user[0], food, serving, calories,))
        conn.commit()
        cursor.execute('SELECT time, food, calories FROM intake ORDER BY id DESC LIMIT 1')
        new_row=cursor.fetchall()
        cursor.execute("""
            SELECT DATE(time) AS tanggal, SUM(calories) AS total_calories
            FROM intake
            GROUP BY tanggal
            ORDER BY tanggal
        """)
        total_calories_rows = cursor.fetchall()

        # Insert total calories per day into Treeview
        conn.close()
        for row in new_row:
            self.tree.insert("", tk.END, values=row)
        # Clear existing entries in total calories treeview
        for child in self.tree_total_calories.get_children():
            self.tree_total_calories.delete(child)

        # Insert updated total calories per day
        for row in total_calories_rows:
            self.tree_total_calories.insert("", tk.END, values=row)
        print("Asupan Kalori Disimpan")

    def update_calorie_list(self):
        # Fungsi ini bisa diimplementasikan untuk memperbarui tampilan list asupan kalori jika diperlukan.
        pass

    def create_report_frame(self):
        ttk.Button(self.report_frame, text="Generate Report", command=self.generate_report).pack(pady=10)
        self.report_text = tk.Text(self.report_frame, width=60, height=20)
        self.report_text.pack(pady=10)

    def generate_report(self):
        conn = self.db_connect()
        cursor=conn.cursor()
        # cursor.execute("""
        #     SELECT DATE(time) AS tanggal, SUM(calories) AS total_calories
        #     FROM intake
        #     GROUP BY tanggal
        #     ORDER BY tanggal
        # """)
        # total_calories = cursor.fetchall()
        cursor.execute('SELECT bmr FROM user_data WHERE nama = %s limit 1', (self.email,))
        bmr = cursor.fetchone() 
                 # Calculate today's total calories
        cursor.execute("""
                SELECT time, SUM(calories) AS total_calories
                FROM intake
                WHERE DATE(time) = CURDATE()
            """)
        total_calories_today = cursor.fetchone()
        conn.close()
        self.report_text.delete(1.0, tk.END)
        self.report_text.insert(tk.END, f"Jumlah kalori yang dikonsumsi per hari: {total_calories_today[1] }.")
        if total_calories_today[1]  > bmr[0]:
            self.report_text.insert(tk.END, " Anda melebihi target kalori harian!\n")
        else:
            self.report_text.insert(tk.END, "Anda di bawah target kalori harian.\n")

        # # Grafik asupan kalori
        # dates = [item["date"] for item in self.calorie_intake]
        # calories = [item["calories"] for item in self.calorie_intake]

        plt.figure(figsize=(10, 5))
        plt.plot(total_calories_today[0] , total_calories_today[1], marker='o', label='Kalori Dikonsumsi')
        plt.axhline(y=bmr[0], color='r', linestyle='-', label='Target Kalori')
        plt.xlabel('Tanggal')
        plt.ylabel('Kalori')
        plt.title('Grafik Asupan Kalori Harian')
        plt.legend()
        plt.grid(True)
        plt.gcf().autofmt_xdate()  # Format tanggal di sumbu x agar lebih terbaca
        plt.savefig('calorie_report.png')
        plt.show()

        self.report_text.insert(tk.END, "Grafik Asupan Kalori Selama Periode Waktu Tertentu Telah Dibuat\n")
    def registration(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.root.title("Registration Form")
        
        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=20, padx=40, fill='both', expand=True)
        
        label = customtkinter.CTkLabel(master=frame, text='CaloriTrack')
        label.pack(pady=12, padx=10)
        
        self.user_email = customtkinter.CTkEntry(master=frame, placeholder_text="Nama")
        self.user_email.pack(pady=12, padx=10)

        self.user_height = customtkinter.CTkEntry(master=frame, placeholder_text="Tinggi Badan (cm)")
        self.user_height.pack(pady=12, padx=10)

        self.user_weight = customtkinter.CTkEntry(master=frame, placeholder_text="Berat Badan (kg)")
        self.user_weight.pack(pady=12, padx=10)
        tk.Label(frame, text="Tanggal Lahir:").pack(anchor='w', padx=270)
        self.user_age = DateEntry(master=frame, date_pattern="yyyy-mm-dd")
        self.user_age.pack()

        self.user_gender = customtkinter.CTkComboBox(master=frame, values=["Pria", "Wanita"])
        self.user_gender.pack(pady=12, padx=10)
        self.user_gender.set("Gender")

        self.keaktifan = customtkinter.CTkComboBox(master=frame, values=["Tidak Pernah Olahraga", "Jarang", "Sering"])
        self.keaktifan.pack(pady=12, padx=10)
        self.keaktifan.set("Keaktifan")

        self.user_pass = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
        self.user_pass.pack(pady=12, padx=10)
        
        button = customtkinter.CTkButton(master=frame, text='Register', command=self.register_user)
        button.pack(pady=12, padx=10)
        self.root.mainloop()
    def register_user(self):
        email = self.user_email.get()
        height = self.user_height.get()
        weight = self.user_weight.get()
        gender = self.user_gender.get()
        activity = self.keaktifan.get()
        password = self.user_pass.get()
        birth_date = self.user_age.get_date()
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        self.user_data={
            "name": email,
            "height": float(height),
            "weight": float(weight),
            "age": float(age),
            "gender": gender,
            "activity":activity
        }
        bmr = self.calculate_bmr(self.user_data)
        conn=self.db_connect()
        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO user_data (nama, height, weight, age, gender, activity, bmr, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                        (email, height, weight, birth_date, gender, activity, bmr, password))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful! Redirecting to login form.")
            self.root.destroy()
            new_root = customtkinter.CTk()
            self.login_page(new_root)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    root = customtkinter.CTk()  # Start with the customtkinter window
    app = CalorieApp(root)
    root.mainloop()
