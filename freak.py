import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.7, maxHands=2)

blur_active = False
peace_frames = 0

def is_peace(hand):
    fingers = detector.fingersUp(hand)
    # fingers = [thumb, index, middle, ring, pinky]

    return (
        fingers[1] == 1 and   # index up
        fingers[2] == 1 and   # middle up
        fingers[3] == 0 and   # ring down
        fingers[4] == 0       # pinky down
    )

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)

    hands, img = detector.findHands(frame)

    detected = False

    if hands:
        for hand in hands:
            if is_peace(hand):
                detected = True
                break

    # anti flicker
    if detected:
        peace_frames += 1
    else:
        peace_frames = max(0, peace_frames - 1)

    blur_active = peace_frames >= 1

    if blur_active:
        img = cv2.GaussianBlur(img, (31, 31), 0)
        cv2.putText(
        img,
        "CAMERA BLURRED",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 0),  # hitam (BGR)
        2
    )

    cv2.imshow("Hehe", img)

    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()