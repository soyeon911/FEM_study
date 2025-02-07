function L2Projector2D()
    g = [2 0 1 0 1 1 0;  % 단순 사각형 도메인 정의 (직접 입력)
         2 1 1 0 1 1 0;
         2 1 0 1 1 1 0;
         2 0 0 1 1 1 0]';
    
    [p,e,t] = initmesh(g, 'hmax', 0.1); % 메쉬 생성
    M = MassAssembler2D(p,t); % 질량 행렬 조립
    b = LoadAssembler2D(p,t,@Foo2); % 하중 벡터 조립
    Pf = M\b; % 선형 시스템 해 구하기

    % 🔹 변경된 부분: 'pdesurf' 대신 'pdeplot' 사용
    figure;
    pdeplot(p, e, t, 'XYData', Pf, 'ZData', Pf, 'Mesh', 'on');
    colorbar;
    title('L2 Projection of f(x, y)');
end
