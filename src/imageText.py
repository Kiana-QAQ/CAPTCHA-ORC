import ddddocr
import cv2

det = ddddocr.DdddOcr(det=True, ocr=True)

with open("../input.jpg", 'rb') as f:
    image = f.read()

bboxes = det.detection(image)
# res = det.classification(image)
print(bboxes)

# 用于保存裁切后的图片
cropped_images = []

im = cv2.imread("../input.jpg")

for i, bbox in enumerate(bboxes):
    x1, y1, x2, y2 = bbox
    im = cv2.rectangle(im, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)
    # 裁切图片
    cropped_image = im[y1:y2, x1:x2]
    # 保存裁切后的图片
    cv2.imwrite(f"../images/img{i}.jpg", cropped_image)
    # 将裁切后的图片添加到列表中
    cropped_images.append(cropped_image)

cv2.imwrite("../output.jpg", im)
