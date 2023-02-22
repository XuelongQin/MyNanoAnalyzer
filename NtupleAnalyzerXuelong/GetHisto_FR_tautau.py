from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas,TH1F,TPaveText
from ROOT.RDF import TH1DModel
import numpy as np
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
time_start=timer.time()


class variable:
    def __init__(self, name, title, nbins, binning):
        self.name=name
        self.title = title
        self.nbins=nbins
        self.binning = binning
    
class cate:
    def __init__(self, name, samplelist):
        self.name=name
        self.samplelist=samplelist
        
        
def gethisto(sample,cut,cutname,weight,variable):
    
    f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/tautau/RDF/{}.root".format(sample))
    t1 = f1.Get("Events")
    f2 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/tautau/RDF/{}_friend.root".format(sample))
    t2 = f2.Get("ntrktuple")
    t1.AddFriend(t2,"friend")
    df = RDataFrame(t1)
    hmodel = TH1DModel("h_{}_{}_{}".format(variable.name,cutname,sample),"",variable.nbins,variable.binning)
    histo = df.Define("totalweight",weight).Filter(cut).Histo1D(hmodel,variable.name,"totalweight").GetPtr()
    histo.Sumw2()
    return histo


def gethistodata(sample,cut,cutname,variable):
    
    f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/tautau/RDF/{}.root".format(sample))
    t1 = f1.Get("Events")
    f2 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/tautau/RDF/{}_friend.root".format(sample))
    t2 = f2.Get("ntrktuple")
    t1.AddFriend(t2,"friend")
    df = RDataFrame(t1)
    hmodel = TH1DModel("h_{}_{}_{}".format(variable.name,cutname,sample),"",variable.nbins,variable.binning)
    histo = df.Filter(cut).Histo1D(hmodel,variable.name).GetPtr()
    histo.Sumw2()
    return histo



def gethisto_cate(cate, cut, cutname, weight, variable):
    h = TH1F("h_{}_{}_{}".format(variable.name,cutname,cate.name),"",variable.nbins,variable.binning)
    for sample in cate.samplelist:
        histo = gethisto(sample,cut,cutname,weight,variable)
        h.Add(histo,1)
    return h
        
def gethisto_catedata(cate, cut, cutname, variable):
    h = TH1F("h_{}_{}_{}".format(variable.name,cutname,cate.name),"",variable.nbins,variable.binning)
    for sample in cate.samplelist:
        histo = gethistodata(sample,cut,cutname,variable)
        h.Add(histo,1)
    return h

def getFRhisto(cut,cutname,variable):
    ST = cate("ST",["ST_t_top","ST_t_antitop","ST_tW_top","ST_tW_antitop"])
    VV = cate("VV",["WW2L2Nu","WZ2Q2L","WZ3LNu","ZZ2Q2L","ZZ2L2Nu","ZZ4L"])
    TT = cate("TT",["TTTo2L2Nu","TTToHadronic","TTToSemiLeptonic"])
    ZTT = cate("ZTT",["DYJetsToLL_M-50"])
    data_obs = cate("data_obs",["dataA","dataB","dataC","dataD"])
    weight = "xsweight*SFweight*Acoweight*npvsweight*nPUtrkweight*nHStrkweight"
    
    cutiso = cut+" && is_isolated"
    cutisoname = cutname + "_iso"
    
    cutnoniso = cut+" && !is_isolated"
    cutnonisoname = cutname + "_noniso"
    
    histoSTiso = gethisto_cate(ST,cutiso,cutisoname,weight,variable)
    histoVViso = gethisto_cate(VV,cutiso,cutisoname,weight,variable)
    histoTTiso = gethisto_cate(TT,cutiso,cutisoname,weight,variable)
    histoZTTiso = gethisto_cate(ZTT,cutiso,cutisoname,weight,variable)
    histodataiso = gethisto_catedata(data_obs,cutiso,cutisoname,variable)
    histoiso = histodataiso.Clone("h_{}_{}_{}".format(variable.name,cutname,"dataiso_sub"))
    histoiso.Add(histoSTiso,-1)
    histoiso.Add(histoVViso,-1)
    histoiso.Add(histoTTiso,-1)
    histoiso.Add(histoZTTiso,-1)
    
 
    histoSTnoniso = gethisto_cate(ST,cutnoniso,cutnonisoname,weight,variable)
    histoVVnoniso = gethisto_cate(VV,cutnoniso,cutnonisoname,weight,variable)
    histoTTnoniso = gethisto_cate(TT,cutnoniso,cutnonisoname,weight,variable)
    histoZTTnoniso = gethisto_cate(ZTT,cutnoniso,cutnonisoname,weight,variable)
    histodatanoniso = gethisto_catedata(data_obs,cutnoniso,cutnonisoname,variable)

    histononiso = histodatanoniso.Clone("h_{}_{}_{}".format(variable.name,cutname,"datanoniso_sub"))
    histononiso.Add(histoSTnoniso,-1)
    histononiso.Add(histoVVnoniso,-1)
    histononiso.Add(histoTTnoniso,-1)
    histononiso.Add(histoZTTnoniso,-1)
    
    for i in (1,histoiso.GetNbinsX()+1):
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
        for i in range(1,hFR.GetNbinsX()+1):
            hFR.SetBinContent(i,hFR.GetBinContent(i)/ratio)
            hFR.SetBinError(i,hFR.GetBinError(i)/ratio)
    
    return histoSTiso,histoVViso,histoTTiso,histoZTTiso,histoSTnoniso,histoVVnoniso,histoTTnoniso,histoZTTnoniso,histodataiso,histodatanoniso,histoiso,histononiso,hFR


tau2pt = variable("tau2pt","#sub_tau_{h} p_{T}",int(11),np.array([30,35,40,45,50,60,80,100,150,200,250,300],dtype=float))
ntrk = variable("nTrk","N_{tracks}",int(21),np.array([-0.5,0.5,1.5,4.5,9.5,14.5,19.5,24.5,29.5,34.5,39.5,44.5,49.5,54.5,59.5,64.5,69.5,74.5,79.5,84.5,89.5,94.5,99.5],dtype=float))
Acopl = variable("Acopl","Acoplanarity",int(20),np.array([0,0.05,0.1,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1.00],dtype=float))

variablelist = [tau2pt, ntrk, Acopl]


fout = TFile("./FR_tautau.root","recreate")
for DM in [0,1,10,11]:
    for variable in variablelist:
        QCDcut = "!isOS"
        QCDcut = QCDcut+" && LepCand_DecayMode[tau2index]=={}".format(DM)
        QCDcutname = "QCD_DM{}".format(DM)
        histoQCDtuple = getFRhisto(QCDcut,QCDcutname,variable)
        fout.cd()
        for histoQCD in histoQCDtuple:
            histoQCD.Write()
fout.Close()