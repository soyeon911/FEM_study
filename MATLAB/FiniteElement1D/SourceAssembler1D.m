function b = SourceAssembler1D(x, f, kappa, g)
    n = length(x) - 1; % 구간 개수
    b = zeros(n + 1, 1); % 로드 벡터 초기화

    % 내부 열원 계산
    for i = 1:n
        h = x(i + 1) - x(i); % 현재 구간 길이
        xmid = (x(i + 1) + x(i)) / 2; % 구간 중간점
        fmid = f(xmid); % 열원 값

        % 중간점 구적법을 사용하여 로드 벡터 계산
        b(i) = b(i) + fmid * h / 2;
        b(i + 1) = b(i + 1) + fmid * h / 2;
    end

    % 경계 데이터 추가
    b(1) = b(1) + kappa(1) * g(1); % 왼쪽 경계
    b(end) = b(end) + kappa(2) * g(2); % 오른쪽 경계
end
