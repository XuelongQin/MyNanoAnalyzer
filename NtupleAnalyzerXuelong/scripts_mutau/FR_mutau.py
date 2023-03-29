import sys
sys.path.append("..")
from pyFunc.GetHisto import variable,cate,gethisto_cate,gethisto
from ROOT import TFile
import numpy as np
def getFRhisto(cut,cutname,variable):
    ST = cate("ST",["ST_t_top","ST_t_antitop","ST_tW_top","ST_tW_antitop"])
    VV = cate("VV",["WW2L2Nu","WZ2Q2L","WZ3LNu","ZZ2Q2L","ZZ2L2Nu","ZZ4L"])
    TT = cate("TT",["TTTo2L2Nu","TTToHadronic","TTToSemiLeptonic"])
    ZTT = cate("ZTT",["DYJetsToLL_M-50"])
    data_obs = cate("data_obs",["dataA","dataB","dataC","dataD"])
    weight = "xsweight*SFweight*Acoweight*npvsweight*nPUtrkweight*nHStrkweight"
    
    cutiso = cut+" && is_isolated"
    cutisoname = cutname + "_iso"
    
    cutisoreal = cutiso + "&& LepCand_gen[tauindex]!=0"
    cutisorealname = cutisoname + "_real"
    
    cutnoniso = cut+" && !is_isolated"
    cutnonisoname = cutname + "_noniso"
    cutnonisoreal = cutnoniso + "&& LepCand_gen[tauindex]!=0"
    cutnonisorealname = cutnonisoname + "_real"
    channel = "mutau"
    
    histoSTiso = gethisto_cate(ST,cutisoreal,cutisorealname,weight,variable,channel)
    histoVViso = gethisto_cate(VV,cutisoreal,cutisorealname,weight,variable,channel)
    histoTTiso = gethisto_cate(TT,cutisoreal,cutisorealname,weight,variable,channel)
    histoZTTiso = gethisto_cate(ZTT,cutisoreal,cutisorealname,weight,variable,channel)
    histodataiso = gethisto_cate(data_obs,cutiso,cutisoname,"1",variable,channel)
    histoiso = histodataiso.Clone("h_{}_{}_{}".format(variable.name,cutname,"dataiso_sub"))
    histoiso.Add(histoSTiso,-1)
    histoiso.Add(histoVViso,-1)
    histoiso.Add(histoTTiso,-1)
    histoiso.Add(histoZTTiso,-1)
    
 
    histoSTnoniso = gethisto_cate(ST,cutnonisoreal,cutnonisorealname,weight,variable,channel)
    histoVVnoniso = gethisto_cate(VV,cutnonisoreal,cutnonisorealname,weight,variable,channel)
    histoTTnoniso = gethisto_cate(TT,cutnonisoreal,cutnonisorealname,weight,variable,channel)
    histoZTTnoniso = gethisto_cate(ZTT,cutnonisoreal,cutnonisorealname,weight,variable,channel)
    histodatanoniso = gethisto_cate(data_obs,cutnoniso,cutnonisoname,"1",variable,channel)

    histononiso = histodatanoniso.Clone("h_{}_{}_{}".format(variable.name,cutname,"datanoniso_sub"))
    histononiso.Add(histoSTnoniso,-1)
    histononiso.Add(histoVVnoniso,-1)
    histononiso.Add(histoTTnoniso,-1)
    histononiso.Add(histoZTTnoniso,-1)
    
    for i in range(1,histoiso.GetNbinsX()+1):
        if histoiso.GetBinContent(i)<=0:
            histoiso.SetBinContent(i,0)
            histoiso.SetBinError(i,0)
        if histononiso.GetBinContent(i)<=0:
            histononiso.SetBinContent(i,0)
            histononiso.SetBinError(i,0)
    
    hFR = histoiso.Clone("hFR_{}_{}".format(variable.name,cutname))
    hFR.Divide(histononiso)

    if variable.name=="Acopl" or variable.name=="nTrk":
        ratio = histoiso.Integral(1,histoiso.GetNbinsX())/histononiso.Integral(1,histononiso.GetNbinsX())
        print ("ratio = ", ratio)
        for i in range(1,hFR.GetNbinsX()+1):
            print ("before i = ", i , " ",hFR.GetBinContent(i))
            hFR.SetBinContent(i,hFR.GetBinContent(i)/ratio)
            hFR.SetBinError(i,hFR.GetBinError(i)/ratio)
            print ("after i = ", i , " ",hFR.GetBinContent(i))
            print ("")
    return histoSTiso,histoVViso,histoTTiso,histoZTTiso,histoSTnoniso,histoVVnoniso,histoTTnoniso,histoZTTnoniso,histodataiso,histodatanoniso,histoiso,histononiso,hFR



taupt = variable("taupt","#tau_{h} p_{T}",int(11),np.array([30,35,40,45,50,60,80,100,150,200,250,300],dtype=float))
ntrk = variable("nTrk","N_{tracks}",int(24),np.array([-0.5,0.5,1.5,2.5,3.5,4.5,9.5,14.5,19.5,24.5,29.5,34.5,39.5,44.5,49.5,54.5,59.5,64.5,69.5,74.5,79.5,84.5,89.5,94.5,99.5],dtype=float))
Acopl = variable("Acopl","Acoplanarity",int(21),np.array([0,0.02,0.05,0.1,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1.00],dtype=float))

variablelist = [taupt, ntrk, Acopl]


fout = TFile("./FR_mutau.root","recreate")
for DM in [0,1,10,11]:
    for variable in variablelist:
        QCDcut = "mtrans<50 && !isOS && taupt>30 && mvis>40"
        Wcut = "isOS && mtrans>75 && taupt>30 && mvis>40"
        QCDcut = QCDcut+" && LepCand_DecayMode[tauindex]=={}".format(DM)
        QCDcutname = "QCD_DM{}".format(DM)
        histoQCDtuple = getFRhisto(QCDcut,QCDcutname,variable)
        Wcut = Wcut+" && LepCand_DecayMode[tauindex]=={}".format(DM)
        Wcutname = "W_DM{}".format(DM)
        histoWtuple= getFRhisto(Wcut,Wcutname,variable)
        fout.cd()
        for histoQCD in histoQCDtuple:
            histoQCD.Write()
        for histoW in histoWtuple:
            histoW.Write()
fout.Close()

