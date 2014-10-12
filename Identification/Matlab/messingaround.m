%  messingaround.m 
%  Backus, Chernov, and Zin, "Identifying Taylor rules" 
%  Written:  July 2013 and after 
format compact 
clear all

C = [2 0; 1 3]

L = chol(C*C','lower')

C*C'
L*L'

syms a b c d1 d2 e f g h k
L = [a 0; b c]
D = diag([d1, d2])
L2 = [e 0; f g]

Linv = inv(L)

Linv*D*L

