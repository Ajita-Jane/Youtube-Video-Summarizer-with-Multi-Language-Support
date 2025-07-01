import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk

class YTS:
    def __init__(self, window, submit_callback, save_pdf_callback):
        self.window = window
        self.window.title("YouTube Transcript Summarizer")

        self.submit_callback = submit_callback
        self.save_pdf_callback = save_pdf_callback

        self.create_widgets()

    def create_widgets(self):
        image = Image.open("D://Jane//1. College//7. Semester VII//MP temp//ytl1.jpg")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.window, image=photo)
        label.photo = photo 
        label.pack()

        l_url = tk.Label(self.window, text="Enter YouTube video URL or ID:")
        l_url.pack(pady=5)

        self.url = tk.Entry(self.window, width=40)
        self.url.pack(pady=5)

        l_lang = tk.Label(self.window, text="Select a Language:")
        l_lang.pack(pady=5)

        self.lang_var = tk.StringVar(value='english')
        menu = tk.OptionMenu(self.window, self.lang_var, 'english', 'french', 'spanish')
        menu.pack(pady=5)

        btn_submit = tk.Button(self.window, text="Submit", command=self.submit)
        btn_submit.pack(pady=10)

        l_trans = tk.Label(self.window, text="Original Transcript:")
        l_trans.pack(pady=5)

        self.txt_trans = scrolledtext.ScrolledText(self.window, width=60, height=10, wrap=tk.WORD)
        self.txt_trans.pack(pady=5)

        l_sum = tk.Label(self.window, text="Summary:")
        l_sum.pack(pady=5)

        self.txt_sum = scrolledtext.ScrolledText(self.window, width=60, height=10, wrap=tk.WORD)
        self.txt_sum.pack(pady=5)

        self.lbl_word_count = tk.Label(self.window, text="")
        self.lbl_word_count.pack(pady=5)

        self.lbl_efficiency = tk.Label(self.window, text="")
        self.lbl_efficiency.pack(pady=5)

        btn_save = tk.Button(self.window, text="Save Summary", command=self.save_pdf)
        btn_save.pack(pady=5)

    def submit(self):
        url_or_id = self.url.get().strip()
        selected_language = self.lang_var.get()
        print(f"Submit pressed. URL/ID: {url_or_id}, Language: {selected_language}")
        self.submit_callback(url_or_id, selected_language)

    def save_pdf(self):
        transcript = self.txt_trans.get(1.0, tk.END).strip()
        summary = self.txt_sum.get(1.0, tk.END).strip()
        print(f"Save PDF pressed. Transcript: {len(transcript.split())} words, Summary: {len(summary.split())} words")
        self.save_pdf_callback(transcript, summary)

    def update_transcript(self, transcript):
        print(f"Updating transcript. Word count: {len(transcript.split())}")
        self.txt_trans.delete(1.0, tk.END)
        self.txt_trans.insert(tk.END, transcript)
        self.update_word_count()

    def update_summary(self, summary):
        print(f"Updating summary. Word count: {len(summary.split())}")
        self.txt_sum.delete(1.0, tk.END)
        self.txt_sum.insert(tk.END, summary)
        self.update_word_count()

    def update_word_count(self):
        transcript = self.txt_trans.get(1.0, tk.END).strip()
        summary = self.txt_sum.get(1.0, tk.END).strip()

        transcript_word_count = len(transcript.split())
        summary_word_count = len(summary.split())

        print(f"Transcript word count: {transcript_word_count}, Summary word count: {summary_word_count}")
        self.lbl_word_count.config(text=f"Transcript Words: {transcript_word_count}, Summary Words: {summary_word_count}")
        self.update_efficiency(transcript_word_count, summary_word_count)

    def update_efficiency(self, transcript_word_count, summary_word_count):
        if transcript_word_count > 0:
            efficiency = (summary_word_count / transcript_word_count) * 100
            print(f"Efficiency: {efficiency:.2f}%")
            self.lbl_efficiency.config(text=f"Efficiency: {efficiency:.2f}%")
        else:
            print("No transcript words, efficiency N/A")
            self.lbl_efficiency.config(text="Efficiency: N/A")

    def show_error(self, message):
        print(f"Error: {message}")
        messagebox.showerror("Error", message)
