from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas,TH1F,TPaveText
from ROOT.RDF import TH1DModel
import numpy as np
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
time_start=timer.time()

ROOT.gInterpreter.AddIncludePath('./lib/')
ROOT.gInterpreter.Declare('#include "./lib/basic_sel.h"')
ROOT.gInterpreter.Declare('#include "./lib/GetPFtrk.h"')
ROOT.gInterpreter.Declare('#include "./lib/Correction.h"')
ROOT.gInterpreter.Declare('#include "./lib/ApplyFR.h"')
ROOT.gSystem.Load('./lib/RDFfunc.so')

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
    
    f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/mutau/RDF/{}.root".format(sample))
    t1 = f1.Get("Events")
    f2 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/mutau/RDF/{}_friend.root".format(sample))
    t2 = f2.Get("ntrktuple")
    t1.AddFriend(t2,"friend")
    df = RDataFrame(t1)
    hmodel = TH1DModel("h_{}_{}_{}".format(variable.name,cutname,sample),"",variable.nbins,variable.binning)
    histo = df.Define("totalweight",weight).Filter(cut).Histo1D(hmodel,variable.name,"totalweight").GetPtr()
    histo.Sumw2()
    return histo


def gethisto_cate(cate, cut, cutname, weight, variable):
    h = TH1F("h_{}_{}_{}".format(variable.name,cutname,cate.name),"",variable.nbins,variable.binning)
    for sample in cate.samplelist:
        histo = gethisto(sample,cut,cutname,weight,variable)
        h.Add(histo,1)
    return h

def gethisto_withFR(sample,cut,cutname,weight,variable):
    f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/mutau/RDF/{}.root".format(sample))
    t1 = f1.Get("Events")
    f2 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/mutau/RDF/{}_friend.root".format(sample))
    t2 = f2.Get("ntrktuple")
    t1.AddFriend(t2,"friend")
    df = RDataFrame(t1)
    hmodel = TH1DModel("h_{}_{}_{}".format(variable.name,cutname,sample),"",variable.nbins,variable.binning)
    df = df.Filter(cut).Define("totalweight",weight).Define("taudecaymode", "LepCand_DecayMode[tauindex]").Define("FR","GetFR_mutau(taudecaymode,mvis,mtrans,taupt,nTrk)").Define("plotweight","totalweight*FR")
    histo = df.Histo1D(hmodel,variable.name,"plotweight").GetPtr()
    histo.Sumw2()
    return histo

def gethisto_withFR_cate(cate,cut,cutname,weight,variable):
    h = TH1F("h_{}_{}_{}".format(variable.name,cutname,cate.name),"",variable.nbins,variable.binning)
    for sample in cate.samplelist:
        histo = gethisto_withFR(sample,cut,cutname,weight,variable)
        h.Add(histo,1)
    return h

def getallhisto(cut,cutname,variable):
    ST = cate("ST",["ST_t_top","ST_t_antitop","ST_tW_top","ST_tW_antitop"])
    VV = cate("VV",["WW2L2Nu","WZ2Q2L","WZ3LNu","ZZ2Q2L","ZZ2L2Nu","ZZ4L"])
    TT = cate("TT",["TTTo2L2Nu","TTToHadronic","TTToSemiLeptonic"])
    ZTT = cate("ZTT",["DYJetsToLL_M-50"])
    GGTT = cate("GGTT",["GGToTauTau"])
    data_obs = cate("data_obs",["dataA","dataB","dataC","dataD"])
    weight = "xsweight*SFweight*Acoweight*npvsweight*nPUtrkweight*nHStrkweight"
    
    cutiso = cut+" && isOS && is_isolated"
    cutisoname = cutname + "_iso"
    
    cutnoniso = cut+" && isOS && !is_isolated"
    cutnonisoname = cutname + "_noniso"
    
    hisST_noniso = gethisto_withFR_cate(ST,cutnoniso,cutnonisoname,weight,variable)
    hisVV_noniso = gethisto_withFR_cate(VV,cutnoniso,cutnonisoname,weight,variable)
    hisTT_noniso = gethisto_withFR_cate(TT,cutnoniso,cutnonisoname,weight,variable)
    hisZTT_noniso = gethisto_withFR_cate(ZTT,cutnoniso,cutnonisoname,weight,variable)
    data_noniso =  gethisto_withFR_cate(data_obs,cutnoniso,cutnonisoname,weight,variable)
    
    Fake = data_noniso.Clone("Fake")
    Fake.Add(hisST_noniso,-1)
    Fake.Add(hisVV_noniso,-1)
    Fake.Add(hisTT_noniso,-1)
    Fake.Add(hisZTT_noniso,-1)
    
    hisST_iso = gethisto_cate(ST,cutiso,cutisoname,weight,variable)
    hisVV_iso = gethisto_cate(VV,cutiso,cutisoname,weight,variable)
    hisTT_iso = gethisto_cate(TT,cutiso,cutisoname,weight,variable)
    hisZTT_iso = gethisto_cate(ZTT,cutiso,cutisoname,weight,variable)
    hisGGTT_iso = gethisto_cate(GGTT,cutiso,cutisoname,weight,variable)
    data_iso =  gethisto_cate(data_obs,cutiso,cutisoname,weight,variable)
    
    hisST_iso.SetName("ST")
    hisVV_iso.SetName("VV")
    hisTT_iso.SetName("TT")
    hisZTT_iso.SetName("ZTT")
    hisGGTT_iso.SetName("GGTT")
    data_iso.SetName("data_obs")
    for i in range(1,Fake.GetNbinsX()+1):
        if Fake.GetBinContent(i)<=0:
            Fake.SetBinContent(i,0)
            Fake.SetBinError(i,0)
        if hisST_iso.GetBinContent(i)<=0:
            hisST_iso.SetBinContent(i,0)
            hisST_iso.SetBinError(i,0) 
        if hisVV_iso.GetBinContent(i)<=0:
            hisVV_iso.SetBinContent(i,0)
            hisVV_iso.SetBinError(i,0) 
        if hisTT_iso.GetBinContent(i)<=0:
            hisTT_iso.SetBinContent(i,0)
            hisTT_iso.SetBinError(i,0) 
        if hisZTT_iso.GetBinContent(i)<=0:
            hisZTT_iso.SetBinContent(i,0)
            hisZTT_iso.SetBinError(i,0) 
        if hisGGTT_iso.GetBinContent(i)<=0:
            hisGGTT_iso.SetBinContent(i,0)
            hisGGTT_iso.SetBinError(i,0) 
    
    return hisST_iso,hisVV_iso,hisTT_iso, hisZTT_iso,hisGGTT_iso,Fake,data_iso
    

mvis = variable("mvis","m_{vis}",int(8),np.array([40,55,70,85,100,150,200,350,500],dtype=float)) 

fout = TFile("./Taug2_mutau_2018.root","recreate")

fout.mkdir("mt_0")
fout.mkdir("mt_1")


mt_0cut = "(nTrk==0) && (Acopl<0.02)"
mt_1cut = "(nTrk==1) && (Acopl<0.02)"

mt_0_histotuple = getallhisto(mt_0cut,"mt_0",mvis)
fout.cd("mt_0")
for histo in mt_0_histotuple:
    histo.Write()
mt_1_histotuple = getallhisto(mt_1cut,"mt_1",mvis)
fout.cd("mt_1")
for histo in mt_1_histotuple:
    histo.Write()
fout.Close()

    


