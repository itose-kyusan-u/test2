import cv2
# %matplotlib inline

try:
    img = cv2.imread('ichigo.jpg')
    if img is None:
        raise FileNotFoundError("ファイルがありませんでした。")
    
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 意味のないコメント…Gitのテストのため

except FileNotFoundError as e:
    print(e)