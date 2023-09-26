import os
from PIL import Image

# 指定包含 PNG 圖像的資料夾
input_folder = r''
# 指定保存 JPG 圖像的資料夾
output_folder = r''

# 創建輸出資料夾（如果它不存在的話）
os.makedirs(output_folder, exist_ok=True)

# 遍歷資料夾中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        # 獲取 PNG 圖像的完整路徑
        png_path = os.path.join(input_folder, filename)
        # 定義 JPG 圖像的完整路徑
        jpg_path = os.path.join(output_folder, filename.rstrip('.png') + '.jpg')
        
        # 打開 PNG 圖像
        with Image.open(png_path) as img:
            # 檢查是否有透明通道
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                # 創建一個白色背景的新圖像
                background = Image.new('RGB', img.size, (255, 255, 255))
                # 合併圖像
                background.paste(img, (0, 0), img.convert('RGBA'))
                # 保存為 JPG 格式
                background.save(jpg_path, 'JPEG')
            else:
                # 如果沒有透明通道，直接保存為 JPG
                img.convert('RGB').save(jpg_path, 'JPEG')

print("Conversion is complete!")