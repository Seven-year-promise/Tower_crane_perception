import cv2
from pathlib import Path


def crop_im(img, num_batches = [8, 8]):
    ori_h, ori_w = img.shape[:-1]
    cropped_w = ori_w//num_batches[0]
    cropped_h = ori_h//num_batches[1]
    image_batches  = []
    for i in range(num_batches[0]):
        x_start = i*cropped_w
        x_end = (i+1)*cropped_w
        if x_end > ori_w:
            x_end = ori_w
        for j in range(num_batches[1]):
            y_start = j*cropped_h
            y_end = (j+1)*cropped_h
            if y_end > ori_h:
                y_end = ori_h
            image_batches.append(img[y_start:y_end, x_start:x_end])
    
    return image_batches


if __name__ == "__main__":
    image_path = Path()
    image_list = image_path.rglob("*.png")
    save_path = Path()
    save_path.mkdir(exist_ok=True, parents=True)
    for i_f in image_list:
        image_name = i_f.name()
        img = cv2.imread(i_f)
        image_batches = crop_im(img, num_batches = [8, 8])
        for num, im in enumerate(image_batches):
            cv2.imwrite(str(save_path/(str(num) + ".png")), im)