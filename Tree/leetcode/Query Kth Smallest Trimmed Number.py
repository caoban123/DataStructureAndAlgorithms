nums = ["9415","5908","1840","5307"]
queries = [[3,2],[2,2],[3,3],[1,3]]
def get_digit(num, i):
    return int(num[-1 - i]) if i < len(num) else 0

# Tiền xử lý chỉ một lần: Tạo ra danh sách các chuỗi đã cắt theo từng độ dài trim
trimmed_nums = []
max_len = max(len(num) for num in nums)  # Tính độ dài lớn nhất của số trong nums
for trim_length in range(1, max_len + 1):
    trimmed_nums.append([(num[-trim_length:], i) for i, num in enumerate(nums)])
    print([(num[-trim_length:], i) for i, num in enumerate(nums)])

# Đối với mỗi query, chỉ cần lấy số đã trim và sắp xếp một lần
lst = []
for query in queries:
    k = query[0] - 1  # K-th smallest element (1-based index)
    trim = query[1]  # Số chữ số cần trim
    trimmed = trimmed_nums[trim - 1]  # Truy cập phần tử đã trim trước đó
    sorted_trimmed = sorted(trimmed, key=lambda x: x[0])  # Sắp xếp theo giá trị cắt
    lst.append(sorted_trimmed[k][1])  # Thêm chỉ số vào kết quả
print(lst)
