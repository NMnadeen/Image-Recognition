# Upload image code: https://tutorial101.blogspot.com/2023/02/fastapi-upload-image.html

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
from random import randint
import uuid