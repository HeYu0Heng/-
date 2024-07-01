import os
from PIL import Image

# 设置图片目录和输出文件
image_dir = 'C:/Users/huiwei/Desktop/xiaole'
output_image_path = 'C:/Users/huiwei/Desktop/qnm/output_image2.png'  # 指定保存为PNG格式

# 获取图片文件名列表
image_files = [f for f in os.listdir(image_dir) if f.endswith('.png')]

# 定义一个函数来从文件名中提取最后一个 subimage 后面的数字
def extract_last_subimage_number(filename):
    parts = filename.split('_')
    for i in range(len(parts) - 1, -1, -1):
        if parts[i].startswith('subimage'):
            return int(parts[i + 1])
    return -1  # 如果没有找到合适的 subimage 后面的数字，返回 -1 或者其他合适的值

# 按照最后一个 subimage 后的数字进行排序
image_files.sort(key=extract_last_subimage_number)

# 读取所有图片并存储在列表中
images = [Image.open(os.path.join(image_dir, f)) for f in image_files]

# 假设所有图片的大小相同
image_width, image_height = images[0].size

# 设置拼接图片的尺寸，每行10张
columns = 10
rows = (len(images) + columns - 1) // columns  # 向上取整

# 创建一个新的空白图像，用于存储拼接结果
output_image = Image.new('RGB', (image_width * columns, image_height * rows))

# 将每张图片粘贴到输出图像中的正确位置
for index, image in enumerate(images):
    x = (index % columns) * image_width
    y = (index // columns) * image_height
    output_image.paste(image, (x, y))

# 保存拼接后的图像为PNG格式
output_image.save(output_image_path)
print(f"拼接后的图像已保存为 {output_image_path}")
