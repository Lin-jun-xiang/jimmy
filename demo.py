
import pandas as pd
import csv
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt
import matplotlib as mpl  # 改變屬性,排版
import json
import os
import copy
import seaborn as sns
from matplotlib.ticker import MultipleLocator


# -------------------------------------------------------------------- 讀取資料夾中所有json檔案
class Test:
    def __init__(self, paths):
        self.paths = paths

    def read(self):
        os.listdir(self.paths)
        Data = []
        for info in os.listdir(self.paths):
            domain = os.path.abspath(self.paths)  # 获取文件夹的路径，此处其实没必要这么写，目的是为了熟悉os的文件夹操作
            info = os.path.join(domain, info)  # 将路径与文件名结合起来就是每个文件的完整路径
            a = open(info, 'r')  # 读取文件内容
            Data += [json.load(a)]  # json.load(檔案物件)
        pass
        return Data

    pass


pass

t = Test(r'C:\\json\\gp_well')
My_Data = []
My_Data += t.read()


##=================================================================================== 將粒徑代號歸類Fine,Coarse,Mud....
# class P():
#     def __init__(self, My_Data, well_number):
#         self.My_Data = My_Data
#         self.well_number = well_number
#
#     def p(self):
#         q = []
#         w = []
#         r = []
#         propertys = []
#         Top = []
#         Bottom = []
#         t1 = []
#         q = self.My_Data[self.well_number]
#         w = q['RockType']
#         r = w['Rocks']
#
#         j = 0
#         for index in r:
#             t = r[j]
#             t1 += {t['TYPE_OF_ROCK']}
#
#             Top += [float(t['TOP_DEPTH'])]  # 口井的TOP資料
#             Bottom += [float(t['BOTTOM_DEPTH'])]  # 口井的BOTTOM資料
#
#             if t1[j] == 'fS' or t1 == 'vfS':  # 細沙條件
#                 propertys += ['Fine']
#
#             elif t1[j] == 'fG' or t1[j] == 'mG' or t1[j] == 'cG' or t1[j] == 'vcG' or t1[j][-1] == 'G':  # 礫石條件
#                 propertys += ['Coarse']
#
#             elif t1[j] == 'C' or t1[j] == 'Z' or t1[j] == 'M' or t1[j][-1] == 'M' or t1[j][-1] == 'Z':  # 泥石條件
#                 propertys += ['Mud']
#
#             elif t1[j] == 'cS' or t1[j] == 'vcS' or t1[j] == 'mS' or t1[j][-1] == 'S':  # 砂礫條件
#                 propertys += ['Middle']
#
#             else:  # 混合岩石
#                 propertys += ['Mix']
#
#             j = j + 1
#
#         pass
#         return propertys, Top, Bottom
#
#     pass
#
#
# pass
#
# # 呼叫涵式,取出13口井的需要資料
# well_data = []
# i = 0
# for y in range(0, 13):
#     x = P(My_Data, i)
#     well_data += [x.p()]
#     i = i + 1
#     pass


##===================================================================================合併重複的層面
# class Merge():
#     def __init__(self, well_data, i, j):
#         self.well_data = well_data
#         self.P_index = [0]
#         self.i = i
#         self.j = j
#
#         pass
#
#     def merge_P(self):
#         P = []
#         self.P_index = [0]
#         for index in self.well_data[self.i][0]:
#             if self.well_data[self.i][0][self.j] == well_data[self.i][0][self.j - 1]:
#                 pass
#
#             else:
#                 P += [self.well_data[self.i][0][self.j - 1]]
#                 self.P_index += [self.j]
#                 pass
#             self.j = self.j + 1
#         pass
#         pass
#
#         Propertys = P[1:] + [well_data[self.i][0][self.j - 1]]
#         self.P_index = self.P_index[1:]
#         return Propertys
#
#     def merge_Depth(self):
#         depth = []
#         k = 0
#         for index in self.P_index:
#             l = self.P_index[k]
#             depth += [self.well_data[self.i][1][l]]
#             k = k + 1
#         pass
#         depth += [self.well_data[self.i][2][self.j - 1]]
#         return depth
#
#     pass
#
#
# pass
#
# # 全部口井的屬性與深度分布
# Propertys = []
# depth = []
# i = 0
# for x in range(0, 13):
#     s = Merge(well_data, i, 0)
#     Propertys += [s.merge_P()]
#     depth += [s.merge_Depth()]
#     if well_data[i][0][0] == well_data[i][0][-1]:
#         Propertys[i].insert(0, well_data[i][0][0])
#         depth[i].insert(0, 0)
#     else:
#         pass
#     i = i + 1
#     pass
# Propertys[10].pop()  # 因為第10口 特別 出現coarse 重複

##===================================================================================
Propertys = [[] for x in range(13)]
depth = [[] for x in range(13)]
i = 0
for x in  range(13):
    j = 0
    for y in My_Data[i]['RockType']['Rocks']:
        Propertys[i] += [copy.deepcopy(My_Data[i]['RockType']['Rocks'][j]['TYPE_OF_ROCK'])]
        depth[i] += [float(copy.deepcopy(My_Data[i]['RockType']['Rocks'][j]['TOP_DEPTH']))]
        j = j+1
    pass
    depth[i] += [float(copy.deepcopy(My_Data[i]['RockType']['Rocks'][-1]['BOTTOM_DEPTH']))]
    i = i+1
pass

##===================================================================================岩層過薄,進行處理
class REMOVE():
    def __init__(self, Propertys, depth, merge_depth):
        self.Propertys = Propertys
        self.depth = depth
        self.merge_depth = merge_depth

    def rem(self):
        # 先處理第一層
        i = 0
        for x in range(13):
            if abs(self.depth[i][1] - self.depth[i][0]) < 1:
                self.Propertys[i][0] = 'Middle'  # 背景值
            else:
                pass
            i = i + 1
        pass
        # 進行深層處理
        i = 0
        for x in range(13):
            j = 1
            k = 0
            for y in self.depth[i][1:-1]:
                if abs(self.depth[i][j + 1] - self.depth[i][j]) < self.merge_depth: # <self.merge_depth使用者輸入
                    self.Propertys[i][j] = self.Propertys[i][j - 1]

                else:
                    pass
                j = j + 1
            pass
            i = i + 1
        pass
        return self.Propertys, self.depth


pass
merge_depth = input("enter merge_depth(unit-m): ")
a = REMOVE(Propertys, depth, float(merge_depth))
aa = a.rem()

##=================================================================================== 再次合併重複層
i = 0
Well_data = [[[] for x in range(3)] for x in range(13)]
for x in range(13):
    Well_data[i][0] = copy.deepcopy(Propertys[i])
    Well_data[i][1] = copy.deepcopy(depth[i][:-1])
    Well_data[i][2] = copy.deepcopy(depth[i][1:])
    i = i + 1

Propertys = [[] for x in range(13)]
P_index = [[] for x in range(13)]
i = 0
for x in range(13):
    j = 1
    for y in Well_data[i][0][1:]:
        if Well_data[i][0][j] == Well_data[i][0][j - 1]:
            pass
        else:
            Propertys[i] += [Well_data[i][0][j - 1]]
            P_index[i] += [j]
        pass
        j = j + 1
    pass
    Propertys[i] += [Well_data[i][0][-1]]
    P_index[i].insert(0, 0)
    i = i + 1
pass
depth = [[] for x in range(13)]
i = 0
for x in range(13):
    j = 0
    for x in P_index[i]:
        depth[i] += [Well_data[i][1][P_index[i][j]]]
        j = j + 1
    pass
    depth[i] += [Well_data[i][2][-1]]
    i = i + 1

##=================================================================================== 將depth分成top,bottom
top = []
bottom = []
i = 0
for x in range(0, 13):
    top += [depth[i][:-1]]
    bottom += [depth[i][1:]]
    i = i + 1
    pass


##=================================================================================== 繪製直方圖
# 先將井口名字座標等資料存放
well_information = [['站名','經度','緯度','TWD67_X','TWD67_Y','TWD97_X','TWD97_Y'],
                    ['潮寮-120301G1','120.425263','22.564217','190064','2496351','190894','2496142'],
                    ['永芳-120302G1','120.394062','22.605260','186871','2500908','187703','2500700'],
                    ['昭明-120303G1','120.409126','22.541269','188393','2493814','189224','2493608'],
                    ['中洲-121901G1','120.479098','22.845351','195709','2527460','196539','2527252'],
                    ['海豐-130102G1','120.506415','22.698220','198456','2511157','199289','2510951'],
                    ['前進-130103G1','120.459757','22.650066','193644','2505842','194476','2505635'],
                    ['萬丹-130502G1','120.469529','22.614359','194634','2501884','195466','2501678'],
                    ['繁華-130601G1','120.572286','22.703347','205227','2511703','206058','2511497'],
                    ['九如-130801G1','120.489790','22.736339','196765','2515385','197595','2515177'],
                    ['鹽埔-131001G1','120.575100','22.753963','205534','2517308','206363','2517101'],
                    ['高樹-131101G1','120.599190','22.827554','208030','2525451','208859','2525243'],
                    ['泰山-131102G1','120.610801','22.790507','209211','2521343','210040','2521138'],
                    ['關福-131104G1','120.617187','22.764879','209859','2518505','210689','2518298']]

# --------------------------------------------------------------------------
class P(): # 先將particle_size轉為座標直
    def __init__(self, Propertys):
        self.Propertys = Propertys

    def p(self):
        particle_sign = ['0', 'C', 'M', 'Z', 'vfS', 'fS', 'mS', 'vcS', 'cS','S', 'fG', 'mG', 'vcG', 'cG','G', 'B','L']
        particle_size = [[] for x in range(13)] # 將符號代表轉換成粒徑比例,以做hist圖
        i = 0
        for x in range(13):
            j = 0
            for y in self.Propertys[i]:
                k = 0
                for z in particle_sign:
                    if str(self.Propertys[i][j]).endswith(particle_sign[k]): # 判斷字串最後是甚麼
                        particle_size[i] += [k]
                        break
                    else:
                        pass
                    k = k+1
                pass
                j = j+1
            pass
            i = i+1
        pass
        return particle_size
pass

q = P(Propertys)
particle_size = q.p()  # 代號'L'代表無資料
# --------------------------------------------------------------------------
# 因前面的 particle_size的vcs,cs粒徑比值有對調(為了不出現字串判斷的問題),需調正
i = 0
for x in range(13):
    j = 0
    for y in particle_size[i]:
        if particle_size[i][j] == 7:
            particle_size[i][j] = 8
        elif particle_size[i][j] == 8:
            particle_size[i][j] = 7
        elif particle_size[i][j] == 12:
            particle_size[i][j] = 13
        elif particle_size[i][j] == 13:
            particle_size[i][j] = 12
        else:
            pass
        j = j+1
    pass
    i = i+1
pass
# -------------------------------------------------------------------------- 為了作圖,將數字代號相同的再次合併,以達到最精簡
class merge_number():
    def __init__(self,depth,particle_size):
        self.depth = depth
        self.particle_size = particle_size
    def merge(self):
        particle_size = [[] for x in range(13)]
        depth = [[] for x in range(13)]
        i = 0
        for x in range(13):
            particle_size[i] += [self.particle_size[i][0]]
            depth[i] += [self.depth[i][0]]
            j = 1
            for y in self.particle_size[i][1:]:
                if self.particle_size[i][j] == self.particle_size[i][j-1]:
                    pass
                else :
                    particle_size[i] += [self.particle_size[i][j]]
                    depth[i] += [self.depth[i][j]]
                pass
                j = j+1
            pass
            depth[i] += [self.depth[i][j]]
            i = i+1
        pass
        return depth , particle_size
pass
g = merge_number(depth,particle_size)
gg = g.merge()

i = 0
for x in range(13):
    particle_size[i] = gg[1][i]
    depth[i] = gg[0][i]
    i = i+1
pass

# --------------------------------------------------------------------------
# 上圖
class Plot():
    def __init__(self,particle_size,depth,i):
        self.particle_size = particle_size
        self.depth = depth
        self.i = i
    def P(self):
        sns.set_style('whitegrid')
        fig = plt.figure(figsize=(10, 50))
        particle_sign = ['0', 'C', 'M', 'Z', 'vfS', 'fS', 'mS', 'cS', 'vcS','S', 'fG', 'mG', 'cG', 'vcG','G','B','L']
        # data1 = pd.Series(self.particle_size[self.i], index=self.depth[self.i][1:])
        df = pd.DataFrame({'x': self.particle_size[self.i],
                           'y': self.depth[self.i][1:]})
        # 顏色設定
        colors = []
        k = 0
        for x in df['x']:
            if df['x'][k] <= 3:
                colors += ['darkorange']
            elif df['x'][k] <= 5 and df['x'][k] > 3:
                colors += ['yellow']
            elif df['x'][k] <= 9 and df['x'][k] > 5:
                colors += ['lime']
            elif df['x'][k] <= 14 and df['x'][k] > 9:
                colors += ['aqua']
            else:
                colors += ['gray']
            k = k + 1
        pass
        plt.ylabel('Depth')
        plt.xlabel('particle_sign')
        mpl.rcParams['font.family'] = 'Microsoft Yahei'  # 允許中文字導入
        plt.text(-1, -20, s=well_information[int(well_number) + 1][0], fontsize=20)  # 井口名字
        plt.text(4, -30, s='經度:' + well_information[int(well_number) + 1][1])
        plt.text(4, -15, s='緯度:' + well_information[int(well_number) + 1][2])
        plt.text(7, -30, s='TWD97-X:' + well_information[int(well_number) + 1][5])
        plt.text(7, -15, s='TWD97-Y:' + well_information[int(well_number) + 1][6])

        wid = copy.deepcopy(df['y'])
        wid = wid.tolist()
        wid.insert(0, 0.0)
        widths = []
        i = 1
        for x in df['y']:
            widths += [round((wid[i] - wid[i-1]),4)]
            i = i + 1
        pass
        i = 0
        for x in df['x']:
            # plt.barh(bottom,widths,height)/(在y軸長條中間對應位置,在x軸長度,長條的寬度)
            p1 = plt.barh(0.5*(float(wid[i])+float(wid[i+1])),width = df['x'][i],height = widths[i], color=colors[i])
            i = i + 1
        pass
        ax = plt.gca()
        ax.invert_yaxis()
        plt.xticks(range(17), particle_sign)  # 自訂x軸的刻度
        # yminorLocator = MultipleLocator(10)
        # ax.yaxis.set_minor_locator(yminorLocator)
pass

# well_number = input("enter well_number of fig: ")
# g= Plot(particle_size,depth,int(well_number))
# gp_fig = g.P()


# 一次性繪圖
well_number = 0;
for x in range(len(My_Data)):
    g = Plot(particle_size,depth,well_number)
    g.fig = g.P()
    well_number = well_number+1
pass


# -------------------------------------------------------------------------- 鼠標事件
# i = int(input("enter well_number of fig: "))
# data1 = pd.Series(particle_size[i], index=depth[i][1:])
#
# df = pd.DataFrame({'x': particle_size[i],
#                    'y': depth[i][1:]})
# colors = []
# k = 0
# for x in df['x']:
#     if df['x'][k] <= 3:
#         colors += ['darkorange']
#     elif df['x'][k] <= 5 and df['x'][k] > 3:
#         colors += ['yellow']
#     elif df['x'][k] <= 9 and df['x'][k] > 5:
#         colors += ['lime']
#     elif df['x'][k] <= 14 and df['x'][k] > 9:
#         colors += ['aqua']
#     else:
#         colors += ['gray']
#     k = k + 1
# pass
#
# wid = copy.deepcopy(df['y'])
# wid = wid.tolist()
# wid.insert(0, 0.0)
# widths = []
# i = 1
# for x in df['y']:
#     widths += [round((wid[i]-wid[i-1]),4)]
#     i=i+1
# # --------------------------------------------------------------------------
# fig = plt.figure(figsize = (10,50))
# po_annotation = [] # 註釋
# i =0
# for index in df['x']:
#     point, = plt.barh(0.5*(float(wid[i])+float(wid[i+1])), df['x'][i],color=colors[i],height = widths[i])
#     annotation = plt.annotate(('x=' + str(df['y'][i]), 'y=' + str(df['x'][i])), xy=(df['y'][i] + 0.1, df['x'][i] + 0.1), xycoords='data',
#                               xytext=(14,20),
#                               textcoords='data', horizontalalignment="left",
#                               )
#     annotation.set_visible(False)
#     po_annotation.append([point, annotation])
#     i = i+1
# pass
# # --------------------------------------------------------------------------
# def on_move(event): # 鼠標觸發事件
#     visibility_changed = False # 預設為False
#     for point, annotation in po_annotation:
#         should_be_visible = (point.contains(event)[0] == True)
#         # 若觸發事件,則should_be_visible = True
#
#         if should_be_visible != annotation.get_visible():
#             visibility_changed = True
#             annotation.set_visible(should_be_visible)
#             # 因預設為False,當should_be_visible = True時,進入此if條件句
#
#     if visibility_changed:
#         plt.draw()
#
#
# on_move_id = fig.canvas.mpl_connect('motion_notify_event', on_move) # 此事件即代表鼠標移到某個座標上
#
# particle_sign = ['0', 'C', 'M', 'Z', 'vfS', 'fS', 'mS', 'cS', 'vcS','S', 'fG', 'mG', 'cG', 'vcG','G', 'B','L']
# plt.xticks(range(17),particle_sign)
# plt.ylabel('Depth (m)')
# plt.xlabel('grain size')
#
# ax = plt.gca()
# ax.invert_yaxis() # 轉置y軸
# plt.show()
## 將值註釋在長條旁邊
# i = 0
# for x,y in enumerate(df['y']):
#     plt.text(df['x'][i],y+0.2,'%s'%y,va = 'center')
#     i = i+1
mpl.rcParams['font.family']='Microsoft Yahei' # 允許中文字導入
plt.text(-1,-20,s = well_information[int(well_number)][0],fontsize = 20) # 井口名字
plt.text(4,-30,s = '經度:'+well_information[int(well_number)][1])
plt.text(4,-15,s = '緯度:'+well_information[int(well_number)][2])
plt.text(7,-30,s = 'TWD97-X:'+well_information[int(well_number)][5])
plt.text(7,-15,s = 'TWD97-Y:'+well_information[int(well_number)][6])

