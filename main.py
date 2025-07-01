import tkinter as tk
from tkinter import messagebox
from ui import YTS
import sum

def on_submit(url_or_id, selected_language):
    try:
        video_id = sum.extract_video_id(url_or_id)

        transcript = sum.get_youtube_transcript(video_id)
        ui.update_transcript(transcript)

        if selected_language != 'english':
            transcript = sum.translate_text(transcript, sum.lang_options[selected_language])

        summary = sum.summarize_text(transcript, 5, selected_language)
        ui.update_summary(summary)
        
    except Exception as e:
        ui.show_error("An error occurred:\n" + str(e))

def save_pdf(transcript, summary):
    try:
        filename = sum.save_sum(transcript, summary)
        messagebox.showinfo("Success", "PDF saved successfully as " + filename)
    except Exception as e:
        messagebox.showerror("Error", "Failed to save PDF:\n" + str(e))

window = tk.Tk()

ui = YTS(window, on_submit, save_pdf)
window.mainloop()

#id: MS5UjNKw_1M
#6F8wFkScnME
