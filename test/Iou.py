#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: Iou.py
# @time: 2020-03-02 17:16
# @desc:

if __name__ == "__main__":

    def computer_iou(x1, y1, w1, h1, x2, y2, w2, h2):

        # consider margin
        if x1 > x2:
            return computer_iou(x2, y2, w2, h2, x1, y1, w1, h1)

        if x2 > w1 or h1 > y2 or h2>y1:
            return 0

        if h2>h1:
            intersection_area = abs(w1-x2)*abs(y1-h2)
        else:
            intersection_area = abs(w1-x2)*abs(y2-h1)

        r1_area = abs(w1-x1)*abs(h1-y1)

        r2_area = abs(w2-x2)*abs(h2-y2)

        r1andr2_area = r1_area+r2_area-intersection_area

        iou = intersection_area/r1andr2_area

        return iou

    print(computer_iou(1,2,3,1,2,2,4,1))


