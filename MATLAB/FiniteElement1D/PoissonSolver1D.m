function PoissonSolver1D()
    h = 0.1; % 메쉬 간격
    x = 2:h:8; % 메쉬 생성
    kappa = [1e6, 0]; % 경계 조건 매개변수 [β0, βL]
    g = [1, 0]; % 경계값 [g0, gL]

    % 강성 행렬과 로드 벡터 계산
    A = StiffnessAssembler1D(x, @Conductivity, kappa);
    b = SourceAssembler1D(x, @Source, kappa, g);

    % 선형 시스템 풀이
    u = A \ b;

    % 온도 분포 그래프 출력
    plot(x, u, '-o');
    xlabel('x');
    ylabel('Temperature T(x)');
    title('Temperature Distribution in the Rod');
    grid on;
end
