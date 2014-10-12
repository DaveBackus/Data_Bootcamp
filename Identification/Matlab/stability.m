% stability.m
% check eigs of simple NK system 
format compact 

%%
syms tau1 tau2 kappa beta alpha 

A = [-tau1 -tau2; 1 -kappa];
B = [-1 -alpha; beta 0];

%%
% Cochrane version:  eq (32), p 592 
syms beta gamma sigma 

A = [beta + sigma*gamma,  -sigma; -gamma 1]/beta;

eig(A-eye(2))
det(A-eye(2))