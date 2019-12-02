for i = 1:100
    for j = i:100
        if main1(i,j) == 19690720
            disp(100 * i + j);
            break;
        end
    end
end