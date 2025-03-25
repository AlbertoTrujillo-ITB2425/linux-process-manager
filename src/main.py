import tkinter as tk
from tkinter import messagebox
import psutil
import subprocess
import os

class ProcessManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Procesos y Servicios en Linux")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Título
        self.title_label = tk.Label(self.root, text="Gestión de Procesos y Servicios", font=("Arial", 20), pady=10)
        self.title_label.pack()

        # Frame para los procesos
        self.process_frame = tk.LabelFrame(self.root, text="Procesos Activos", font=("Arial", 14), padx=10, pady=10)
        self.process_frame.pack(padx=20, pady=10, fill="both", expand="yes")

        # Listbox para mostrar los procesos
        self.process_listbox = tk.Listbox(self.process_frame, width=50, height=10)
        self.process_listbox.pack(padx=10, pady=10)

        # Botón para actualizar lista de procesos
        self.update_process_button = tk.Button(self.process_frame, text="Actualizar Procesos", command=self.update_processes)
        self.update_process_button.pack(padx=10, pady=10)

        # Frame para servicios
        self.service_frame = tk.LabelFrame(self.root, text="Gestión de Servicios", font=("Arial", 14), padx=10, pady=10)
        self.service_frame.pack(padx=20, pady=10, fill="both", expand="yes")

        # Botones para gestionar servicios
        self.start_service_button = tk.Button(self.service_frame, text="Arrancar Servicio", command=self.start_service)
        self.start_service_button.pack(padx=10, pady=5)

        self.stop_service_button = tk.Button(self.service_frame, text="Detener Servicio", command=self.stop_service)
        self.stop_service_button.pack(padx=10, pady=5)

        self.enable_service_button = tk.Button(self.service_frame, text="Habilitar Servicio", command=self.enable_service)
        self.enable_service_button.pack(padx=10, pady=5)

        self.disable_service_button = tk.Button(self.service_frame, text="Deshabilitar Servicio", command=self.disable_service)
        self.disable_service_button.pack(padx=10, pady=5)

        # Frame para estadísticas
        self.stats_frame = tk.LabelFrame(self.root, text="Estadísticas del Sistema", font=("Arial", 14), padx=10, pady=10)
        self.stats_frame.pack(padx=20, pady=10, fill="both", expand="yes")

        # Etiquetas para mostrar CPU y Memoria
        self.cpu_label = tk.Label(self.stats_frame, text="Uso de CPU: 0%", font=("Arial", 12))
        self.cpu_label.pack(padx=10, pady=5)

        self.memory_label = tk.Label(self.stats_frame, text="Uso de Memoria: 0%", font=("Arial", 12))
        self.memory_label.pack(padx=10, pady=5)

        # Actualización de estadísticas
        self.update_stats()

    def update_processes(self):
        # Limpiar la lista
        self.process_listbox.delete(0, tk.END)

        # Listar procesos activos
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            process_info = f"PID: {proc.info['pid']} - {proc.info['name']} - CPU: {proc.info['cpu_percent']}% - Memoria: {proc.info['memory_percent']}%"
            self.process_listbox.insert(tk.END, process_info)

    def start_service(self):
        service_name = self.prompt_for_service("Ingrese el nombre del servicio a arrancar:")
        if service_name:
            try:
                subprocess.run(['sudo', 'systemctl', 'start', service_name], check=True)
                messagebox.showinfo("Éxito", f"Servicio {service_name} arrancado correctamente.")
            except subprocess.CalledProcessError:
                messagebox.showerror("Error", f"No se pudo arrancar el servicio {service_name}.")

    def stop_service(self):
        service_name = self.prompt_for_service("Ingrese el nombre del servicio a detener:")
        if service_name:
            try:
                subprocess.run(['sudo', 'systemctl', 'stop', service_name], check=True)
                messagebox.showinfo("Éxito", f"Servicio {service_name} detenido correctamente.")
            except subprocess.CalledProcessError:
                messagebox.showerror("Error", f"No se pudo detener el servicio {service_name}.")

    def enable_service(self):
        service_name = self.prompt_for_service("Ingrese el nombre del servicio a habilitar:")
        if service_name:
            try:
                subprocess.run(['sudo', 'systemctl', 'enable', service_name], check=True)
                messagebox.showinfo("Éxito", f"Servicio {service_name} habilitado para el inicio automático.")
            except subprocess.CalledProcessError:
                messagebox.showerror("Error", f"No se pudo habilitar el servicio {service_name}.")

    def disable_service(self):
        service_name = self.prompt_for_service("Ingrese el nombre del servicio a deshabilitar:")
        if service_name:
            try:
                subprocess.run(['sudo', 'systemctl', 'disable', service_name], check=True)
                messagebox.showinfo("Éxito", f"Servicio {service_name} deshabilitado para el inicio automático.")
            except subprocess.CalledProcessError:
                messagebox.showerror("Error", f"No se pudo deshabilitar el servicio {service_name}.")

    def prompt_for_service(self, prompt_text):
        service_name = tk.simpledialog.askstring("Servicio", prompt_text)
        return service_name

    def update_stats(self):
        # Obtener estadísticas del sistema
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent

        # Actualizar las etiquetas de estadísticas
        self.cpu_label.config(text=f"Uso de CPU: {cpu_usage}%")
        self.memory_label.config(text=f"Uso de Memoria: {memory_usage}%")

        # Llamar a la actualización cada 1 segundo
        self.root.after(1000, self.update_stats)


if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()

    # Crear la aplicación
    app = ProcessManagerApp(root)

    # Iniciar la aplicación
    root.mainloop()
