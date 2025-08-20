from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
import os

# FastAPI version
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import samsungctl

app = FastAPI(
    title="Samsung TV Remote API",
    description="Control your Samsung TV over WiFi",
    version="1.0.0"
)

class TVCommand(BaseModel):
    command: str

config = {
    "name": "Web Remote",
    "description": "TV Remote Control",
    "id": "webremote",
    "host": "192.168.0.135",  # Replace with your TV's IP address
    "port": 8001,
    "method": "websocket",
    "timeout": 0
}

command_map = {}
#    'power': 'KEY_POWER',
#    'volume_up': 'KEY_VOLUP',
#    'volume_down': 'KEY_VOLDOWN',
#    'mute': 'KEY_MUTE',
#    'channel_up': 'KEY_CHUP',
#    'channel_down': 'KEY_CHDOWN',
#    '1': 'KEY_1',
#    '2': 'KEY_2',
#    '3': 'KEY_3',
#    '4': 'KEY_4',
#    '5': 'KEY_5',
#    '6': 'KEY_6',
#    '7': 'KEY_7',
#    '8': 'KEY_8',
#    '9': 'KEY_9',
#    '0': 'KEY_0'
#}


@app.get("/home", summary="Serve home.html if it exists")
async def get_home_html():
    html_path = os.path.join(os.path.dirname(__file__), "home.html")
    if os.path.exists(html_path):
        return FileResponse(html_path, media_type="text/html")
    return JSONResponse(status_code=404, content={"detail": "home.html not found"})

@app.post("/tv", summary="Send a remote command to the Samsung TV")
async def control_tv(cmd: TVCommand):
    key = command_map.get(cmd.command, cmd.command).upper()
    try:
        with samsungctl.Remote(config) as remote:
            remote.control(key)
        return {"status": "ok", "command": cmd.command}
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "detail": str(e)})