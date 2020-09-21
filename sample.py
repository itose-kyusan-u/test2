import cv2
# %matplotlib inline

try:
    img = cv2.imread('ichigo.jpg')
    if img is None:
        raise FileNotFoundError("ファイルがありませんです。")
    
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)