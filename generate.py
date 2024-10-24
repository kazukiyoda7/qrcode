import qrcode
import numpy as np
import os

# 'data'ディレクトリのパス
data_dir = "data"
# ディレクトリが存在しない場合は作成
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    print(f"{data_dir}ディレクトリを作成しました。")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=1,
    border=1,
    mask_pattern=0
)

for i in range(10):
    data = str(i)
    qr.add_data(data)
    # print(qr.data_list)
    qr.make(fit=True)
    # print(qr.modules)
    
    # バイナリデータ化
    # data_binary = np.array(qr.modules).astype(int).flatten()
    # print(data_binary)
    # print(data_binary.shape)

    img = qr.make_image(fill_color="black", back_color="white").convert('L')
    img.save('data/' + data + '.png')

    qr.clear()
