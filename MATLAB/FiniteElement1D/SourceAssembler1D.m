function b = SourceAssembler1D(x, f, kappa, g)
b = LoadAssembler1D(x, f); % 기본 로드 벡터
b(1) = b(1) + kappa(1) * g(1); % 왼쪽 경계 데이터 추가
b(end) = b(end) + kappa(2) * g(2); % 오른쪽 경계 데이터 추가
end