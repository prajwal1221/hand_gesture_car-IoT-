import cv2
import mediapipe as mp
import asyncio
import websockets

# Replace with your ESP8266 WebSocket IP
ESP_IP = "ws://192.168.4.1:81"

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils  # For drawing landmarks

# Open Webcam
cap = cv2.VideoCapture(0)

# Initialize Async Event Loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def send_command(command):
    """Send gesture command to ESP8266 via WebSocket."""
    try:
        async with websockets.connect(ESP_IP) as websocket:
            await websocket.send(command)
            print(f"Sent: {command}")
    except Exception as e:
        print(f"WebSocket Error: {e}")

def recognize_gesture(landmarks):
    """Detects if the palm is open (all fingers extended)"""
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    index_pip = landmarks[6]
    middle_pip = landmarks[10]
    ring_pip = landmarks[14]
    pinky_pip = landmarks[18]


    thumb_base = landmarks[2]

    # Check if all fingers are straight (tips above their PIP joints)
    if (
        index_tip.y < index_pip.y and
        middle_tip.y < middle_pip.y and
        ring_tip.y < ring_pip.y and
        pinky_tip.y < pinky_pip.y and
        abs(thumb_tip.x - thumb_base.x) > 0.1  # Thumb spread out
    ):
        return "S"

    elif thumb_tip.y < middle_tip.y < pinky_tip.y:
        return "F"
    
    elif thumb_tip.y > middle_tip.y > pinky_tip.y:
        return "B" 

    elif thumb_tip.x > middle_tip.x > pinky_tip.x:
        return "L"

    elif thumb_tip.x > middle_tip.x > pinky_tip.x:
        return "R" 
    
    return None  # No recognized gesture

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB (for MediaPipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark
            gesture = recognize_gesture(landmarks)

            if gesture:
                loop.run_until_complete(send_command(gesture))
                cv2.putText(frame, f"Gesture: {gesture}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
