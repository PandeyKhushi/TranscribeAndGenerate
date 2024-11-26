from transformers import pipeline
import gradio as gr
from huggingface_hub import HfFolder
import requests
import asyncio
from gtts import gTTS
import google.generativeai as genai

pipe = pipeline("automatic-speech-recognition", model="sanchit-gandhi/whisper-small-dv")
genai.configure(api_key="AIzaSyCYLEmqBizZYGv9aieORnX1EViMY79LVqc")
generation_config = {
  "temperature": 0.8,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 8192
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

async def query(text):
    print("\n\nDETECTED TEXT:",text,"\n\n")
    response=model.generate_content(text,request_options={"timeout":240})
    print(response.candidates[0])
    return response.text

async def transcribe_speech(filepath):
    output = pipe(
        filepath,
        max_new_tokens=256,
        generate_kwargs={
            "task": "transcribe",
            "language": "english",
        },  # update with the language you've fine-tuned on
        chunk_length_s=30,
        batch_size=8,
    )
    return await query(output["text"])


def final(filepath):
    answer=asyncio.run(transcribe_speech(filepath))
    return answer

def main(filepath):
    response=final(filepath)
    # print(response)
    # myobj = gTTS(text=response, lang='en', slow=False) 
    # myobj.save(filepath)
    # return filepath
    return response

mic_transcribe = gr.Interface(
    fn=main,
    inputs=gr.Audio(sources="microphone", type="filepath"),
    outputs="text",
)

file_transcribe = gr.Interface(
    fn=main,
    inputs=gr.Audio(sources="upload", type="filepath"),
    outputs="audio",
)


demo=gr.TabbedInterface(
        [mic_transcribe, file_transcribe],
        ["Transcribe Microphone", "Transcribe Audio File"],
    )

demo.launch(debug=True)