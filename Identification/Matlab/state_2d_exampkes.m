%  regular_companion.m
%  Check to verify companion matrix is regular 
%  Written by:  Dave Backus, December 2011
format compact

syms phi1 phi2 phi3
A = [phi1 phi2 phi3; 1 0 0; 0 1 0]

A^2
A^3

return 