from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas,TH1F,TPaveText,TH2F
from ROOT.RDF import TH1DModel,TH2DModel
import numpy as np
import sys
from math import cos,sin,sqrt,pi,pow
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
        
        
def gethisto(sample,cut,cutname,weight,variable1,variable2):
    
    f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/mutau/RDF/{}.root".format(sample))
    t1 = f1.Get("Events")
    f2 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/mutau/RDF/{}_friend.root".format(sample))
    t2 = f2.Get("ntrktuple")
    t1.AddFriend(t2,"friend")
    df = RDataFrame(t1)
    hmodel = TH2DModel("h_{}_{}_{}_{}".format(variable1.name,variable2.name,cutname,sample),"",variable1.nbins,variable1.binning,variable2.nbins,variable2.binning)
    histo = df.Define("totalweight",weight).Filter(cut).Histo2D(hmodel,variable1.name,variable2.name,"totalweight").GetPtr()
    histo.Sumw2()
    return histo

def gethistodata(sample,cut,cutname,variable1,variable2):
    
    f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/mutau/RDF/{}.root".format(sample))
    t1 = f1.Get("Events")
    f2 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/mutau/RDF/{}_friend.root".format(sample))
    t2 = f2.Get("ntrktuple")
    t1.AddFriend(t2,"friend")
    df = RDataFrame(t1)
    hmodel = TH2DModel("h_{}_{}_{}_{}".format(variable1.name,variable2.name,cutname,sample),"",variable1.nbins,variable1.binning,variable2.nbins,variable2.binning)
    histo = df.Filter(cut).Histo2D(hmodel,variable1.name,variable2.name).GetPtr()
    histo.Sumw2()
    return histo


def gethisto_cate(cate, cut, cutname, weight, variable1,variable2):
    h = TH2F("h_{}_{}_{}_{}".format(variable1.name,variable2.name,cutname,cate),"",variable1.nbins,variable1.binning,variable2.nbins,variable2.binning)
    for sample in cate.samplelist:
        histo = gethisto(sample,cut,cutname,weight,variable1,variable2)
        h.Add(histo,1)
    return h
        
def gethisto_catedata(cate, cut, cutname, variable1,variable2):
    h = TH2F("h_{}_{}_{}_{}".format(variable1.name,variable2.name,cutname,cate),"",variable1.nbins,variable1.binning,variable2.nbins,variable2.binning)
    for sample in cate.samplelist:
        histo = gethistodata(sample,cut,cutname,variable1,variable2)
        h.Add(histo,1)
    return h

def getWFRhisto(cut,cutname,variable1,variable2):
    ST = cate("ST",["ST_t_top","ST_t_antitop","ST_tW_top","ST_tW_antitop"])
    VV = cate("VV",["WW2L2Nu","WZ2Q2L","WZ3LNu","ZZ2Q2L","ZZ2L2Nu","ZZ4L"])
    TT = cate("TT",["TTTo2L2Nu","TTToHadronic","TTToSemiLeptonic"])
    ZTT = cate("ZTT",["DYJetsToLL_M-50"])
    W = cate("W",["WJets","W1Jets","W2Jets","W3Jets","W4Jets"])
    data_obs = cate("data_obs",["dataA","dataB","dataC","dataD"])
    weight = "xsweight*SFweight*Acoweight*npvsweight*nPUtrkweight*nHStrkweight"
    
    cutOS = cut + "&& isOS && is_isolated"
    cutSS = cut + "&& (!isOS) && is_isolated"
    cutOSname = cutname +"OS_iso"
    cutSSname = cutname + "SS_iso"
    
    histoSTSS = gethisto_cate(ST,cutSS,cutSSname,weight,variable1,variable2)
    histoVVSS = gethisto_cate(VV,cutSS,cutSSname,weight,variable1,variable2)
    histoTTSS = gethisto_cate(TT,cutSS,cutSSname,weight,variable1,variable2)
    histoZTTSS = gethisto_cate(ZTT,cutSS,cutSSname,weight,variable1,variable2)
    histoWSS = gethisto_cate(W,cutSS,cutSSname,weight,variable1,variable2)
    histodataSS = gethisto_catedata(data_obs,cutSS,cutSSname,variable1,variable2)
    histoSS= histodataSS.Clone("h_{}_{}_{}_{}".format(variable1.name,variable2.name,cutSSname,"QCD"))
    histoSS.Add(histoSTSS,-1)
    histoSS.Add(histoVVSS,-1)
    histoSS.Add(histoTTSS,-1)
    histoSS.Add(histoZTTSS,-1)
    histoSS.Add(histoWSS,-1)
    
    histoWOS = gethisto_cate(W,cutOS,cutOSname,weight,variable1,variable2)
    

    hFR = histoWOS.Clone("hWFR_{}_{}_{}".format(variable1.name,variable2.name,cutname))
    #hFR.Divide(histononiso)
    deno = histoSS.Clone("hWQCD_{}_{}_{}".format(variable1.name,variable2.name,cutname))
    deno.Add(histoWOS)
    hFR.Divide(deno)
    
    return histoSTSS,histoVVSS,histoTTSS,histoZTTSS,histoWSS,histodataSS,histoSS,histoWOS,hFR

mvis = variable("mvis","mvis",int(3),np.array([0,25,50,75],dtype=float))
mtranse = variable("mtrans","mtrans",int(3),np.array([50,100,150,200,250,300],dtype=float))


fout = TFile("./FRW_mutau.root","recreate")
for DM in [0,1,10,11]:
    cut = "LepCand_DecayMode[tauindex]=={}".format(DM)
    cutname = "DM{}".format(DM)
    histotuple = getWFRhisto(cut,cutname,mvis,mtranse)
    fout.cd()
    for histo in histotuple:
        histo.Write()
fout.Close()





