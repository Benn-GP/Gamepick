import random
import tkinter as tk
from tkinter import ttk


def normalizar_categoria(categoria):
    """Convierte valores con o sin tilde a una categoría estándar."""
    mapa = {
        "accion / aventura": "Acción / Aventura",
        "acción / aventura": "Acción / Aventura",
        "competitivo": "Competitivo",
        "peleas": "Peleas",
        "retro": "Retro / Clásicos",
        "retro / clásicos": "Retro / Clásicos",
        "retro / clasicos": "Retro / Clásicos",
        "rpg": "RPG",
        "carreras": "Carreras",
    }
    return mapa.get(categoria.strip().lower(), categoria.strip())


def normalizar_epoca(epoca):
    """Normaliza las épocas para que el programa sea más robusto."""
    valor = epoca.strip().lower()
    if valor in ("clasico", "clásico"):
        return "Clásico"
    if valor == "moderno":
        return "Moderno"
    if valor == "cualquiera":
        return "Cualquiera"
    return epoca.strip()


def obtener_juegos():
    """Base de datos sencilla con juegos por categoría y época."""
    return {
        "Competitivo": {
            "Moderno": [
                ("VALORANT", "Competitivo", "Shooter táctico con rondas, precisión y trabajo en equipo."),
                ("Dota 2", "Competitivo", "Estrategia intensa, habilidades únicas y partidas complejas."),
                ("Counter-Strike 2", "Competitivo", "Disparos competitivos con estrategia, puntería y coordinación."),
            ],
            "Clásico": [
                ("Quake", "Competitivo", "Shooter clásico muy rápido y muy competitivo."),
                ("StarCraft", "Competitivo", "Estrategia clásica con decisiones rápidas y profundas."),
                ("Warcraft III", "Competitivo", "Batallas estratégicas con múltiples razas y habilidades."),
            ],
            "Cualquiera": [
                ("VALORANT", "Competitivo", "Shooter táctico con rondas, precisión y trabajo en equipo."),
                ("Dota 2", "Competitivo", "Estrategia intensa, habilidades únicas y partidas complejas."),
                ("Quake", "Competitivo", "Shooter clásico muy rápido y muy competitivo."),
            ],
        },
        "Acción / Aventura": {
            "Moderno": [
                ("God of War", "Acción / Aventura", "Aventura épica con combates fuertes y una historia emocionante."),
                ("Marvel's Spider-Man", "Acción / Aventura", "Exploración, acrobacias y acción en una gran ciudad."),
                ("Horizon Forbidden West", "Acción / Aventura", "Mundo abierto, exploración y combates contra máquinas gigantes."),
            ],
            "Clásico": [
                ("Mega Man X", "Acción / Aventura", "Acción, plataformas y habilidades especiales muy memorables."),
                ("The Legend of Zelda", "Acción / Aventura", "Exploración, enigmas y aventuras clásicas muy completas."),
                ("Castlevania", "Acción / Aventura", "Acción intensa con un estilo clásico y muy desafiante."),
            ],
            "Cualquiera": [
                ("God of War", "Acción / Aventura", "Aventura épica con combates fuertes y una historia emocionante."),
                ("Mega Man X", "Acción / Aventura", "Acción, plataformas y habilidades especiales muy memorables."),
                ("Marvel's Spider-Man", "Acción / Aventura", "Exploración, acrobacias y acción en una gran ciudad."),
            ],
        },
        "Peleas": {
            "Moderno": [
                ("Tekken 8", "Peleas", "Peleas modernas con personajes muy variados y combates intensos."),
                ("Street Fighter 6", "Peleas", "Combates rápidos, estilo y estrategias muy dinámicas."),
                ("Mortal Kombat 1", "Peleas", "Peleas brutales con mucha intensidad y personajes icónicos."),
            ],
            "Clásico": [
                ("Tekken 3", "Peleas", "Un clásico de peleas con una gran cantidad de personajes y acción."),
                ("Street Fighter II", "Peleas", "Referencia básica del género, rápida y muy popular."),
                ("Mortal Kombat 3", "Peleas", "Peleas clásicas con estilo arcade y mucha energía."),
            ],
            "Cualquiera": [
                ("Tekken 3", "Peleas", "Un clásico de peleas con una gran cantidad de personajes y acción."),
                ("Street Fighter 6", "Peleas", "Combates rápidos, estilo y estrategias muy dinámicas."),
                ("Mortal Kombat 1", "Peleas", "Peleas brutales con mucha intensidad y personajes icónicos."),
            ],
        },
        "Retro / Clásicos": {
            "Moderno": [
                ("Mega Man 11", "Retro / Clásicos", "Juego moderno que honra la esencia de los clásicos de acción."),
                ("Sonic Mania", "Retro / Clásicos", "Pasa la nostalgia a una nueva generación con un estilo clásico."),
                ("Street Fighter 30th Anniversary", "Retro / Clásicos", "Colección retro con mucha historia del arcade clásico."),
            ],
            "Clásico": [
                ("Bomberman", "Retro / Clásicos", "Clásico de estrategia y explosivos muy divertido."),
                ("Super Mario Bros.", "Retro / Clásicos", "Plataformas inmortal con gran nivel de dificultad y diversión."),
                ("Pac-Man", "Retro / Clásicos", "Época dorada del arcade con un gameplay simple y adictivo."),
            ],
            "Cualquiera": [
                ("Bomberman", "Retro / Clásicos", "Clásico de estrategia y explosivos muy divertido."),
                ("Super Mario Bros.", "Retro / Clásicos", "Plataformas inmortal con gran nivel de dificultad y diversión."),
                ("Sonic Mania", "Retro / Clásicos", "Pasa la nostalgia a una nueva generación con un estilo clásico."),
            ],
        },
        "RPG": {
            "Moderno": [
                ("Elden Ring", "RPG", "RPG de acción con exploración, combate y una historia intensa."),
                ("The Witcher 3", "RPG", "Mundo abierto, decisiones clave y aventuras muy profundas."),
                ("Baldur's Gate 3", "RPG", "RPG táctico y narrativo con decisiones importantes."),
            ],
            "Clásico": [
                ("Final Fantasy VII", "RPG", "RPG clásico con historia, personajes y una gran relevancia."),
                ("Chrono Trigger", "RPG", "RPG icónico con viajes en el tiempo y varios finales."),
                ("Pokémon Red", "RPG", "Clásico RPG de exploración, evolución y estrategia."),
            ],
            "Cualquiera": [
                ("Elden Ring", "RPG", "RPG de acción con exploración, combate y una historia intensa."),
                ("Final Fantasy VII", "RPG", "RPG clásico con historia, personajes y una gran relevancia."),
                ("The Witcher 3", "RPG", "Mundo abierto, decisiones clave y aventuras muy profundas."),
            ],
        },
        "Carreras": {
            "Moderno": [
                ("Mario Kart 8 Deluxe", "Carreras", "Carreras rápidas, objetos, personajes famosos y mucha diversión."),
                ("Forza Horizon 5", "Carreras", "Autos, velocidad y un mundo abierto con gran variedad."),
                ("Gran Turismo 7", "Carreras", "Simulador serio con gran detalle y mucha sensación realista."),
            ],
            "Clásico": [
                ("Mario Kart 64", "Carreras", "Clásico de carreras con gran estilo y partidas muy entretenidas."),
                ("F-Zero", "Carreras", "Carreras futuristas rápidas y muy desafiantes."),
                ("Crash Team Racing", "Carreras", "Carreras con personajes y una gran dosis de caos."),
            ],
            "Cualquiera": [
                ("Mario Kart 8 Deluxe", "Carreras", "Carreras rápidas, objetos, personajes famosos y mucha diversión."),
                ("Mario Kart 64", "Carreras", "Clásico de carreras con gran estilo y partidas muy entretenidas."),
                ("Forza Horizon 5", "Carreras", "Autos, velocidad y un mundo abierto con gran variedad."),
            ],
        },
    }


def recomendar_juego(categoria, epoca):
    """Devuelve un juego aleatorio según la categoría y la época."""
    categoria = normalizar_categoria(categoria)
    epoca = normalizar_epoca(epoca)

    juegos = obtener_juegos()
    if categoria not in juegos:
        return None

    if epoca == "Cualquiera":
        opciones = juegos[categoria]["Moderno"] + juegos[categoria]["Clásico"]
    else:
        opciones = juegos[categoria].get(epoca, [])

    if not opciones:
        return None

    return random.choice(opciones)


def mostrar_recomendacion(combo_categoria, combo_epoca, resultado):
    """Muestra el juego sugerido en el área de texto."""
    categoria = combo_categoria.get()
    epoca = combo_epoca.get()

    if not categoria or not epoca:
        resultado.delete("1.0", tk.END)
        resultado.insert(tk.END, "Selecciona una categoría y una época antes de recomendar.")
        return

    juego = recomendar_juego(categoria, epoca)
    resultado.delete("1.0", tk.END)

    if juego is None:
        resultado.insert(tk.END, "No se encontró una recomendación para esa combinación.")
        return

    nombre, genero, descripcion = juego
    resultado.insert(tk.END, "🎮 RECOMENDACIÓN\n\n")
    resultado.insert(tk.END, f"Juego: {nombre}\n")
    resultado.insert(tk.END, f"Categoría: {genero}\n")
    resultado.insert(tk.END, f"Época: {epoca}\n")
    resultado.insert(tk.END, f"Descripción: {descripcion}")


def limpiar_formulario(combo_categoria, combo_epoca, resultado):
    """Reinicia la interfaz y borra el resultado."""
    combo_categoria.set("Competitivo")
    combo_epoca.set("Cualquiera")
    resultado.delete("1.0", tk.END)


def sorprender(resultado):
    """Muestra una recomendación aleatoria sin filtros."""
    juegos = [
        ("VALORANT", "Competitivo", "Shooter táctico con rondas, precisión y trabajo en equipo."),
        ("Dota 2", "Competitivo", "Estrategia intensa, habilidades únicas y partidas complejas."),
        ("Mega Man X", "Acción / Aventura", "Acción, plataformas y habilidades especiales muy memorables."),
        ("God of War", "Acción / Aventura", "Aventura épica con combates fuertes y una historia emocionante."),
        ("Tekken 3", "Peleas", "Un clásico de peleas con una gran cantidad de personajes y acción."),
        ("Bomberman", "Retro / Clásicos", "Clásico de estrategia y explosivos muy divertido."),
        ("Elden Ring", "RPG", "RPG de acción con exploración, combate y una historia intensa."),
        ("Mario Kart 8 Deluxe", "Carreras", "Carreras rápidas, objetos, personajes famosos y mucha diversión."),
    ]

    nombre, genero, descripcion = random.choice(juegos)
    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, "🎲 ¡SORPRESA!\n\n")
    resultado.insert(tk.END, f"Juego: {nombre}\n")
    resultado.insert(tk.END, f"Categoría: {genero}\n")
    resultado.insert(tk.END, f"Descripción: {descripcion}")


def main():
    """Crea la ventana principal y organiza la interfaz."""
    ventana = tk.Tk()
    ventana.title("GamePick - Recomendador de Videojuegos")
    ventana.geometry("560x520")
    ventana.resizable(False, False)

    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure("TLabel", font=("Arial", 11))
    estilo.configure("Titulo.TLabel", font=("Arial", 20, "bold"), foreground="#1f2937")
    estilo.configure("TButton", font=("Arial", 10, "bold"))

    contenedor = ttk.Frame(ventana, padding=20)
    contenedor.pack(fill="both", expand=True)

    ttk.Label(contenedor, text="🎮 GAMEPICK", style="Titulo.TLabel").pack(pady=(0, 5))
    ttk.Label(contenedor, text="Descubre tu próximo videojuego").pack(pady=(0, 20))
    
    marco = ttk.Frame(contenedor)
    marco.pack(fill="x")

    ttk.Label(marco, text="Categoría:").grid(row=0, column=0, sticky="w", padx=(0, 10), pady=8)
    categorias = [
        "Competitivo",
        "Acción / Aventura",
        "Peleas",
        "Retro / Clásicos",
        "RPG",
        "Carreras",
    ]
    combo_categoria = ttk.Combobox(marco, values=categorias, state="readonly", width=28)
    combo_categoria.set("Competitivo")
    combo_categoria.grid(row=0, column=1, sticky="ew", pady=8)

    ttk.Label(marco, text="Época:").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=8)
    combo_epoca = ttk.Combobox(marco, values=["Moderno", "Clásico", "Cualquiera"], state="readonly", width=28)
    combo_epoca.set("Cualquiera")
    combo_epoca.grid(row=1, column=1, sticky="ew", pady=8)

    marco.columnconfigure(1, weight=1)

    botones = ttk.Frame(contenedor)
    botones.pack(fill="x", pady=(20, 10))

    ttk.Button(botones, text="🎮 Recomendar", command=lambda: mostrar_recomendacion(combo_categoria, combo_epoca, resultado)).pack(side="left", padx=(0, 8))
    ttk.Button(botones, text="🎲 Sorpréndeme", command=lambda: sorprender(resultado)).pack(side="left", padx=8)
    ttk.Button(botones, text="Limpiar", command=lambda: limpiar_formulario(combo_categoria, combo_epoca, resultado)).pack(side="left", padx=8)
    ttk.Button(botones, text="Salir", command=ventana.destroy).pack(side="left", padx=8)

    ttk.Label(contenedor, text="Resultado:").pack(anchor="w", pady=(10, 5))
    resultado = tk.Text(contenedor, height=11, width=58, wrap="word", font=("Arial", 10))
    resultado.pack(fill="both", expand=True)

    resultado.insert(tk.END, "Selecciona una categoría y presiona Recomendar para ver una recomendación.")

    ventana.mainloop()


if __name__ == "__main__":
    main()