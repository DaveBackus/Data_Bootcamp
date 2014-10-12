%  example_mc.m 
%  Numerical example of identification problem 
%  Example from Section 3.1, rep agent with power utility  
%  Backus, Chernov, and Zin, "Identifying Taylor rules" 
%  Written:  July 2013 and after 
format compact 
clear all

disp(' ')
disp('Taylor rule identification example') 

disp(' ')
disp('Parameters') 
% structural parameters
alpha=5
tau=1.5

% state process 
kcorr=-0.05; % correlation between the two x's
A=[0 1; -0.05 0.9]
eigA = eig(A)
C=[0.0078 0; kcorr*0.0078/sqrt(1-kcorr^2) 0.044*0.0078] 
Vx=inv(eye(4,4)-kron(A,A))*reshape(C*C',4,1); % unconditional variance of the x's
Vx=reshape(Vx,2,2);

% verify 
disp(' ')
disp('Verify Vx calculation')
Vx 
Vx_check = A*Vx*A' + C*C'

% shocks 
disp(' ')
disp('Shocks')
d1=[1 0]' % shock to consumption growth
rho1 = d1'*A*Vx*d1/(d1'*Vx*d1) % first autocorrelation of g 

% set up shock 
d22=1;
d21=-Vx(1,2)/Vx(1,1)*d22;
d2 = [d21 d22]'  % MP shock, satsifies d1'*Vx*d2=0

% restriction on Taylor rule shock 
e = Vx*d1
orthog_check = d1'*Vx*d2  

disp(' ')
disp('***Version 1: state observed')

% solution 
disp(' ')
disp('Solution') 
b = ((alpha*d1'*A-d2')*inv(tau*eye(2,2)-A))' %inflation
a = ((alpha*d1'+b')*A)' % nominal rate

a_check = (tau*b'+d2')'

var_pi = b'*Vx*b

disp(' ')
disp('Estimates of tau')
% least squares estimate 
tau_ls = (b'*Vx*a)/(b'*Vx*b)
% true value 
tau_est = a'*e/(b'*e)
top = a'*e
bot = b'*e 

disp(' ')
disp('***Version 2: Use (i,pi) as state')

Q = [a'; b']
Qinv = inv(Q) 

Ap = Q*A*Qinv 
eigAp = eig(A)
Cp = Q*C 

ap = (a'*Qinv)'
bp = (b'*Qinv)'

d1p = (d1'*Qinv)'
d2p = (d2'*Qinv)'
Vxp = Q*Vx*Q'

ep = Vxp*d1p 

tau_example2 = ap'*ep/(bp'*ep)

disp(' ')
disp('***Version 4: diagonal')

Q = [a'; a'*A]
Qinv = inv(Q) 

Ap = Q*A*Qinv 
eigAp = eig(A)
Cp = Q*C 

ap = (a'*Qinv)'
bp = (b'*Qinv)'

d1p = (d1'*Qinv)'
d2p = (d2'*Qinv)'
Vxp = Q*Vx*Q'

ep = Vxp*d1p 

tau_example3 = ap'*ep/(bp'*ep)

disp(' ')
disp('***Version 3: Use (f0=i,f1) as state')

Q = [a'; a'*A]
Qinv = inv(Q) 

Ap = Q*A*Qinv 
eigAp = eig(A)
Cp = Q*C 

ap = (a'*Qinv)'
bp = (b'*Qinv)'

d1p = (d1'*Qinv)'
d2p = (d2'*Qinv)'
Vxp = Q*Vx*Q'

ep = Vxp*d1p 

tau_example3 = ap'*ep/(bp'*ep)

return

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
pause

%Simulate innovations and states
randn('seed',0); %set seed
T=50000; %simulation size
w=normrnd(0, 1,  T, 2); %innovations
x=zeros(T,2);
%x(1,:)=C*w(1,:)';
for i=2:T
    x(i,:)=(A*x(i-1,:)'+C*w(i,:)')'; %states
end 

%Simulate observavles
fwdt=zeros(T,120); % forward rates
pi=zeros(T,1); %inflation 

for i=1:T
    pi(i)=b'*x(i,:)';
    for j=1:120
        fwdt(i,j)=a'*A^(j-1)*x(i,:)';
    end
end

display('--------- OLS tau  --------');
tauhat=inv(pi'*pi)*(pi'*fwdt(:,1))

%Assume state is known

aHat=inv(x'*x)*(x'*fwdt(:,1));
bHat=inv(x'*x)*(x'*pi);

%Estimate Ahat from the new state via VAR(1)

Spec = vgxset('n',2,'nAR',1,'Constant',true);
[EstSpec, EstStdErrors] = vgxvarx(Spec, x, [], []);
vgxdisp(EstSpec, EstStdErrors);

pause

% VAR output

Ahat=[-0.00154208  1.00937;   -0.0500093  0.899016];
Chat=[6.1213e-05 0; -3.0692e-06 2.71614e-07];
Vxhat=inv(eye(4,4)-kron(Ahat,Ahat))*reshape(Chat*Chat',4,1); %unconditional variance of the xhat's
Vxhat=reshape(Vxhat,2,2);

display('--------- identified tau  --------');
tau=(aHat'*inv(Ahat)-bHat')*Vxhat*aHat/((aHat'*inv(Ahat)-bHat')*Vx*bHat)

return
pause

delta=(aHat'-bHat'*A)';

% NO EXCLUSION RESTRICTIONS

tau=0.5;
display('--------- MP shock when state is known, wrong tau--------');
d2k05=(delta'*inv(A)-bHat'*(tau*eye(2,2)-A))'

tau=1.5;
display('--------- MP shock when state is known, right tau--------');
d2k15=(delta'*inv(A)-bHat'*(tau*eye(2,2)-A))'

%return
pause

%Assume state is not known

xhat=zeros(T,2);
xhat(:,1)=fwdt(:,1);
xhat(:,2)=fwdt(:,120);

% OLS of pi and i on states

aHat=[1 0]';
bHat=inv(xhat'*xhat)*(xhat'*pi);

%Estimate Ahat from the new state via VAR(1)

Spec = vgxset('n',2,'nAR',1,'Constant',true);
[EstSpec, EstStdErrors] = vgxvarx(Spec, xhat, [], []);
vgxdisp(EstSpec, EstStdErrors);

pause

% VAR output

Ahat=[0.865896 0;  1.31068e-09  -0.380258];
Chat=[6.42109e-05 0; 1.03895e-13 1.73993e-22];
Vxhat=inv(eye(4,4)-kron(Ahat,Ahat))*reshape(Chat*Chat',4,1); %unconditional variance of the xhat's
Vxhat=reshape(Vxhat,2,2);


% CORRECT EXCLUSION RESTRICTIONS
% This is unfinished
%bahat=bHat'*Ahat;
display('--------- identified tau  --------');
%tau=(delta(1)+delta(2)*Vxhat(1,2)/Vxhat(1,1)+bahat(1)+bahat(2)*Vxhat(1,2)/Vxhat(1,1))/(bHat(1)+bHat(2)*Vxhat(1,2)/Vxhat(1,1))
tauhat=(aHat'*inv(Ahat)-bHat')*Vxhat*aHat/((aHat'*inv(Ahat)-bHat')*Vxhat*bHat)

delta=(aHat'-bHat'*Ahat)*inv(Ahat);

% NO EXCLUSION RESTRICTIONS

tau=0.5;

display('--------- MP shock when state is unknown, wrong tau--------');
d2u05=(delta-bHat'*(tau*eye(2,2)-Ahat))'

tau=1.5;

display('--------- MP shock when state is unknown, right tau--------');
d2u15=(delta-bHat'*(tau*eye(2,2)-Ahat))'

% CORRECT EXCLUSION RESTRICTIONS
% This is unfinished
%bahat=bHat'*Ahat;
display('--------- identified tau  --------');
%tau=(delta(1)+delta(2)*Vxhat(1,2)/Vxhat(1,1)+bahat(1)+bahat(2)*Vxhat(1,2)/Vxhat(1,1))/(bHat(1)+bHat(2)*Vxhat(1,2)/Vxhat(1,1))
tau=(aHat'*inv(Ahat)-bHat')*Vxhat*aHat/((aHat'*inv(Ahat)-bHat')*Vxhat*bHat)



