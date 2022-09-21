import numpy as np
import cv2
import timeit
import os


def templateMatching(filename,templatein):
    #reading and resizing video
    #template matching requires grayscale image. so, we loading the image in gray scale.
    template = cv2.imread(templatein,0)


    template_width, template_height = template.shape

    #methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
    #           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    cap = cv2.VideoCapture(filename)
    height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps= cap.get(cv2.CAP_PROP_FPS)

    #array for storing result of each frame
    arr = np.arange(fps*1500)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc('P','I','M','1')
    out = cv2.VideoWriter('output.avi',fourcc, fps, (width,height))

    # create VideoWriter object2
    out2 = cv2.VideoWriter('output2.avi',fourcc, fps, (width,height))

    def search():
        flag = 0
        for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):

            #READ A FRAME
            success, img = cap.read()
            # img = captureScreen()
            #imgCopy = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            if success:
                imgCopy = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                result = cv2.matchTemplate(imgCopy, template, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                arr[frame_idx] = max_val

                #write out frame
                if flag==1:
                    out.write(img)


                threshold= 0.45
                if max_val >= threshold:
                    flag=1
                    #print("Match Found")
                    print(max_val)
                    #getting the co-ordinates of the rectangle to draw
                    top_left = max_loc
                    bottom_right = (top_left[0] + template_width, top_left[1] + template_height)

                    cv2.rectangle(imgCopy, top_left, bottom_right, 255, 5)
                    cv2.imshow('Match', imgCopy)


                else:
                    print("No Match")
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

    search()

    cap.release()
    cv2.destroyAllWindows
    #release video writer
    out.release()

    # result = timeit.timeit(stmt='search()', globals=globals(), number=1)
    print("match found successfully")
    # print("Execution Time: ", result)



    def crop():
        max_index= np.argmax(arr)
        start_frame= max_index
        end_frame= 40*fps
        counter=1

        cap = cv2.VideoCapture(filename)

        for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
            success, img = cap.read()

            if success:
                if(counter>=start_frame and counter<=end_frame):
                    out2.write(img)
                counter+=1

        out2.release()
        cv2.destroyAllWindows