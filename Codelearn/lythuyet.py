#0 Toán tử in và not in
#Kiểm tra một chuỗi nằm trong một chuỗi khác hay không, kết quả trả về true hoặc false
#1 Toán tử in và not in. Kiểm tra một chuỗi nằm trong một chuỗi khác hay không, kết quả trả về true hoặc false;
#2 Phương thức upper(), lower() Trả về một chuỗi được viết hoa hoặc viết thường;
#3 Phương thức isupper(), islower() Trả về true hoặc false nếu một chuỗi (chữ cái) có được viết hoa hay viết thường toàn bộ xâu
#4 Phương thức isalpha(): trả về True nếu chuỗi chỉ chứa các ký tự chữ cái và không có ký tự trắng, còn lại trả về False
#5 Phương thức isnumeric(), isdecimal() Trả về True nếu chuỗi chỉ chứa các ký tự chữ số và không có ký tự trắng, còn lại trả về False
#6 Phương thức isalnum(): trả về True nếu chuỗi chỉ chứa các ký tự chữ cái hoặc chữ số và không có ký tự trắng, còn lại trả về False;
#7 Phương thức isspace(): trả về True nếu chuỗi chỉ chứa các ký tự trắng, hoặc dấu tab, hoặc dấu ngắt dòng, còn lại trả về False;
#8 Phương thức istitle(): trả về True nếu chuỗi chỉ chứa các từ, mỗi từ được viết thường và viết hoa chữ cái đầu, còn lại trả về False;
#9 Phương thức startswith(str): Trả về True nếu chuỗi bắt đầu bởi chuỗi str; endswith(str): Trả về True nếu chuỗi kết thúc bởi chuỗi str, còn lại trả về False;
#10 Phương thức join(ListOfString): ListOfString là một List gồm các chuỗi ký tự. join() dùng để nối các phần tử trong ListOfString bằng một chuỗi tương ứng của phương thức;
#11 Phương thức split(str): dùng để tách mỗi từ nằm trong chuỗi tương ứng thành một list, mỗi phần tử nằm trong list là một chuỗi con;
#12 Phương thức rjust(n,ch), ljust(n,ch), center(n,ch) Trả về một chuỗi mới khi thêm vào chuỗi gốc các ký tự ch, sao cho chiều dài của chuỗi đúng bằng n ký tự và chuỗi gốc được đặt nằm bên phải (rjust()), bên trái (ljust()) hoặc ở giữa (center());
#13 Phương thức strip(str), rstrip(str), and lstrip(str) Trả về một chuỗi mới trong đó đã xóa các ký tự có trong chuỗi str ở 2 đầu (strip()), bên phải (rstrip()) hoặc bên trái (lstrip()) chuỗi gốc
#14 Phương thức find(str,n)
    #Thực hiện tìm chuỗi str trong chuỗi gốc, bắt đầu từ ký tự có số chỉ mục n, n để trống thì mặc định bằng 0.
    #Trả về vị trí (index) lần đầu được tìm thấy (từ trái sang phải). Nếu không tìm thấy thì trả về -1
#15 Phương thức replace(oldvalue, newvalue, n)
    #Tìm và thay thế các chuỗi oldvalue xuất hiện trong chuỗi gốc bằng newvalue, với n lần tìm và thay thế; Nếu không có n: thì mặc định là tất cả các lần xuất hiện.
#16 Pop(i) method Thực hiện xóa và lấy ra giá trị của phần tử có số chỉ mục i trong List. Nếu tham số i để trống thì mặc định là lấy phần tử cuối trong List.
#17 Sort() method Cho phép sắp xếp các phần tử trong List có thứ tự;
#18 Remove() 
        #Phân biệt giữa hàm del() và phương thức remove()
        #Hàm del() xóa một phần tử khi biết index
        #Hàm remove() xóa một phần tử khi biết giá trị
#19 Index(x) method Trả về index của một phần tử được tìm thấy trong List;
        #Trong trường hợp x không tồn tại trong List sẽ bị lỗi  cần sử dụng cú pháp: if x in L để kiểm tra trước khi gọi phương thức index().
