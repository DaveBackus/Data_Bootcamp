%  kalman_ma1.m 
%  Takes MA(1) in state-space form, computes Kalman filter, and shows
%  what happens in noninvertible case.  
%  Written:  May 2010 and after 
format compact 
clear all
close all

disp(' ')
%disp('Kalman filter calculations') 
disp('---------------------------------------------------------------')
disp(' ')

%  1. MA(1) 
syms chi0 chi1 theta real 
syms P p11 p12 p22 K 

A = [0 1; 0 0];
C = [chi0; chi1];
Q = C*C';
G = [1 1];
R = [0];

%  Solution 
P = [p11 p12; p12 p22];
Pm = A*P*A' + Q             % Pm = P-
Vara = (G*Pm*G'+R)
K = Pm*G'*inv(G*Pm*G'+R)

Pguess1 = simplify(Pm - Pm*G'*inv(G*Pm*G'+R)*G*Pm)
Pguess2 = simplify(Pm - Pm*G'*inv(G*Pm*G'+R)*G*Pm)
Pmguess2 = simplify(A*Pm*A' + Q - A*Pm*G'*inv(G*Pm*G'+R)*G*Pm*A')

Pmguess2 = simplify(A*Pm*A' + Q - A*Pm*G'*inv(G*Pm*G'+R)*G*Pm*A')

return 

%  2. Scalar case 
clear A C Q G P K 
syms A C Q G R P K real  

%  Solution 
Pm = A*P*A' + Q             % Pm = P-
Vara = (G*Pm*G'+R)
K = Pm*G'*inv(G*Pm*G'+R)
Pguess = Pm - Pm*G'*inv(G*Pm*G'+R)*G*Pm;
Pguess1 = simplify(Pguess)
Pmguess2 = simplify(A*Pm*A' + Q - A*Pm*G'*inv(G*Pm*G'+R)*G*Pm*A')

return 
