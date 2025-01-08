function M = MassAssembler1D(x)
    n = length(x) - 1; % number of subintervals
    M = zeros(n + 1, n + 1); % initialize the mass matrix
    for i = 1:n
        h = x(i + 1) - x(i); % length of the current subinterval
        M(i, i) = M(i, i) + h / 3; % diagonal entry for node i
        M(i, i + 1) = M(i, i + 1) + h / 6; % off-diagonal entry
        M(i + 1, i) = M(i + 1, i) + h / 6; % symmetric entry
        M(i + 1, i + 1) = M(i + 1, i + 1) + h / 3; % diagonal entry for node i+1
    end
end
