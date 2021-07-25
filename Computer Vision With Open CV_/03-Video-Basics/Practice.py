#V1
# =============================================================================
# import cv2
# 
# cap = cv2.VideoCapture(0)
# 
# 
# width = (int)(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = (int)(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 
# writer = cv2.VideoWriter('Camtest.mp4',cv2.VideoWriter_fourcc(*'DIVX'),20,(width,height))
# 
# while True:
#     
#     ret,frame = cap.read()
#     
#    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#    
#     writer.write(frame)
#     
#     cv2.imshow('frame',frame)
#     
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#   
# cap.release()
# writer.release()
# cv2.destroyAllWindows()
# =============================================================================

#V2
# =============================================================================
# import cv2
# import time
# 
# cap = cv2.VideoCapture('camtest.mp4')
# 
# if cap.isOpened() == False:
#     print("Can't open the file.")
# 
# while cap.isOpened():
#     
#     ret,frame = cap.read()
#     
#     if ret == True:
#         
#         time.sleep(1/20)
#         
#         cv2.imshow('frame',frame)
#     
#         if cv2.waitKey(5) & 0xFF == ord('q'):
#             break
#         
#     else:
#         break        
#     
#       
# cap.release()
# cv2.destroyAllWindows()
# =============================================================================


#V3
# =============================================================================
# import cv2
# 
# cap = cv2.VideoCapture(0)
# 
# 
# width = (int)(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = (int)(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 
# x,y = width//2,height//2
# w,h = width//4,height//4
# 
# 
# while True:
#     
#     ret,frame = cap.read()
#     
#     cv2.rectangle(frame,(x,y),(w,h),(0,0,255),thickness=5)
# 
#     
#     cv2.imshow('frame',frame)
#     
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#   
# cap.release()
# cv2.destroyAllWindows()
# =============================================================================


#V4
# =============================================================================
# 
# import cv2
# 
# # Callback Function
# # tlc = topleft_clicked, brc = bottomright_clicked 
# 
# def draw_rect(event,x,y,flags,param):
#     
#     global pt1,pt2,tlc,brc
#     
#     if event == cv2.EVENT_LBUTTONDOWN:
#         
#         # Reset the rectangle
#         if tlc and brc:
#             pt1 = (0,0)
#             pt2 = (0,0)
#             tlc = False
#             brc = False
#         
#         if tlc==False:
#             pt1 = (x,y)
#             tlc = True
#         
#         elif brc==False:
#             pt2 = (x,y)
#             brc = True
#                     
#                         
# # Global variables
# pt1 = (0,0)
# pt2 = (0,0)
# tlc = False
# brc = False
# 
# # Connect to callback
# 
# cap = cv2.VideoCapture(0)
# 
# cv2.namedWindow('Test')
# cv2.setMouseCallback('Test',draw_rect)
# 
# while True:
#     
#     ret,frame = cap.read()
#     
#     # Drawing on the frame
#     
#     if tlc:
#         cv2.circle(frame,center=pt1,radius=3,color=(0,0,255),thickness=-1)
#     
#     if tlc and brc:
#         cv2.rectangle(frame,pt1,pt2,(0,0,255),thickness=3)
#         
#     cv2.imshow('Test',frame)
#     
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     
# cap.release()
# cv2.destroyAllWindows()
# =============================================================================
    
    
























