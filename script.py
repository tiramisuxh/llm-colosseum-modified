import sys
from dotenv import load_dotenv
from eval.game import Game, Player1, Player2
from loguru import logger
from diambra.arena.utils.controller import create_devices_list
from tkinter import ttk, messagebox, Toplevel, Message
import tkinter as tk
from PIL import Image, ImageTk

logger.remove()
logger.add(sys.stdout, level="INFO")

load_dotenv()

# List of models Tested for the leaderboards
li_models = [
    "anthropic:claude-3-sonnet-20240229",
    "mistral:pixtral-large-latest",
    "mistral:pixtral-12b-2409",
    "anthropic:claude-3-haiku-20240307",
    "openai:gpt-4o",
    "openai:gpt-4o-mini",
    "anthropic:claude-3-sonnet-20240229",
]


# Starting with vision tournamennt
def game(
    model: str = "",
    device_idx: int = 0,
):
    # Environment Settings
    game = Game(
        render=True,
        player_1=None,
        # player_1=Player1(
        #     nickname="Baby",
        #     model="openai:gpt-4o-mini",
        #     robot_type="vision",
        #     temperature=0.7,
        # ),
        player_2=Player2(
            nickname="Baby",
            model=model,
            robot_type="vision",
            temperature=0.7,
        ),
        splash_screen=True,
        device_idx=device_idx,
    )
    return game.run()

def welcome():
    top = Toplevel()
    top.title('Welcome')
    Message(top, text="Loading...", padx=20, pady=20).pack()
    top.after(20000, top.destroy)

def selection():
    welcome()
    selected_model = model.get()
    selected_device = device.get()
    win_statement = game(
        model=selected_model,
        device_idx=int(selected_device[0]),
    )
    messagebox.showinfo("Winner", win_statement)

if __name__ == "__main__":
    main_window = tk.Tk()
    main_window.state('zoomed')

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    # Load placeholder images (replace with your images later)
    bg_image = ImageTk.PhotoImage(Image.open("sfbg.jpg").resize((screen_width, screen_height)))
    button_image = ImageTk.PhotoImage(Image.new("RGB", (100, 50), color="#3498db"))

    # Set background
    background_label = tk.Label(main_window, image=bg_image)
    background_label.place(relwidth=1, relheight=1)

    # Create a frame for layout management
    frame = ttk.Frame(main_window, padding="10")
    frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER, relwidth=0.3, relheight=0.3)

    # Configure grid layout
    frame.columnconfigure(1, weight=1)

    # Title
    title_label = ttk.Label(
        frame,
        text="LLM Colloseum",
        font=("Helvetica", 20, "bold"),
        foreground="white",
        background="#2c3e50",
    )
    title_label.grid(column=0, row=0, columnspan=2, pady=10)

    # Model selection
    ttk.Label(frame, text="Select Model:", font=("Helvetica", 14), foreground="white", background="#2c3e50").grid(
        column=0, row=1, sticky=tk.W, padx=10, pady=10
    )
    model = ttk.Combobox(frame, state="readonly", values=li_models, font=("Helvetica", 14))
    model.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=10, pady=10)

    # Device selection with larger labels and combobox
    ttk.Label(frame, text="Select Device:", font=("Helvetica", 14), foreground="white", background="#2c3e50").grid(
        column=0, row=2, sticky=tk.W, padx=10, pady=10
    )
    device = ttk.Combobox(frame, state="readonly", values=create_devices_list(), font=("Helvetica", 14))
    device.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=10, pady=10)

    # Start button
    start_button = tk.Button(
        frame,
        text="Start",
        image=button_image,
        compound=tk.CENTER,
        font=("Helvetica", 16, "bold"),
        fg="white",
        bg="#3498db",
        command=selection,
    )
    start_button.grid(column=0, row=3, columnspan=2, pady=10)

    # Keep a reference to images to prevent garbage collection
    main_window.bg_image = bg_image
    main_window.button_image = button_image

    main_window.mainloop()
    
