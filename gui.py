# gui.py
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from database import Database  # Import the Database class

class StudentGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1200+0+0")
        self.root.title("Student Management System")

        # Initialize the database connection
        self.db = Database()

        # ==================== Variable Declarations ====================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_stu_ID = StringVar()
        self.var_name = StringVar()
        self.var_sec = StringVar()
        self.var_age = StringVar()
        self.var_gen = StringVar()
        self.var_pno = StringVar()
        self.var_email = StringVar()
        self.var_bus = StringVar()
        self.var_com_search = StringVar()
        self.var_search = StringVar()

        # Call method to create GUI components
        self._create_widgets()
        # Initial data load
        self.fetch_data()

    def _create_widgets(self):
        """Creates and places all the GUI widgets."""

        # ==================== Header Images ====================
        # 1st image
        img1 = Image.open(r"/Users/luckyjaglan/Documents/Projects/Student-Management-System-Tkinter-MySQL/Management_Images/srm1.png")
        img1 = img1.resize((540, 160), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl_img1 = Label(self.root, image=self.photoimg1)
        lbl_img1.place(x=0, y=0, width=540, height=160)

        # 2nd image
        img2 = Image.open(r"/Users/luckyjaglan/Documents/Projects/Student-Management-System-Tkinter-MySQL/Management_Images/images_(1)-dszdYhTtd-transformed.jpeg")
        img2 = img2.resize((540, 160), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_img2 = Label(self.root, image=self.photoimg2)
        lbl_img2.place(x=540, y=0, width=540, height=160)

        # 3rd image
        img3 = Image.open(r"/Users/luckyjaglan/Documents/Projects/Student-Management-System-Tkinter-MySQL/Management_Images/mainbuilding.jpeg")
        img3 = img3.resize((540, 160), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl_img3 = Label(self.root, image=self.photoimg3)
        lbl_img3.place(x=1080, y=0, width=540, height=160)

        # Background Image
        bg_img = Image.open(r"/Users/luckyjaglan/Documents/Projects/Student-Management-System-Tkinter-MySQL/Management_Images/bg.png")
        bg_img = bg_img.resize((1530, 710), Image.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img)

        lbl_bg = Label(self.root, image=self.photobg_img)
        lbl_bg.place(x=0, y=160, width=1530, height=710)

        title_lbl = Label(lbl_bg, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # ==================== Main Frame ====================
        main_frame = Frame(lbl_bg, bd=2, bg="white")
        main_frame.place(x=5, y=55, width=1515, height=650)

        # ==================== Left Label Frame ====================
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=730, height=630)

        # Current Course Information
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=5, width=710, height=150)

        # Department
        dep_label = Label(current_course_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), width=18, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course:", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), width=18, state="readonly")
        course_combo["values"] = ("Select Course", "BTech", "MTech", "BCA", "MCA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year:", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), width=18, state="readonly")
        year_combo["values"] = ("Select Year", "1st Year", "2nd Year", "3rd Year", "4th Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # Semester
        sem_label = Label(current_course_frame, text="Semester:", font=("times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=("times new roman", 12, "bold"), width=18, state="readonly")
        sem_combo["values"] = ("Select Semester", "1st Sem", "2nd Sem", "3rd Sem", "4th Sem", "5th Sem", "6th Sem", "7th Sem", "8th Sem")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W)

        # Student Class Information
        student_class_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Student Class Information", font=("times new roman", 12, "bold"))
        student_class_frame.place(x=5, y=160, width=710, height=440)

        # Student ID
        stu_id_label = Label(student_class_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        stu_id_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        stu_id_entry = ttk.Entry(student_class_frame, textvariable=self.var_stu_ID, font=("times new roman", 12, "bold"), width=20)
        stu_id_entry.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        # Name
        name_label = Label(student_class_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        name_entry = ttk.Entry(student_class_frame, textvariable=self.var_name, font=("times new roman", 12, "bold"), width=20)
        name_entry.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        # Section
        sec_label = Label(student_class_frame, text="Section:", font=("times new roman", 12, "bold"), bg="white")
        sec_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        sec_entry = ttk.Entry(student_class_frame, textvariable=self.var_sec, font=("times new roman", 12, "bold"), width=20)
        sec_entry.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # Age
        age_label = Label(student_class_frame, text="Age:", font=("times new roman", 12, "bold"), bg="white")
        age_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        age_entry = ttk.Entry(student_class_frame, textvariable=self.var_age, font=("times new roman", 12, "bold"), width=20)
        age_entry.grid(row=1, column=3, padx=2, pady=5, sticky=W)

        # Gender
        gen_label = Label(student_class_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gen_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        gen_combo = ttk.Combobox(student_class_frame, textvariable=self.var_gen, font=("times new roman", 12, "bold"), width=18, state="readonly")
        gen_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gen_combo.current(0)
        gen_combo.grid(row=2, column=1, padx=2, pady=5, sticky=W)

        # Phone No
        pno_label = Label(student_class_frame, text="Phone No:", font=("times new roman", 12, "bold"), bg="white")
        pno_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        pno_entry = ttk.Entry(student_class_frame, textvariable=self.var_pno, font=("times new roman", 12, "bold"), width=20)
        pno_entry.grid(row=2, column=3, padx=2, pady=5, sticky=W)

        # Email
        email_label = Label(student_class_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        email_entry = ttk.Entry(student_class_frame, textvariable=self.var_email, font=("times new roman", 12, "bold"), width=20)
        email_entry.grid(row=3, column=1, padx=2, pady=5, sticky=W)

        # Bus Route
        bus_label = Label(student_class_frame, text="Bus Route:", font=("times new roman", 12, "bold"), bg="white")
        bus_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)
        bus_entry = ttk.Entry(student_class_frame, textvariable=self.var_bus, font=("times new roman", 12, "bold"), width=20)
        bus_entry.grid(row=3, column=3, padx=2, pady=5, sticky=W)

        # ==================== Buttons Frame ====================
        btn_frame = Frame(student_class_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=340, width=700, height=50)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=17)
        save_btn.grid(row=0, column=0, padx=5, pady=5)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=17)
        update_btn.grid(row=0, column=1, padx=5, pady=5)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=17)
        delete_btn.grid(row=0, column=2, padx=5, pady=5)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=17)
        reset_btn.grid(row=0, column=3, padx=5, pady=5)


        # ==================== Right Label Frame ====================
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=750, height=630)

        # Search System
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=5, width=730, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, textvariable=self.var_com_search, font=("times new roman", 12, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select Attribute", "Student_ID", "Phone", "Email")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, textvariable=self.var_search, font=("times new roman", 12, "bold"), width=20)
        search_entry.grid(row=0, column=2, padx=2, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", command=self.search_data, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=10)
        search_btn.grid(row=0, column=3, padx=5, pady=5)

        showall_btn = Button(search_frame, text="Show All", command=self.fetch_data, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=10)
        showall_btn.grid(row=0, column=4, padx=5, pady=5)

        # ==================== Table Frame ====================
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=80, width=730, height=520)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "sec", "age", "gen", "pno", "email", "bus"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("sec", text="Section")
        self.student_table.heading("age", text="Age")
        self.student_table.heading("gen", text="Gender")
        self.student_table.heading("pno", text="Phone No")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("bus", text="Bus Route")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("sec", width=100)
        self.student_table.column("age", width=50)
        self.student_table.column("gen", width=100)
        self.student_table.column("pno", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("bus", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)


    # ==================== Methods for GUI Functionality ====================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_stu_ID.get() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
            return

        try:
            data_tuple = (
                self.var_dep.get(), self.var_course.get(), self.var_year.get(),
                self.var_sem.get(), self.var_stu_ID.get(), self.var_name.get(),
                self.var_sec.get(), int(self.var_age.get()), self.var_gen.get(),
                self.var_pno.get(), self.var_email.get(), self.var_bus.get()
            )
            self.db.add_student(data_tuple)
            messagebox.showinfo("Success", "Student added successfully!", parent=self.root)
            self.fetch_data()
            self.reset_data()
        except Exception as ex:
            messagebox.showerror("Error", f"Failed to add student: {str(ex)}", parent=self.root)

    def fetch_data(self):
        records = self.db.fetch_all_students()
        if len(records) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in records:
                self.student_table.insert("", END, values=row)

    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content["values"]

        self.var_dep.set(row[0])
        self.var_course.set(row[1])
        self.var_year.set(row[2])
        self.var_sem.set(row[3])
        self.var_stu_ID.set(row[4])
        self.var_name.set(row[5])
        self.var_sec.set(row[6])
        self.var_age.set(row[7])
        self.var_gen.set(row[8])
        self.var_pno.set(row[9])
        self.var_email.set(row[10])
        self.var_bus.set(row[11])

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_stu_ID.get() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
            return

        try:
            data_tuple = (
                self.var_dep.get(), self.var_course.get(), self.var_year.get(),
                self.var_sem.get(), self.var_name.get(), self.var_sec.get(),
                int(self.var_age.get()), self.var_gen.get(), self.var_pno.get(),
                self.var_email.get(), self.var_bus.get(), self.var_stu_ID.get() # Student_ID is last for WHERE clause
            )
            self.db.update_student(data_tuple)
            messagebox.showinfo("Success", "Student data updated successfully!", parent=self.root)
            self.fetch_data()
            self.reset_data()
        except Exception as ex:
            messagebox.showerror("Error", f"Failed to update: {str(ex)}", parent=self.root)

    def delete_data(self):
        stu_id = self.var_stu_ID.get()
        if stu_id == "":
            messagebox.showerror("Error", "Student ID is required to delete!", parent=self.root)
            return

        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete student ID {stu_id}?", parent=self.root):
            try:
                self.db.delete_student(stu_id)
                messagebox.showinfo("Success", "Student data deleted successfully!", parent=self.root)
                self.reset_data()
                self.fetch_data()
            except Exception as ex:
                messagebox.showerror("Error", f"Failed to delete: {str(ex)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_stu_ID.set("")
        self.var_name.set("")
        self.var_sec.set("")
        self.var_age.set("")
        self.var_gen.set("Select Gender")
        self.var_pno.set("")
        self.var_email.set("")
        self.var_bus.set("")

    def search_data(self):
        search_by = self.var_com_search.get()
        search_term = self.var_search.get()

        if search_by == "Select Attribute" or search_term == "":
            messagebox.showerror("Error", "Please select a search attribute and enter a search term.", parent=self.root)
            return

        try:
            records = self.db.search_student(search_by, search_term)
            self.student_table.delete(*self.student_table.get_children())
            if records:
                for row in records:
                    self.student_table.insert("", END, values=row)
            else:
                messagebox.showinfo("Not Found", "No records match your search.", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Search Error: {str(ex)}", parent=self.root)