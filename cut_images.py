from PIL import Image
import os

Image.MAX_IMAGE_PIXELS = None

def sliding_window(image, window_size, stride, output_folder, original_filename):
    width, height = image.size
    count = 0

    for y in range(0, height, stride):
        for x in range(0, width, stride):
            # 定义滑动窗口区域
            box = (x, y, x + window_size, y + window_size)

            try:
                window = image.crop(box)

                # 处理边界情况，确保子图像大小为指定的窗口大小
                if window.size[0] < window_size or window.size[1] < window_size:
                    continue

                # 生成输出文件路径，使用原始图片的名字作为前缀
                output_path = os.path.join(output_folder, f"{original_filename}_subimage_{count}.tif")

                # 保存子图像到指定文件夹
                window.save(output_path)

                count += 1
            except Exception as e:
                print(f"处理窗口 {box} 时出错：{e}")

def batch_sliding_window(input_folder, output_folder, window_size=50, stride=50):
    # 如果输出文件夹不存在，则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有图像
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".tiff", ".tif")):
            image_path = os.path.join(input_folder, filename)

            try:
                # 打开图像
                image = Image.open(image_path)

                # 提取原始图片名字（不包含扩展名）
                original_filename = os.path.splitext(filename)[0]

                # 生成滑动窗口子图像并保存到指定文件夹
                sliding_window(image, window_size, stride, output_folder, original_filename)
            except Exception as e:
                print(f"处理文件 {image_path} 时出错：{e}")

if __name__ == "__main__":
    # 指定输入文件夹
    input_folder = "C:/Users/huiwei/Desktop/111"

    # 指定输出文件夹
    output_folder = "C:/Users/huiwei/Desktop/chaifen"

    # 生成滑动窗口子图像并保存到指定文件夹
    batch_sliding_window(input_folder, output_folder)