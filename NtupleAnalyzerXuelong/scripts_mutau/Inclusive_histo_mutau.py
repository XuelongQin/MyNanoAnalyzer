import sys
sys.path.append("..")
from pyFunc.GetHisto import variable,cate,gethisto_withFR_cate,getallhisto_mutau
from ROOT import TFile
import numpy as np

varname = sys.argv[1]
print (varname)

mvis = variable("mvis","m_{vis}",int(32),np.array([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,400,500],dtype=float))
taupt = variable("taupt","#tau p_{T}",int(34),np.array([30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
mupt = variable("mupt","#mu p_{T}",int(36),np.array([26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
Aco = variable("Acopl","acoplanarity",int(40),np.arange(0,1.025,0.025,dtype=float))
mtranse = variable("mtrans","m_{T}(#mu,MET)",int(36),np.arange(0,185,5,dtype=float))
nTrk = variable("nTrk","N_{tracks}",int(50),np.arange(0,102,2,dtype=float))
MET = variable("MET_pt","MET",int(19),np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,80,90,100,110,120],dtype=float))
taueta = variable("taueta","#tau #eta", int(25), np.arange(-2.5,2.7,0.2,dtype=float))
mueta = variable("mueta","#mu #eta", int(25), np.arange(-2.5,2.7,0.2,dtype=float))
#variablelist = [mvis,taupt,mupt,Aco,mtranse]
variablelist = [mvis,taupt,mupt,Aco,mtranse,nTrk,MET,taueta,mueta]
for var in variablelist:
    if varname == var.name:
        fout = TFile("./Inclusive_mutau_2018_{}.root".format(var.name),"recreate")
        fout.mkdir("full")
        cut = "nTrk>=0 && taupt>30 && mvis>40"
        if var.name!="mtrans":
            cut = cut + " && mtrans<75"
        print ("Begin to generate histo of variable ", var.name, " with cut ", cut)
        cutname = "Inclusive"
        histotuple = getallhisto_mutau(cut,"Inclusive",var)
        fout.cd("full")
        for histo in histotuple:
            histo.Write() 
        fout.Close()