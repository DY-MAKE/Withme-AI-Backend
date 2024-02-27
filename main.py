import uvicorn

from typing import Optional

from fastapi import FastAPI, File, UploadFile
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

# from customFunctions import index
# from ocr.prediction import Prediction_OCR

from services.caption.prediction import getCaptionForImage
import uuid

app = FastAPI()


class BaseResponse(BaseModel):
    result: Optional[str]

# app.mount("/static", StaticFiles(directory="./static", html = True), name="static")

# @app.post("/upload", response_model=API_Response)
# async def Upload(file: UploadFile = File(...)):
#     ALLOW_TYPES = ['jpg', 'jpeg', 'png', 'jpg']
#     file_type = file.filename.split(".")[-1]
    
#     if (index(ALLOW_TYPES, file_type) == None):
#         raise HTTPException(
#             status_code=422,
#             detail="not allowed extension"
#         )

#     Result = API_Response()
#     Token = str(uuid.uuid4())+"."+file_type
#     image = await file.read()
#     try:
#         f = open("./temp/"+Token, "wb")
#         f.write(image)
#     except Exception as e:
#         Result.detail = str(e)
#     else:
#         Result.result = Token
#     finally:
#         return Result


# class AI_Token(BaseModel):
#     token: str

@app.post("/caption", response_model=BaseResponse)
async def run_ocr(file: UploadFile = File(...)):
    ALLOW_TYPES = ['jpg', 'jpeg', 'png', 'jpg']
    file_type = file.filename.split(".")[-1]

    try:
        image = await file.read()
        return BaseResponse(result=getCaptionForImage(image))
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
        # print(e)
        # Return.detail = "Wrong Token"
    # else:

        # if (detection and detection.result):
        #     Return.result = detection.result
        # elif (detection.error):
        #     raise HTTPException(
        #         status_code=418,
        #         detail=detection.error
        #     )
        # else:
        #     raise HTTPException(
        #         status_code=500,
        #         detail="unknown error"
        #     )

# @app.post("/ocr", response_model=API_Response)
# async def run_ocr(Body: AI_Token):
#     Return = API_Response()
#     try:
#         image = open("./temp/"+Body.token, "rb").read()
#         detection = Prediction_OCR(image)
#     except Exception as e:
#         print(e)
#         Return.detail = "Wrong Token"
#     else:
#         if (detection and detection.result):
#             Return.result = detection.result
#         elif (detection.error):
#             raise HTTPException(
#                 status_code=418,
#                 detail=detection.error
#             )
#         else:
#             raise HTTPException(
#                 status_code=500,
#                 detail="unknown error"
#             )
#     return Return



# class TTS_Request(BaseModel):
#     text: str
# @app.post("/tts", response_model=API_Response)
# async def run_TTS(Body: TTS_Request):
#     Return = API_Response()

#     tts = TextToBase64(Body.text)

#     if (tts.result):
#         Return.result = tts.result
#     else:
#         Return.detail = tts.err
    
#     return Return



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3001)