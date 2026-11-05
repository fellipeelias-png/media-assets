# Odoya calm video tool
Renders the 15 s seamless-loop calm Reel (particle text, left layout, singing-bowl audio).
1. `python3 bowls15.py` then `ffmpeg -i bowls15.wav -c:a aac -b:a 256k bowls15.m4a` (once).
2. `python3 render_calm.py CLIP.mp4 OUT.mp4 '["you are","not lost.","you are traveling","between galaxies."]' 'galaxies.' 0`
Layout fixed: logo + handle + shop link top left (x140, y300), phrase from y630, Anton 69 px, highlight with purple gradient and white outline. Fonts OFL (Anton, Barlow).
