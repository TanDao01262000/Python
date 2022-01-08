"""Convert a PDF file into audio file with pyttsx3 and slate3k"""
import pyttsx3
import slate3k

def converting():
    docs = open('C:\\Users\\tankh\\Downloads\\WorldMusicPerformance.pdf', 'rb')
    rough = slate3k.PDF(docs)
    print(rough)
    print(rough[0])
    content =  [[x for x in rough[i].split('\n') if x != " "] for i in range(len(rough))]
    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 170)

    # print(content)

    audio_reader.save_to_file(content, "audio_file.mp3")
    audio_reader.runAndWait()

    docs.close()
converting()
