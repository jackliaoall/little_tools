from PIL import Image
import os
import glob

# 輸入資料夾和輸出資料夾的路徑
input_folder = r""
output_folder = r""

# 確保輸出資料夾存在，如果不存在，則創建它
#if not os.path.exists(output_folder):
#    os.makedirs(output_folder)

# 遍歷輸入資料夾中的所有圖片文件
image_files = glob.glob(os.path.join(input_folder, "*.png"))  # 請根據您的圖片格式修改這裡

counter = 0

for image_file in image_files:
    # 打開原始圖片
    original_image = Image.open(image_file)

    # 獲取原始圖片的寬度和高度
    width, height = original_image.size

    # 計算每個子圖片的寬度和高度
    sub_width = width // 2
    sub_height = height // 2

    counter = counter + 1

    # 切割並保存四個子圖片
    for i in range(2):
        for j in range(2):
            left = i * sub_width
            upper = j * sub_height
            right = left + sub_width
            lower = upper + sub_height
            sub_image = original_image.crop((left, upper, right, lower))
            sub_image.save(os.path.join(output_folder, f"{counter}_{i}_{j}.png"))

    # 關閉原始圖片
    original_image.close()