# please click the master see my code 点击main 选择master 查看源码

### Seagate_ImageProcessing

需求分析：通过摄像头捕捉一张图片， 对其图片进行处理 ， 能够自动识别出LED灯是否亮

大致思路： 
1.先对捕捉的图片进行分析    
2.获取ROI区域(在这里即为LED周围区域)    
3.对其作高斯模糊处理以及HSV腐蚀等图像处理 使其有模糊变得更加高清    
4.呃呃 目前写到这里 正在学习采用何种方式 模版匹配 or 阈值处理 ？？     

1.Color Palette ： 制作一个BGR插件 调节按钮控制BGR的值可以获得不同的颜色   
2.Find Color： 读入一张图片 ， 点击任何一点 即可在控制台输出其 BGR HSV GRAY值   
3.MakeBorder： 对原始图片的边框进行填充处理   
4.main ： 主函数   
