import cv2 as cv
import mediapipe as mp
import pyautogui as pg

cam = cv.VideoCapture(0)
mphand = mp.solutions.hands

hands = mphand.Hands()

clk = 1
key = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?']]
size = 100 / 100

buttonList = []


def S_key():
    for i in range(len(key)):
        for j, keyy in enumerate(key[i]):
            x = int((j * 60 * size) + 25)
            y = int((i * 60 * size) + 25)
            h = int(x + 50 * size)
            w = int(y + 50 * size)
            buttonList.append([x, y, h, w, keyy])

    x_start = int((0 * 60 * size) + 25)
    y_start = int((len(key) * 60 * size) + 25)
    x_end = int((3 * 60 * size) + 25 + 50 * size)
    y_end = int((len(key) * 60 * size) + 25 + 50 * size)
    buttonList.append([x_start, y_start, x_end, y_end, 'backspace'])

    x_start = int((4 * 60 * size) + 25)
    y_start = int((len(key) * 60 * size) + 25)
    x_end = int((6 * 60 * size) + 25 + 50 * size)
    y_end = int((len(key) * 60 * size) + 25 + 50 * size)
    buttonList.append([x_start, y_start, x_end, y_end, 'capslock'])

    x_start = int((7 * 60 * size) + 25)
    y_start = int((len(key) * 60 * size) + 25)
    x_end = int((9 * 60 * size) + 25 + 50 * size)
    y_end = int((len(key) * 60 * size) + 25 + 50 * size)
    buttonList.append([x_start, y_start, x_end, y_end, 'enter'])

    x_start = int((1 * 60 * size) + 25)
    y_start = int((len(key) + 1) * 60 * size + 25)
    x_end = int((8 * 60 * size) + 25 + 50 * size)
    y_end = int((len(key) + 1) * 60 * size + 25 + 50 * size)
    buttonList.append([x_start, y_start, x_end, y_end, ' '])



S_key()


def drawKey(img, buttonList):
    for x, y, h, w, keyy in buttonList:
        cv.rectangle(img, (x, y), (h, w), (0, 255, 255), 2)
        cv.putText(img, keyy, (x + 12, y + 29), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)


while True:
    success, img = cam.read()
    img = cv.flip(img, 1)
    h, w, c = img.shape
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    if result.multi_hand_landmarks:
        lmlist = []
        for handsLms in result.multi_hand_landmarks:
            for id, landmarks in enumerate(handsLms.landmark):
                x, y = int(landmarks.x * w), int(landmarks.y * h)
                lmlist.append([id, x, y])
        X = lmlist[12][1]
        Y = lmlist[12][2]
        cv.circle(img, (X, Y), 9, (255, 0, 255), cv.FILLED)
        if lmlist[8][2] > lmlist[7][2] and clk > 0:
            cv.circle(img, (X, Y), 9, (0, 0, 255), cv.FILLED)
            for x, y, h, w, keyy in buttonList:
                if x < X < h and y < Y < w:
                    pg.press(keyy)
            clk = -1
        elif lmlist[8][2] < lmlist[7][2]:
            clk = 1
    drawKey(img, buttonList)
    cv.imshow("Digital Keyboard", img)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cv.destroyAllWindows()
