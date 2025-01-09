import torch
import gradio as gr
from transformers import pipeline

pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", torch_dtype=torch.bfloat16)

def summary(input):
  output = pipe(input)[0]['summary_text']
  return output

gr.close_all()

demo = gr.Interface(fn=summary, 
                    inputs=[gr.Textbox(label="Input text to summarize", lines=6)], 
                    outputs=[gr.Textbox(label="Summarized Text", lines=4)],
                    title="AI-Powered Text Summarizer",
                    description="Simplify lengthy text into concise summaries with this AI-driven tool, powered by the DistilBART model for fast and accurate results.")

demo.launch()
