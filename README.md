# 🎙️ Whisper Transkrypcja GUI

Whisper Transkrypcja GUI to aplikacja do automatycznej transkrypcji audio i wideo na napisy `.srt`. Zbudowana na bazie modelu **Whisper** od OpenAI, oferuje łatwy w obsłudze interfejs graficzny (GUI) pozwalający na szybkie przekształcanie dźwięku z filmów, podcastów i innych nagrań audio na tekst.

Aplikacja działa lokalnie i obsługuje pliki audio i wideo w popularnych formatach takich jak `.mp3`, `.wav`, `.mp4` czy `.mkv`. Dzięki wykorzystaniu modelu Whisper, transkrypcja jest szybka i precyzyjna, a możliwość podziału na krótkie frazy zwiększa czytelność napisów.

## 🚀 Funkcje
- 🖥️ Przyjazny interfejs graficzny (ciemny motyw)
- 🔈 Obsługuje pliki `.mp3`, `.wav`, `.mp4`, `.webm`, `.mkv`, itp.
- 🧠 Transkrypcja za pomocą modelu Whisper (w tym `tiny`, `base`, `small`, `medium`, `large`, `turbo`)
- 🧩 Podział segmentów na mniejsze frazy (np. po 7 słów)
- 🔄 Podgląd logów i postęp transkrypcji w %
- ⛔ Przycisk **Przerwij transkrypcję** w trakcie działania
- 💾 Eksport do formatu `.srt`
- 🧰 Wersja `.exe` – bez potrzeby instalacji Pythona

## 🧠 O Whisper
Whisper to model przetwarzania mowy na tekst (ASR – Automatic Speech Recognition) stworzony przez OpenAI. Jest to jeden z najlepszych dostępnych modeli, który wspiera wiele języków i jest odporny na szumy. Whisper został zaprojektowany z myślą o przetwarzaniu dźwięku w różnych kontekstach, dzięki czemu jest w stanie dokładnie transkrybować rozmowy, wykłady, podcasty, nagrania rozmów i inne rodzaje dźwięków.

Dzięki otwartemu kodowi, Whisper jest dostępny do użycia za darmo na komputerach lokalnych, co czyni go idealnym rozwiązaniem dla osób potrzebujących dokładnej transkrypcji.

## 🖼️ Zrzut ekranu
![Zrzut ekranu GUI](https://skullmedia.pl/wp-content/uploads/2025/04/EA6165C1-8144-4C3C-A33A-BA1D8A0752ED.png)

## 🚀 Jak uruchomić (Python)

1. Zainstaluj zależności:
```bash
pip install customtkinter openai-whisper torch
```

2. (Opcjonalnie) pobierz `ffmpeg.exe` i wrzuć do folderu z aplikacją

3. Uruchom: 
```bash
python transcriber_gui.pyw
```
lub po prostu odpalając za pomocą pythona

## 📦 Wersja EXE
Możesz zbudować wersję `.exe` (która nie wymaga instalowania Pythona):

```bash
pyinstaller --onefile --windowed --icon=icon.ico \
  --hidden-import=whisper --hidden-import=ffmpeg \
  --add-data="ffmpeg.exe;." \
  --distpath "./EXE" transcriber_gui.pyw
``` 

W katalogu `EXE/` znajdziesz gotowy plik `main.exe`

## 📁 Wymagania
- Python 3.8+
- Modele Whisper (`tiny.pt`, `medium.pt`, itd.) – mogą zostać pobrane automatycznie lub ręcznie do folderu `models/`
- `ffmpeg.exe` (dla obsługi plików wideo)

## 🔖 Licencja
Whisper i modele ASR są dostępne na licencji [MIT](https://opensource.org/licenses/MIT) dzięki OpenAI. Model Whisper jest dostępny na [GitHubie OpenAI](https://github.com/openai/whisper).

`ffmpeg` jest narzędziem otwartym, dostępnym na licencji LGPL lub GPL w zależności od wybranej wersji. Więcej informacji znajdziesz na [stronie FFmpeg](https://ffmpeg.org).