from typing import List, Literal, Dict, Optional
from ..._models import BaseModel

__all__ = ["CheckResponse", "Urls"]


class Urls(BaseModel):
    url_chat: str
    url_asr: str
    url_tts: str
    url_txt2img: str
    url_img2img: str


class CheckResponse(BaseModel):
    code: Literal[0, 1]
    data: Urls
    msg: str
    time: str
