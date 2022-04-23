st.header("Student Attention Detection")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])        
webcam = webcam()
while run:
    # read frame from webcam 
    status, frame = webcam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceDetector(grayImage, 0)

    for face in faces:
        faceLandmarks = landmarkFinder(grayImage, face)
        faceLandmarks = face_utils.shape_to_np(faceLandmarks)

        leftEye = faceLandmarks[leftEyeStart:leftEyeEnd]
        rightEye = faceLandmarks[rightEyeStart:rightEyeEnd]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)

        cv2.drawContours(frame, [leftEyeHull], -1, (255, 0, 0), 2)
        cv2.drawContours(frame, [rightEyeHull], -1, (255, 0, 0), 2)

        if ear < MINIMUM_EAR:
            EYE_CLOSED_COUNTER += 1
        else:
            EYE_CLOSED_COUNTER = 0

        cv2.putText(frame, "EAR: {:.2f}".format(ear), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        if EYE_CLOSED_COUNTER >= MAXIMUM_FRAME_COUNT:
            cv2.putText(frame, "Drowsiness", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')
