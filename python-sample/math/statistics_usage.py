# %%
import statistics

data = [1, 2, 3, 4, 5, 6, 7, 4, 5, 6, 2, 3, 4, 4, 4, 4]

print(f"平均数: {statistics.mean(data)}")
print(f"中位数: {statistics.median(data)}")
print(f"方差: {statistics.variance(data)}")
print(f"标准差: {statistics.stdev(data)}")
print(f"众数: {statistics.mode(data)}")

# %%
