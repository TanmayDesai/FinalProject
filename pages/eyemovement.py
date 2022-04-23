"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
#from gaze_tracking import GazeTracking
import streamlit as st

MAXIMUM_FRAME_COUNT = 180
def app():
    from gaze_tracking import GazeTracking
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(0)
    EYE_COUNTER = 0
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])
    while run:
        # We get a new frame from the webcam
        _, frame = webcam.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        text = ""

        #if gaze.is_blinking():
        #    text = "Blinking"
        if gaze.is_right():
            text = "Looking right"
            EYE_COUNTER = EYE_COUNTER + 1
        elif gaze.is_left():
            text = "Looking left"
            EYE_COUNTER = EYE_COUNTER + 1
        elif gaze.is_up():
            text = "Looking Up"
            EYE_COUNTER = EYE_COUNTER + 1

        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
        if(EYE_COUNTER>= MAXIMUM_FRAME_COUNT):
            cv2.putText(frame,"Please Look at the Screen", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
            EYE_COUNTER = 0
        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
    #cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    #cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

        FRAME_WINDOW.image(frame)
    else:
        st.write('Stopped')  
