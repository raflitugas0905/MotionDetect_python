import cv2
import mediapipe as mp
import time

# Inisialisasi MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Fungsi untuk cek jari terbuka/tertutup
def get_finger_states(hand_landmarks, hand_label):
    tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    fingers = {}

    # Thumb cek pakai X
    if hand_label == "Right":
        fingers["Thumb"] = hand_landmarks.landmark[tips[0]].x < hand_landmarks.landmark[tips[0] - 1].x
    else:  
        fingers["Thumb"] = hand_landmarks.landmark[tips[0]].x > hand_landmarks.landmark[tips[0] - 1].x

    # Other fingers cek pakai Y
    for i, tip_id in enumerate(tips[1:], start=1):
        fingers[["Index", "Middle", "Ring", "Pinky"][i - 1]] = (
            hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y
        )

    return fingers

# Mapping gesture custom
def recognize_gesture(fingers):
    # Semua jari terbuka → Haii
    if all(v is True for v in fingers.values()):
        return "Haii"

    # Hanya telunjuk terbuka → Nama Saya
    if fingers["Index"] and not any([fingers["Middle"], fingers["Ring"], fingers["Pinky"], fingers["Thumb"]]):
        return "Nama Saya"

    # Point (telunjuk + jempol mungkin ikut) → Rafli Tri Hanafi
    if fingers["Index"] and not fingers["Middle"] and not fingers["Ring"] and not fingers["Pinky"]:
        return "Rafli Tri Hanafi"

    # Thumbs Up → Kerenn Kan
    if fingers["Thumb"] and not any([fingers["Index"], fingers["Middle"], fingers["Ring"], fingers["Pinky"]]):
        return "Kerenn Kan"

    return "Unknown"

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print('ERROR: Could not open webcam.')
        exit()

    prev_time = 0
    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        model_complexity=1,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.5
    ) as hands:
        while True:
            ret, frame = cap.read()
            if not ret:
                print('ERROR: empty frame')
                break

            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape
            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(img_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    fingers = get_finger_states(hand_landmarks, handedness.classification[0].label)
                    gesture = recognize_gesture(fingers)

                    cv2.putText(
                        frame, f"{gesture}",
                        (10, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0), 2
                    )

            # FPS counter
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
            prev_time = curr_time
            cv2.putText(frame, f'FPS: {int(fps)}', (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

            cv2.imshow('Hand Gesture Recognition', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
