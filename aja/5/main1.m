function main1
    ic = csvread('in.txt');
    i = 1;
    while (i <= length(ic))
        instr = num2str(ic(i));
        while length(instr) < 5
            instr = ['0',instr]; %#ok<AGROW>
        end
        operands = zeros(1,3);
        for j=2:length(instr)-1
            if i+j-1 > length(ic)
                break;
            end
            if instr(end-j) == '0'
                operands(j-1) = ic(i+j-1)+1;
            else
                operands(j-1) = i+j-1;
            end
        end
        switch instr(end-1:end)
            case '01'
                ic(operands(3)) = ic(operands(1)) + ic(operands(2));
                i = i + 4;
            case '02'
                ic(operands(3)) = ic(operands(1)) * ic(operands(2));
                i = i + 4;
            case '03'
                x = input('Input: ');
                ic(ic(i+1)+1) = x;
                i = i + 2;
            case '04'
                disp(ic(ic(i+1)+1));
                i = i + 2;
            case '99'
                break;
            otherwise
                disp('oops');
                break;
        end
    end
end