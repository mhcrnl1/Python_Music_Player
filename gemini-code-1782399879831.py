import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Music Player")
        self.root.geometry("400x200")
        self.root.config(bg="#2c3e50")

        # Initialize Pygame Mixer
        pygame.mixer.init()

        # Track State
        self.current_file = None

        # --- UI Elements ---
        
        # Track Name Label
        self.track_label = tk.Label(
            self.root, 
            text="No track selected", 
            bg="#2c3e50", 
            fg="white", 
            font=("Helvetica", 12)
        )
        self.track_label.pack(pady=20)

        # Button Frame
        self.button_frame = tk.Frame(self.root, bg="#2c3e50")
        self.button_frame.pack()

        # Buttons
        self.load_btn = tk.Button(self.button_frame, text="Load", command=self.load_music, width=8)
        self.load_btn.grid(row=0, column=0, padx=5)

        self.play_btn = tk.Button(self.button_frame, text="Play", command=self.play_music, width=8)
        self.play_btn.grid(row=0, column=1, padx=5)

        self.pause_btn = tk.Button(self.button_frame, text="Pause", command=self.pause_music, width=8)
        self.pause_btn.grid(row=0, column=2, padx=5)

        self.resume_btn = tk.Button(self.button_frame, text="Resume", command=self.resume_music, width=8)
        self.resume_btn.grid(row=0, column=3, padx=5)

        self.stop_btn = tk.Button(self.button_frame, text="Stop", command=self.stop_music, width=8)
        self.stop_btn.grid(row=0, column=4, padx=5)

    # --- Player Functions ---

    def load_music(self):
        # Open file explorer to select an audio file
        file_path = filedialog.askopenfilename(
            title="Select a Song",
            filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")]
        )
        if file_path:
            self.current_file = file_path
            # Extract just the file name from the path
            song_name = file_path.split("/")[-1]
            self.track_label.config(text=f"Loaded: {song_name}")
            pygame.mixer.music.load(self.current_file)

    def play_music(self):
        if self.current_file:
            pygame.mixer.music.play()
            self.track_label.config(fg="#2ecc71") # Turn text green when playing

    def pause_music(self):
        if self.current_file:
            pygame.mixer.music.pause()
            self.track_label.config(fg="#f1c40f") # Turn text yellow when paused

    def resume_music(self):
        if self.current_file:
            pygame.mixer.music.unpause()
            self.track_label.config(fg="#2ecc71")

    def stop_music(self):
        if self.current_file:
            pygame.mixer.music.stop()
            self.track_label.config(fg="white")

# --- Main Application Loop ---
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()