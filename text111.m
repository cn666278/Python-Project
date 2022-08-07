clc; clear; close all;

%task2(iii)
x = [2 1 0 1]; % vector of x(n)
x1=[x zeros(1,60)]; % padding 60 zeros
X_fft = fft(x1); % DFT computation
mag = abs(X_fft); % compute the magnitude
ph = angle(X_fft)*180/pi; % compute the phase
% Plot the magnitude and phase
k = 0:1:size(x1,2)-1;
 
figure(3)
%plot magnitude
subplot(2,1,1);
stem(k, mag, 'filled'); % plot magnitude using stem
title("Amplitude of DFT");
xlabel('frequnency in pi units, \Omega'); ylabel('Amplitude');
 
%plot phase
subplot(2,1,2);
stem(k, ph, 'filled'); % plot phase using stem
title("Phase of DFT");
xlabel('Index, k'); ylabel('Degrees');
