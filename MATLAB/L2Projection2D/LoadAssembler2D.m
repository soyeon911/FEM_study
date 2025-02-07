function b = LoadAssembler2D(p,t,f)
    np = size(p,2); % 노드 개수
    nt = size(t,2); % 요소 개수
    b = zeros(np,1); % 로드 벡터 초기화

    for K = 1:nt  % 각 삼각형 요소에 대해 반복
        loc2glb = t(1:3,K); % 로컬-글로벌 매핑
        x = p(1,loc2glb); % x 좌표
        y = p(2,loc2glb); % y 좌표
        area = polyarea(x,y); % 삼각형 면적 계산

        % 로컬 로드 벡터 (Load Vector)
        bK = [f(x(1),y(1));
              f(x(2),y(2));
              f(x(3),y(3))] / 3 * area; 
        
        % 글로벌 로드 벡터에 추가
        b(loc2glb) = b(loc2glb) + bK;
    end
end
