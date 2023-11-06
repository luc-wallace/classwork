clear all;
C = imread("PlaneGrey.jpeg");
figure(1);
imshow(C);
C(:,:) = 255 - C(:,:);
figure(2);
imshow(C);
imwrite(C, "PlaneGreyNegative.jpeg");