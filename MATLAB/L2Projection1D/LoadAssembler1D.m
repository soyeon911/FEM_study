function b = LoadAssembler1D(x, f)
    n = length(x) - 1; % number of subintervals
    b = zeros(n + 1, 1); % initialize the load vector
    for i = 1:n
        h = x(i + 1) - x(i); % length of the current subinterval
        b(i) = b(i) + f(x(i)) * h / 2; % contribution at node i
        b(i + 1) = b(i + 1) + f(x(i + 1)) * h / 2; % contribution at node i+1
    end
end
