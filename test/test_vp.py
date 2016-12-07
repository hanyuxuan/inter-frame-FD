import videoprocessing.slidingwindow as sl

result = sl.segment_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14],3,1)
result1 = sl.segment_list(["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png",
                           "11.png","12.png","13.png","14.png","15.png"],3,2)
print result
print result1