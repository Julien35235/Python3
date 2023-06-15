def openfilleNavigationsMethod():
    import tkinter as tk
    from tkinter import messagebox

    def open_waze():
        messagebox.showinfo("Navigation", "Ouverture de l'application Waze...")

    def open_google_maps():
        messagebox.showinfo("Navigation", "Ouverture de l'application Google Maps...")

    def open_ios_plans():
        messagebox.showinfo("Navigation", "Ouverture de l'application Plans (iOS)...")

    def open_tomtom():
        messagebox.showinfo("Navigation", "Ouverture de l'application TomTom...")

    def open_garmin_drive():
        messagebox.showinfo("Navigation", "Ouverture de l'application Garmin Drive...")

    def main_menu():
        root = tk.Tk()
        root.title("Menu de navigation")

        waze_button = tk.Button(root, text="Waze", command=open_waze)
        waze_button.pack()

        google_maps_button = tk.Button(root, text="Google Maps", command=open_google_maps)
        google_maps_button.pack()

        ios_plans_button = tk.Button(root, text="Plans (iOS)", command=open_ios_plans)
        ios_plans_button.pack()

        tomtom_button = tk.Button(root, text="TomTom", command=open_tomtom)
        tomtom_button.pack()

        garmin_drive_button = tk.Button(root, text="Garmin Drive", command=open_garmin_drive)
        garmin_drive_button.pack()

        root.mainloop()

    if __name__ == "__main__":
        main_menu()
