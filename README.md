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
 
1. **Zainstaluj Pythona**:
   Pobierz i zainstaluj Pythona z [oficjalnej strony Pythona](https://www.python.org/downloads/).

2. **Zainstaluj zależności**:
   Otwórz terminal (np. PowerShell) i zainstaluj wymagane pakiety za pomocą poniższego polecenia:

   ```bash
   pip install customtkinter openai-whisper torch
   ```

3. **(Opcjonalnie) pobierz `ffmpeg.exe`**:
   Pobierz `ffmpeg.exe` ze strony: [FFmpeg](https://ffmpeg.org/download.html).
   Następnie wrzuć plik `ffmpeg.exe` do folderu z aplikacją.

4. **Uruchom aplikację**:
   Uruchom aplikację za pomocą poniższego polecenia:

   ```bash
   python transcriber_gui.pyw
   ```

   lub po prostu odpalając za pomocą Pythona.

## 🚀 Przyspiesz transkrypcje dzięki CUDA w karcie graficznej ()

# 🖥️ Obsługa CUDA (dla użytkowników z GPU)

Aby używać GPU z **PyTorch**, musisz zainstalować odpowiednią wersję **PyTorch** z obsługą CUDA. Poniżej znajdziesz instrukcje, jak skonfigurować środowisko z obsługą CUDA.

## Jak sprawdzić wersję CUDA w systemie

Aby sprawdzić, jaka wersja CUDA jest zainstalowana na Twoim systemie, użyj poniższego polecenia w terminalu:

```bash
nvcc --version
```

To polecenie wyświetli wersję zainstalowanej **CUDA Toolkit**.

## Instalacja PyTorch z CUDA

Zainstaluj odpowiednią wersję PyTorch zgodnie z wersją CUDA zainstalowaną w systemie. W poniższym przykładzie pokażemy instalację PyTorch dla wersji **CUDA 11.6** i **CUDA 10.2**.

### Dla CUDA 11.6:
Jeśli masz zainstalowaną wersję **CUDA 11.6**, uruchom poniższe polecenie:

```bash
pip install torch==1.10.0+cu116 torchvision==0.11.1+cu116 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
```

### Dla CUDA 10.2:
Jeśli masz zainstalowaną wersję **CUDA 10.2**, uruchom poniższe polecenie:

```bash
pip install torch==1.9.0+cu102 torchvision==0.10.0+cu102 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
```

### Inne wersje CUDA:
Możesz również zainstalować inną wersję PyTorch dla innej wersji **CUDA**. Odwiedź stronę [PyTorch Get Started](https://pytorch.org/get-started/locally/) i wybierz odpowiednią wersję dla swojego systemu.

## Instalacja CUDA Toolkit i sterowników NVIDIA

Aby korzystać z GPU w PyTorch, należy również zainstalować **CUDA Toolkit** oraz odpowiednie sterowniki NVIDIA.

1. Przejdź na stronę pobierania **CUDA Toolkit**: [CUDA Toolkit Download](https://developer.nvidia.com/cuda-toolkit).
2. Pobierz wersję **CUDA** odpowiednią do Twojego systemu operacyjnego.
3. Zainstaluj **CUDA Toolkit** i **NVIDIA drivers** zgodnie z instrukcjami na stronie.
4. Upewnij się, że wersja **CUDA Toolkit** jest kompatybilna z Twoim systemem i wersją PyTorch.

## Ustawienie zmiennej środowiskowej (opcjonalne)

W zależności od systemu operacyjnego, możesz również potrzebować ustawić zmienne środowiskowe dla **CUDA**.

Na przykład na Windowsie:
1. Otwórz **Panel sterowania** → **System** → **Zaawansowane ustawienia systemu** → **Zmienne środowiskowe**.
2. W sekcji **Zmienne systemowe** dodaj do zmiennej `Path` ścieżkę do folderu `bin` w zainstalowanym CUDA, np. `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.6\bin`.

Po tych krokach PyTorch będzie mógł korzystać z Twojego GPU do przyspieszenia obliczeń.

---


## 📁 Wymagania
- Python 3.8+
- Modele Whisper (`tiny.pt`, `medium.pt`, itd.) – mogą zostać pobrane automatycznie lub ręcznie do folderu `models/`
- `ffmpeg.exe` (dla obsługi plików wideo)

## 🔖 Licencja
Whisper i modele ASR są dostępne na licencji [MIT](https://opensource.org/licenses/MIT) dzięki OpenAI. Model Whisper jest dostępny na [GitHubie OpenAI](https://github.com/openai/whisper).

`ffmpeg` jest narzędziem otwartym, dostępnym na licencji LGPL lub GPL w zależności od wybranej wersji. Więcej informacji znajdziesz na [stronie FFmpeg](https://ffmpeg.org).