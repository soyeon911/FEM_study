function L2Projector1D()
    n = 5; % number of subintervals
    h = 1/n; % mesh size
    x = 0:h:1; % mesh points
    M = MassAssembler1D(x); % assemble mass matrix
    b = LoadAssembler1D(x, @Foo1); % assemble load vector
    Pf = M\b; % solve the linear system
    plot(x, Pf, '-o'); % plot the L^2 projection
    title('L^2 Projection');
    xlabel('x');
    ylabel('Projection');
end
