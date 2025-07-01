from youtube_transcript_api import YouTubeTranscriptApi
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from googletrans import Translator
from fpdf import FPDF
import os

lang_options = {
    'english': 'en',
    'french': 'fr',
    'spanish': 'es'
}

def get_youtube_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = ""
    for item in transcript:
        text += item['text'] + " "
    return text.strip()

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

def summarize_text(text, sentence_count=1, language='english'):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    result = " ".join(str(sentence) for sentence in summary)
    return result.strip()

def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    return url

def save_sum(transcript, summary, filename="transcript_summary.pdf"):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "YouTube Transcript and Summary", ln=True, align="C")

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Original Transcript:", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10, transcript)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Summary:", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10, summary)

    pdf.output(filename)
    return os.path.abspath(filename)
