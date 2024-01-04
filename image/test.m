pkg load image

close all;
clear all;
clc;

W = imread("Trees.jpeg");
W = imrotate(W, 180);

imshow(W)

imwrite(W, "TreesRotate.jpeg");
imshow(W);

info = imfinfo("TreesRotate.jpeg");
disp(info);

