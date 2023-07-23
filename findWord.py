from youtube_transcript_api import YouTubeTranscriptApi as yta
import re

def print_time(search_word,time):
    print(f"'{search_word}' was mentioned at:")
    # calculate the accurate time according to the video's duration
    for t in time:
        hours = int(t // 3600)
        min = int(t // 60)
        sec = int(t % 60)
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

# Get the youtube video id form url after "?v="
video_id = "1aA1WGON49E"
# Change the language if needed, example: en, English
transcript = yta.get_transcript(video_id, languages=('tr', 'Turkish'))
data = [t['text'] for t in transcript]

# Removing non-alphanumeric characters and accepting Turkish Characters
data = [re.sub(r"[^a-zA-Z0-9-ışğöüçiIŞĞÖÜÇİ ]", "", line) for line in data]
# Define the search word wanted
search_word = "Facebook"

time = []
for i, line in enumerate(data):
    if search_word in line:
        start_time = transcript[i]['start']
        time.append(start_time)

print_time(search_word, time)


# https://github.com/olaDEN
