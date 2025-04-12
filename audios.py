from openai import OpenAI
import os

# Lê a API key de um arquivo
with open("C:/include_your_path_here/openai_key.txt", "r") as f:
    api_key = f.read().strip()

# Inicializa o cliente
client = OpenAI(api_key=api_key)

# Abre o arquivo de áudio
audio_files = [
    "C:/include_your_path_here/file.ogg",
    "C:/include_your_path_here/file2.ogg"
]

# Corrigido: nome da variável e criação de pasta
output_folder = "C:/include_your_path_here/file"
os.makedirs(output_folder, exist_ok=True)

# Agora processa cada áudio
for idx, audio_path in enumerate(audio_files, start=1):
    with open(audio_path, "rb") as audio_file:  # Aqui sim usamos "rb"
        transcription = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_file,
            response_format="text"
        )
    
    # Salva cada transcrição
    output_path = os.path.join(output_folder, f"transcription_{idx}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(transcription)

    print(f"✅ Transcription {idx} saved to: {output_path}")
