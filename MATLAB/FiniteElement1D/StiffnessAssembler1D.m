function A = StiffnessAssembler1D(x, a, kappa)
    n = length(x) - 1; % 구간 개수
    A = zeros(n + 1, n + 1); % 강성 행렬 초기화

    for i = 1:n
        h = x(i + 1) - x(i); % 현재 구간의 길이
        xmid = (x(i + 1) + x(i)) / 2; % 구간 중간점
        amid = a(xmid); % 열전도도 값

        % 지역 강성 행렬 계산
        A(i, i) = A(i, i) + amid / h;
        A(i, i + 1) = A(i, i + 1) - amid / h;
        A(i + 1, i) = A(i + 1, i) - amid / h;
        A(i + 1, i + 1) = A(i + 1, i + 1) + amid / h;
    end

    % 경계 조건 반영
    A(1, 1) = A(1, 1) + kappa(1); % 왼쪽 경계 (x = 2)
    A(end, end) = A(end, end) + kappa(2); % 오른쪽 경계 (x = 8)
end
