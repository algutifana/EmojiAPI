from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional
from emojis import emojilist

app = FastAPI()


#list of emojis


#get emoji by id
@app.get("/get-by-id/{emoji_id}")
def get_item(emoji_id: int = Path(None,desc = 'ID of emoji you want to view')):
    return emojilist[emoji_id]

# get emoji by name (Optional)
@app.get('/get-by-name')
def get_item(*, name: Optional[str] = None):
    for emoji_id in emojilist:

        if emojilist[emoji_id]['name'] == name:
            return emojilist[emoji_id]

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)