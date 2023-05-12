# Madhur Dhwani

### Introduction -

Welcome to our audio to text converter! This tool is designed to make your life easier by transcribing your audio files into text using <b>OpenAI's Whisper</b> technology. With this state-of-the-art speech recognition technology, we are able to accurately transcribe your audio files into text in real time. Our tool is built using Flask, a micro web framework in Python, which provides a user-friendly interface to easily upload and convert your audio files. Whether you need to transcribe an interview, a lecture, or a podcast, our audio to text converter is here to help. So, sit back and relax while we do the heavy lifting for you!

### Technology Used 
- Flask 
- whisper
- torch 

### Installation 

- Create virtual environment using 

    python -m venv venv

- Initialize the empty git repository using 

    git init 

- Clone the git repository using 

    git clone 

- Install all the dependancies using 

    pip install -r requirements.txt


### About 
- `./templates`
    - Includes the index.html file having all the html code 
- `./app.py` 
    - Containes the code for flask
- `./static/uploads`
    - containes all the uploaded audio files 

### What you can do 

- [] Improve the UI 
- [] Add a *loader* till the audio gets processed 
- [] Add a text highlight feature while replaying the audio after transcription 
- [] Divide the longer audio inputs into chunks and output the complete transcription at end
- [] Add support for multiple languages, as it currenty processes only `English`.

### References 
- [] You can refer to openai-whispers official documentation --> `https://github.com/openai/whisper`

- [] You can use timestamps for task 3