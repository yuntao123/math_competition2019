
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans, KMeans


from data import get_data
import openpyxl

outwb = openpyxl.Workbook()  # 打开一个将写的文件
outws = outwb.create_sheet(index=0)  # 在将写的文件创建she

x= get_data(0,3)  # 提取所有列数据
x2= get_data(1,2)  # 提取所有列数据
x3= get_data(2,3)  # 提取所有列数据



# 定义四个簇类中心
centers1 = [[-0.268,-1.09,-0.015],[-21.76,-16.34,-11.42],[-75.76,-46.55,-41.96]]
centers2 = [[-0.268,-1.09,-0.015],[-75.76,-46.55,-41.96]]



# # 若我们选择k=2
k_means = KMeans(init='k-means++', n_clusters=4, n_init=10,random_state=10)
y_pred = k_means.fit_predict(x)
# plt.scatter(x[:, 0], x[:, 1],x[:, 2], c=y_pred)
# plt.show()

ax=plt.subplot(111,projection='3d')
y1, y2 = x[:, 0], x[:, 1]
z = x[:, 2]
ax.scatter(y1, y2,z ,c=y_pred)
plt.show()
plt.show()




scores2 = metrics.calinski_harabaz_score(x,y_pred)
print("the Calinski-Harabasz scores(k=2) is: ",scores2)
