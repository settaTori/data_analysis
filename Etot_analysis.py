#原子間距離が記載されている.datファイルとクラスタリング.datファイルを参照するはず
import os
import numpy as np
import argparse
import matplotlib.pyplot as plt

def data_setup(Etot, Cluster, Dist1, Dist2):
    print("Now loading...")
    etot = np.loadtxt(Etot, skiprows = 0, unpack = True)
    flame, clus = np.loadtxt(Cluster, skiprows = 1, unpack = True, dtype = "int")
    flame2, dist1 = np.loadtxt(Dist1, skiprows = 1, unpack = True)
    flame3, dist2 = np.loadtxt(Dist2, skiprows = 1, unpack = True)
    Etot_analyzed_dat_create(etot, flame, dist1, dist2, clus)


def Etot_analyzed_dat_create(etot, flame, dist1, dist2, clus):
    time = flame * 0.01
    print("Now creating .dat file...")
    with open("Etot_active_site_dist.dat","w") as f:
        f.write("Flame    Energy           Dist(act)    Dist(Tyr55)" + "\n")
        number = 0
        for i,x in enumerate(clus):
            if x == 0 and dist1[i] < 2.75 and dist1[i] > 2.50 and dist2[i] < 2.40:
                number = number + 1
                f.write(str(flame[i]) + "    " + str('{:.4f}'.format(etot[i])) + "    " + str('{:.2f}'.format(dist1[i])) + "        " + str('{:.2f}'.format(dist2[i])) + "\n")
            
            elif x == 1 and dist2[i] < 2.75 and dist1[i] > 2.50 and dist2[i] < 2.40:
                number = number + 1
                f.write(str(flame[i]) + "    " + str('{:.4f}'.format(etot[i])) + "    " + str('{:.2f}'.format(dist1[i])) + "        " + str('{:.2f}'.format(dist2[i])) + "\n")

            elif x == 2 and dist1[i] < 2.75 and dist1[i] > 2.50 and dist2[i] < 2.40:
                number = number + 1
                f.write(str(flame[i]) + "    " + str('{:.4f}'.format(etot[i])) + "    " + str('{:.2f}'.format(dist1[i])) + "        " + str('{:.2f}'.format(dist2[i])) + "\n")

            elif x == 3 and dist1[i] < 2.75 and dist1[i] > 2.50 and dist2[i] < 2.40:
                number = number + 1
                f.write(str(flame[i]) + "    " + str('{:.4f}'.format(etot[i])) + "    " + str('{:.2f}'.format(dist1[i])) + "        " + str('{:.2f}'.format(dist2[i])) + "\n")
        f.write(str(number) + "\n")

    print("Succeeded!")
    print("Next Etot_graph_drawer")
    Etot_graph_drawer(etot, time, dist1, dist2, clus)

def Etot_graph_drawer(etot, time, dist1, dist2, clus):
    print("Now data setting...")
    c1_etot = [etot[i] for i,x in enumerate(clus) if x == 0 and dist1[i] < 2.75 and dist1[i] > 2.50 and dist2[i] < 2.40]
    time1 = [time[i] for i,x in enumerate(clus) if x == 0 and dist1[i] < 2.75 and dist1[i] > 2.50 and dist2[i] < 2.40]
    c2_etot = [etot[i] for i,x in enumerate(clus) if x == 1 and dist1[i] < 2.75 and dist1[i] > 2.50 and dist2[i] < 2.40]
    time2 = [time[i] for i,x in enumerate(clus) if x == 1 and dist1[i] < 2.75 and dist1[i] > 2.50 and dist2[i] < 2.40]
    c3_etot = [etot[i] for i,x in enumerate(clus) if x == 2 and dist1[i] < 2.75 and dist1[i] > 2.50 and dist2[i] < 2.40]
    time3 = [time[i] for i,x in enumerate(clus) if x == 2 and dist1[i] < 2.75 and dist1[i] > 2.50 and dist2[i] < 2.40]
    c4_etot = [etot[i] for i,x in enumerate(clus) if x == 3 and dist1[i] < 2.75 and dist1[i] > 2.50 and dist2[i] < 2.40]
    time4 = [time[i] for i,x in enumerate(clus) if x == 3 and dist1[i] < 2.75 and dist1[i] > 2.50 and dist2[i] < 2.40]
    others_etot = [etot[i] for i,x in enumerate(clus) if x > 3 or x < 0 and dist1[i] < 2.75 and dist1[i] > 2.50 and dist2[i] < 2.40]
    time_others = [time[i] for i,x in enumerate(clus) if x > 3 or x < 0 and dist1[i] < 2.75 and dist1[i] > 2.50 and dist2[i] < 2.40]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(time1, c1_etot, "o", color = "#0000cd", markersize = 5, alpha = 0.3)
    ax.plot(time2, c2_etot, "o", color = "#dc143c", markersize = 5, alpha = 0.3)
    ax.plot(time3, c3_etot, "o", color = "#228b22", markersize = 5, alpha = 0.3)
    ax.plot(time4, c4_etot, "o", color = "#ffa500", markersize = 5, alpha = 0.3)
    ax.plot(time_others, others_etot, "o", color = "#696969", markersize = 5, alpha = 1)
    ax.set_ylabel("energy / kcal/mol", fontsize = 15, labelpad = 15)
    ax.set_ylim(-132000,-126000)
    ax.set_xlabel("time / ns", fontsize = 15, labelpad = 15)
    ax.set_xlim(0,100)
    plt.rcParams["font.size"] = 8
    plt.show()
    print("Complete!!")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Etot",
                        help="total energy data file.")
    parser.add_argument("Cluster",
                        help="cluster data file.")
    parser.add_argument("Dist1",
                        help="distance data file")
    parser.add_argument("Dist2",
                        help="distance data file")
    args = parser.parse_args()
    Etot = args.Etot
    Cluster = args.Cluster
    Dist1 = args.Dist1
    Dist2 = args.Dist2
    data_setup(Etot, Cluster, Dist1, Dist2)



