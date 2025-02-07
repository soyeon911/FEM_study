function M = MassAssembler2D(p,t)
    np = size(p,2); % 노드 개수
    nt = size(t,2); % 요소 개수
    M = sparse(np,np); % 희소 행렬로 초기화

    for K = 1:nt  % 각 삼각형 요소에 대해 반복
        loc2glb = t(1:3,K); % 로컬-글로벌 매핑
        x = p(1,loc2glb); % x 좌표
        y = p(2,loc2glb); % y 좌표
        area = polyarea(x,y); % 삼각형 면적 계산

        % 로컬 질량 행렬 (Mass Matrix)
        MK = [2 1 1;
              1 2 1;
              1 1 2] / 12 * area; 
        
        % 글로벌 질량 행렬에 추가
        M(loc2glb,loc2glb) = M(loc2glb,loc2glb) + MK;
    end
end
