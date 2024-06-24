import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from city import City
from travel import Travel
import search_algorithms
import organizer

class MetroTravelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Metro Travel")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")

        self.cities = City.loader()
        self.travels = Travel.loader()

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use('clam')

        # Configuración de los selectores
        style.configure("TRadiobutton", background="#f0f0f0", font=("Helvetica", 12))
        style.map("TRadiobutton", background=[('active', '#d9d9d9')])

        # Estilo para los OptionMenu
        style.configure("TMenubutton", background="#d9d9d9", foreground="#000000", font=("Helvetica", 12), borderwidth=2, relief="solid")
        style.map("TMenubutton", background=[('active', '#c0c0c0')])

        # Estilo para los botones
        style.configure("TButton", font=("Helvetica", 14), padding=10, background="#4CAF50", foreground="#ffffff", borderwidth=0)
        style.map("TButton", background=[('active', '#45a049')])

        # Estilo para las etiquetas
        style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 14))

        title_label = ttk.Label(self.root, text="Metro Travel", font=("Helvetica", 24, "bold"))
        title_label.pack(pady=10)

        self.visa_label = ttk.Label(self.root, text="¿El pasajero tiene visa?")
        self.visa_label.pack(pady=5)

        self.visa_var = tk.IntVar()
        self.visa_yes = ttk.Radiobutton(self.root, text="Sí", variable=self.visa_var, value=1, style="TRadiobutton", command=self.update_menus)
        self.visa_no = ttk.Radiobutton(self.root, text="No", variable=self.visa_var, value=0, style="TRadiobutton", command=self.update_menus)
        self.visa_yes.pack()
        self.visa_no.pack()

        self.origin_label = ttk.Label(self.root, text="Seleccione la ciudad origen:")
        self.origin_label.pack(pady=5)
        self.origin_var = tk.StringVar()
        self.origin_menu = ttk.OptionMenu(self.root, self.origin_var, "")
        self.origin_menu.pack()

        self.destination_label = ttk.Label(self.root, text="Seleccione la ciudad destino:")
        self.destination_label.pack(pady=5)
        self.destination_var = tk.StringVar()
        self.destination_menu = ttk.OptionMenu(self.root, self.destination_var, "")
        self.destination_menu.pack()

        self.route_type_label = ttk.Label(self.root, text="¿Qué tipo de ruta desea?")
        self.route_type_label.pack(pady=5)

        self.route_type_var = tk.IntVar()
        self.route_type_cost = ttk.Radiobutton(self.root, text="Ruta menos costosa", variable=self.route_type_var, value=1, style="TRadiobutton")
        self.route_type_hops = ttk.Radiobutton(self.root, text="Ruta con menos escalas", variable=self.route_type_var, value=2, style="TRadiobutton")
        self.route_type_cost.pack()
        self.route_type_hops.pack()

        self.submit_button = ttk.Button(self.root, text="Calcular Ruta", command=self.calculate_route, style="TButton")
        self.submit_button.pack(pady=10)

        self.result_label = ttk.Label(self.root, text="", wraplength=500)
        self.result_label.pack(pady=10)

        # Inicializar los OptionMenus
        self.update_menus()

    def update_menus(self):
        has_visa = self.visa_var.get() == 1

        if has_visa:
            cities = self.cities
        else:
            cities = organizer.cities_without_visa(self.cities)

        cities_names = [city.name for city in cities]

        self.origin_menu["menu"].delete(0, "end")
        self.destination_menu["menu"].delete(0, "end")

        for city_name in cities_names:
            self.origin_menu["menu"].add_command(label=city_name, command=tk._setit(self.origin_var, city_name))
            self.destination_menu["menu"].add_command(label=city_name, command=tk._setit(self.destination_var, city_name))

        self.origin_var.set(cities_names[0] if cities_names else "")
        self.destination_var.set(cities_names[0] if cities_names else "")

    def calculate_route(self):
        has_visa = self.visa_var.get() == 1
        origin_name = self.origin_var.get()
        destination_name = self.destination_var.get()
        route_type = self.route_type_var.get()

        if not origin_name or not destination_name or route_type == 0:
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            return

        origin_city = next(city for city in self.cities if city.name == origin_name)
        destination_city = next(city for city in self.cities if city.name == destination_name)

        if has_visa:
            cities_to_apply = self.cities
            travels_to_apply = self.travels
        else:
            cities_to_apply = organizer.cities_without_visa(self.cities)
            travels_to_apply = organizer.travels_without_visa(cities_to_apply, self.travels)

        origin_code = origin_city.code
        destination_code = destination_city.code

        # Verificar el grafo
        graph = {city.code: set() for city in cities_to_apply}
        for travel in travels_to_apply:
            graph[travel.origin].add(travel.destination)
            graph[travel.destination].add(travel.origin)  # Añadir para caminos bidireccionales


        # Validar que los nodos de origen y destino existen en el grafo
        if origin_code not in graph or destination_code not in graph:
            messagebox.showerror("Error", "La ciudad de origen o destino no está disponible en el grafo.")
            return

        if route_type == 1:
            cost, route = search_algorithms.dijkstra(cities_to_apply, travels_to_apply, origin_code, destination_code)
            result_text = f"La ruta más barata desde {origin_city.name} ({origin_city.code}) hasta {destination_city.name} ({destination_city.code}) cuesta $ {cost} y es {route}"
        else:
            hops, path = search_algorithms.dijkstra_min_cities(cities_to_apply, travels_to_apply, origin_code, destination_code)
            result_text = f"El número mínimo de ciudades a pasar es: {hops} y la ruta es {path}"

        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = MetroTravelApp(root)
    root.mainloop()
