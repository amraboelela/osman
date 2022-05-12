# Translate Osman series

Here we show the steps, to download, then translate youtube Osman episodes starting of episode 90 then you can watch them translated in your computer.

## Setup
This is the setup in macOS

```
% sudo mkdir -p /usr/local/bin
% sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
% sudo chmod a+rx /usr/local/bin/youtube-dl
% vim translation_key.py
key = "<PUT THE KEY FROM YOUR GOOGLE TRANSLATE API ACCOUNT>"
% brew install pyenv
% pyenv install 2.7.18
% pyenv global 2.7.18
% pyenv init --path
copy the output
% vi ~/.zshrc
paste then save
% source ~/.zshrc 
% sudo easy_install -U requests
% sudo -H pip3 install requests
% sudo -H pip3 install gTTS
% brew install ffmpeg
% brew install handbrake
```

## Usage

- To build episode 90 till episode 93 and translate from Turkish to English:

```
$ ./build.sh 90 93 tr en
```
