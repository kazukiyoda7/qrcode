import qrcode
import numpy as np
import os
import random
import pandas as pd

# ディレクトリが存在しない場合は作成
data_dir = "data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    print(f"created {data_dir} directory.")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
    mask_pattern=0,
)

df = pd.DataFrame(columns=["path", "contents"])

for i in range(100):
    contents = i
    qr.add_data(contents)
    qr.make(fit=True)
    path = 'data/' + str(i) + '.png'
    img = qr.make_image(fill_color="black", back_color="white").convert('L')
    img.save(path)
    df = df.append({"path": path, "contents": contents}, ignore_index=True)
    df.to_csv("data/qr_data.csv", index=False)
    qr.clear()