import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
import whisper
import threading
import sys
import io

# 🔧 Folder na modele
current_dir = os.path.dirname(os.path.abspath(__file__))
os.environ["XDG_CACHE_HOME"] = os.path.join(current_dir, "models")

stop_flag = False

class RedirectStdout(io.StringIO):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def write(self, s):
        self.text_widget.configure(state="normal")
        self.text_widget.insert("end", s)
        self.text_widget.see("end")
        self.text_widget.configure(state="disabled")

    def flush(self):
        pass

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) % 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

def split_text(text, max_words):
    words = text.split()
    return [' '.join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

def toggle_ui(state):
    output_entry.configure(state=state)
    words_entry.configure(state=state if split_var.get() else "disabled")
    model_menu.configure(state=state)
    transcribe_btn.configure(state=state)
    split_check.configure(state=state)
    stop_btn.configure(state="normal" if state == "disabled" else "disabled")

def stop_transcription():
    global stop_flag
    stop_flag = True
    log_text.configure(state="normal")
    log_text.insert("end", "\u26d4 Transkrypcja została przerwana przez użytkownika.\n")
    log_text.see("end")
    log_text.configure(state="disabled")

def transcribe():
    file_path = filedialog.askopenfilename(title="Wybierz plik audio lub wideo",
                                           filetypes=[("Audio/Video files", "*.mp3 *.wav *.m4a *.webm *.mp4 *.mkv")])
    if not file_path:
        return

    output_name = output_entry.get().strip()
    if not output_name:
        messagebox.showerror("Błąd", "Podaj nazwę pliku wyjściowego.")
        return

    model_size = model_var.get()
    max_words = int(words_entry.get()) if split_var.get() else None

    log_text.configure(state="normal")
    log_text.insert("end", f"\n>> Ładowanie modelu: {model_size}\n")
    log_text.configure(state="disabled")

    def run_transcription():
        global stop_flag
        stop_flag = False
        toggle_ui("disabled")

        try:
            model = whisper.load_model(model_size)
            log_text.configure(state="normal")
            log_text.insert("end", f">> Rozpoczęto transkrypcję...\n")
            log_text.configure(state="disabled")
            result = model.transcribe(file_path, language="pl", fp16=False)
            audio_duration = result["segments"][-1]["end"]
            srt_content = ""
            count = 1

            for segment in result["segments"]:
                if stop_flag:
                    log_text.configure(state="normal")
                    log_text.insert("end", "⚠️ Transkrypcja została przerwana.\n")
                    log_text.configure(state="disabled")
                    toggle_ui("normal")
                    return

                progress = int((segment["start"] / audio_duration) * 100)
                log_text.configure(state="normal")
                log_text.insert("end", f"▶️ {progress}% - {segment['text'].strip()}\n")
                log_text.see("end")
                log_text.configure(state="disabled")

                start_time = segment["start"]
                end_time = segment["end"]
                text = segment["text"].strip()

                if split_var.get() and max_words:
                    parts = split_text(text, max_words)
                    duration = (end_time - start_time) / len(parts)
                    for i, part in enumerate(parts):
                        start = format_timestamp(start_time + i * duration)
                        end = format_timestamp(start_time + (i + 1) * duration)
                        srt_content += f"{count}\n{start} --> {end}\n{part}\n\n"
                        count += 1
                else:
                    start = format_timestamp(start_time)
                    end = format_timestamp(end_time)
                    srt_content += f"{count}\n{start} --> {end}\n{text}\n\n"
                    count += 1

            out_path = os.path.join(os.path.dirname(file_path), output_name + ".srt")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(srt_content)

            log_text.configure(state="normal")
            log_text.insert("end", f"\n>> Napisy zapisane jako: {out_path}\n")
            log_text.configure(state="disabled")
            messagebox.showinfo("Gotowe", "Transkrypcja zakończona!")

        except Exception as e:
            log_text.configure(state="normal")
            log_text.insert("end", f"\n❌ Błąd: {e}\n")
            log_text.configure(state="disabled")
            messagebox.showerror("Błąd", str(e))

        finally:
            toggle_ui("normal")

    threading.Thread(target=run_transcription, daemon=True).start()

# === GUI ===
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Whisper Transkrypcja .srt")
root.geometry("740x640")

frame = ctk.CTkFrame(root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

output_label = ctk.CTkLabel(frame, text="Nazwa pliku wyjściowego (bez .srt):")
output_label.pack(pady=(10, 2))
output_entry = ctk.CTkEntry(frame, width=400)
output_entry.pack(pady=(0, 10))

model_label = ctk.CTkLabel(frame, text="Wybierz model Whispera:")
model_label.pack()
model_var = ctk.StringVar(value="medium")
model_menu = ctk.CTkOptionMenu(frame, variable=model_var, values=["tiny", "base", "small", "medium", "large", "turbo"])
model_menu.pack(pady=6)

split_var = ctk.BooleanVar(value=False)

split_check = ctk.CTkCheckBox(frame, text="Dziel segmenty na mniejsze frazy", variable=split_var, command=lambda: words_entry.configure(state="normal" if split_var.get() else "disabled"))
split_check.pack()

words_label = ctk.CTkLabel(frame, text="Ilość słów na frazę:")
words_label.pack()
words_entry = ctk.CTkEntry(frame, width=60)
words_entry.insert(0, "7")
words_entry.pack(pady=(0, 10))
words_entry.configure(state="disabled")

transcribe_btn = ctk.CTkButton(frame, text="Wybierz plik i transkrybuj", command=transcribe)
transcribe_btn.pack(pady=(0, 5))

stop_btn = ctk.CTkButton(frame, text="⛔ Przerwij transkrypcję", command=stop_transcription, state="disabled")
stop_btn.pack(pady=(0, 10))

log_text = ctk.CTkTextbox(frame, height=280, width=680)
log_text.pack(padx=10, pady=10)
log_text.configure(state="disabled")

sys.stdout = RedirectStdout(log_text)
sys.stderr = RedirectStdout(log_text)

root.protocol("WM_DELETE_WINDOW", lambda: (root.destroy(), sys.exit()))
root.mainloop()
