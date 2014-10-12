%  state_2d_example.m 
%  Check id with 2-state example of state-space version of model 
%  Written by:  Dave Backus, December 2011
format compact

syms a11 a12 a21 a22 lambda 
A = [a11 a12; a21 a22]
ILA  = eye(2) - lambda*A
detILA = det(ILA)
invILA = inv(ILA) 

detILA*invILA

syms e1 e2 e11 e12 e22
e1 = [e11; e12]
e2 = [0; e22]
e = e1 + e2

e'*ans

return 