
function Ex = E(x,p)
Ex = sum(x.*p);
end

function COVx = COV(x,p)
Ex = E(x,p);
COVx = E((x-Ex).^2,p);
end

x_min = 0; x_max = 10; %meter
x=linspace(x_min,x_max,100); % converted to 100 bins
pd_x = makedist('Normal','mu',0.5,'sigma',0.25);

% robot position belief
p_x = pdf(pd_x,x); % P(x)
eta = sum(p_x);
p_x = 1/eta*p_x; % now p sums up to 1
bar(x,p_x)

Ex = E(x,p_x) % = 3.00
COVx = COV(x,p_x) % = 0.25^2