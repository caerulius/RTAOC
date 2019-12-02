function ret=main1(noun,verb)
    ic = csvread('in.txt');
    ic(2) = noun;
    ic(3) = verb;
    i = 1;
    while (i <= length(ic))
        switch ic(i)
            case 1
                ic(ic(i+3)+1) = ic(ic(i+1)+1) + ic(ic(i+2)+1);
            case 2
                ic(ic(i+3)+1) = ic(ic(i+1)+1) * ic(ic(i+2)+1);
            case 99
                break;
            otherwise
                disp('oops');
        end
        i = i + 4;
    end

    ret = ic(1);
end