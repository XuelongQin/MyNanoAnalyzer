from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas,TH1F,TPaveText,TH2F
from ROOT.RDF import TH1DModel, TH2DModel
import numpy as np
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
time_start=timer.time()
import sys
sys.path.append("..")

ROOT.gInterpreter.AddIncludePath('../lib/')
ROOT.gInterpreter.Declare('#include "../lib/ApplyFR.h"')
ROOT.gInterpreter.Declare('#include "../lib/Sys.h"')
ROOT.gSystem.Load('../lib/RDFfunc.so')


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
        
        

def gethisto(sample,cut,cutname,weight,variable,channel):
    
    #f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/{}/RDF/{}.root".format(channel,sample))
    #t1 = f1.Get("Events")
    print ("channel ", channel, " sample ", sample)
    f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/{}/RDF/{}.root".format(channel,sample))
    t1 = f1.Get("Events")
    #t1.AddFriend(t2,"friend")
    df = RDataFrame(t1)
    hmodel = TH1DModel("h_{}_{}_{}".format(variable.name,cutname,sample),"",variable.nbins,variable.binning)
    if channel=="mutau":
        histo = df.Redefine("taupt","my_tau.Pt()").Redefine("mvis","(my_mu + my_tau).M()").Define("totalweight",weight).Filter(cut).Histo1D(hmodel,variable.name,"totalweight").GetPtr()
    else:
        histo = df.Redefine("tau1pt","my_tau1.Pt()").Redefine("tau2pt","my_tau2.Pt()").Redefine("mvis","(my_tau1 + my_tau2).M()").Define("totalweight",weight).Filter(cut).Histo1D(hmodel,variable.name,"totalweight").GetPtr()
    histo.Sumw2()
    return histo

def gethisto_cate(cate, cut, cutname, weight, variable,channel):
    h = TH1F("h_{}_{}_{}".format(variable.name,cutname,cate.name),"",variable.nbins,variable.binning)
    for sample in cate.samplelist:
        histo = gethisto(sample,cut,cutname,weight,variable,channel)
        h.Add(histo,1)
    return h


def gethisto_sysweight(sample,cut,cutname,weight,variable,channel,func):
    
    #f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/{}/RDF/{}.root".format(channel,sample))
    #t1 = f1.Get("Events")
    print ("channel ", channel, " sample ", sample)
    f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/{}/RDF/{}.root".format(channel,sample))
    t1 = f1.Get("Events")
    #t1.AddFriend(t2,"friend")
    df = RDataFrame(t1)
    hmodel = TH1DModel("h_{}_{}_{}".format(variable.name,cutname,sample),"",variable.nbins,variable.binning)
    histo = df.Redefine("taupt","my_tau.Pt()").Redefine("mvis","(my_mu + my_tau).M()").Define("weight2",func).Define("totalweight","{}*weight2".format(weight)).Filter(cut).Histo1D(hmodel,variable.name,"totalweight").GetPtr()
    histo.Sumw2()
    return histo

def gethisto_cate_sysweight(cate, cut, cutname, weight, variable,channel, func):
    h = TH1F("h_{}_{}_{}".format(variable.name,cutname,cate.name),"",variable.nbins,variable.binning)
    for sample in cate.samplelist:
        histo = gethisto_sysweight(sample,cut,cutname,weight,variable,channel, func)
        h.Add(histo,1)
    return h


def gethisto_sysnewtaupt(sample,cut,cutname,weight,variable,channel,func):
    
    #f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/{}/RDF/{}.root".format(channel,sample))
    #t1 = f1.Get("Events")
    print ("channel ", channel, " sample ", sample)
    f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/{}/RDF/{}.root".format(channel,sample))
    t1 = f1.Get("Events")
    #t1.AddFriend(t2,"friend")
    df = RDataFrame(t1)
    hmodel = TH1DModel("h_{}_{}_{}".format(variable.name,cutname,sample),"",variable.nbins,variable.binning)
    histo = df.Redefine("my_tau",func).Redefine("taupt","my_tau.Pt()").Redefine("mvis","(my_mu + my_tau).M()").Define("totalweight",weight).Filter(cut).Histo1D(hmodel,variable.name,"totalweight").GetPtr()
    histo.Sumw2()
    return histo

def gethisto_cate_sysnewtaupt(cate, cut, cutname, weight, variable,channel, func):
    h = TH1F("h_{}_{}_{}".format(variable.name,cutname,cate.name),"",variable.nbins,variable.binning)
    for sample in cate.samplelist:
        histo = gethisto_sysnewtaupt(sample,cut,cutname,weight,variable,channel, func)
        h.Add(histo,1)
    return h


def gethisto2D(sample,cut,cutname,weight,variable1,variable2,channel):
    
    #f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/{}/RDF/{}.root".format(channel,sample))
    #t1 = f1.Get("Events")
    f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/{}/RDF/{}.root".format(channel,sample))
    t1 = f1.Get("Events")
    #t1.AddFriend(t2,"friend")
    df = RDataFrame(t1)
    hmodel = TH2DModel("h_{}_{}_{}_{}".format(variable1.name,variable2.name,cutname,sample),"",variable1.nbins,variable1.binning,variable2.nbins,variable2.binning)
    histo = df.Define("totalweight",weight).Filter(cut).Histo2D(hmodel,variable1.name,variable2.name,"totalweight").GetPtr()
    histo.Sumw2()
    return histo

def gethisto2D_cate(cate, cut, cutname, weight, variable1,variable2,channel):
    h = TH2F("h_{}_{}_{}_{}".format(variable1.name,variable2.name,cutname,cate.name),"",variable1.nbins,variable1.binning,variable2.nbins,variable2.binning)
    for sample in cate.samplelist:
        histo = gethisto2D(sample,cut,cutname,weight,variable1,variable2,channel)
        h.Add(histo,1)
    return h

def gethisto_withFR(sample,cut,cutname,weight,variable,channel):
    #f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/{}/RDF/{}.root".format(channel,sample))
    #t1 = f1.Get("Events")
    f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/{}/RDF/{}.root".format(channel,sample))
    print ("f1",sample)
    t1 = f1.Get("Events")
    print ("t1",sample)
    
    #t1.AddFriend(t2,"friend")
    df = RDataFrame(t1)
    hmodel = TH1DModel("h_{}_{}_{}".format(variable.name,cutname,sample),"",variable.nbins,variable.binning)
    if channel =="mutau":
        df = df.Filter(cut).Define("totalweight",weight).Define("taudecaymode", "LepCand_DecayMode[tauindex]").Define("FR","GetFR_{}(taudecaymode,mvis,mtrans,taupt,nTrk)".format(channel)).Define("plotweight","totalweight*FR")
    if channel =="tautau":
        df = df.Filter(cut).Define("totalweight",weight).Define("taudecaymode", "LepCand_DecayMode[tau2index]").Define("FR","GetFR_{}(LepCand_DecayMode[tau2index],tau2pt,nTrk)".format(channel)).Define("plotweight","totalweight*FR")
    histo = df.Histo1D(hmodel,variable.name,"plotweight").GetPtr()
    print ("histo",histo.GetBinContent(1))
    histo.Sumw2()
    return histo

def gethisto_withFR_cate(cate,cut,cutname,weight,variable,channel):
    h = TH1F("h_{}_{}_{}".format(variable.name,cutname,cate.name),"",variable.nbins,variable.binning)
    for sample in cate.samplelist:
        histo = gethisto_withFR(sample,cut,cutname,weight,variable,channel)
        print (sample)
        h.Add(histo,1)
    return h


def getallhisto_tautau(cut,cutname,variable):
    channel = "tautau"
    ST = cate("ST",["ST_t_top","ST_t_antitop","ST_tW_top","ST_tW_antitop"])
    VV = cate("VV",["WW2L2Nu","WZ2Q2L","WZ3LNu","ZZ2Q2L","ZZ2L2Nu","ZZ4L"])
    TT = cate("TT",["TTTo2L2Nu","TTToHadronic","TTToSemiLeptonic"])
    ZTT = cate("ZTT",["DYJetsToLL_M-50"])
    GGTT = cate("GGTT",["GGToTauTau"])
    data_obs = cate("data_obs",["dataA","dataB","dataC","dataD"])
    weight = "xsweight*SFweight*Acoweight*npvsweight*nPUtrkweight*nHStrkweight"
    
    cutisodata = cut+" && isOS && is_isolated"
    cutnonisodata = cut+" && isOS && !is_isolated"
    
    cutisodataname = cutname+"_iso_data"
    cutnonisodataname = cutname+"_noniso_data"
    
    cutisoMC = cut+" && isOS && is_isolated  && LepCand_gen[tau2index]!=0"
    cutnonisoMC = cut+" && isOS && !is_isolated  && LepCand_gen[tau2index]!=0"
    
    cutisoMCname = cutname+"_iso_realMC"
    cutnonisoMCname = cutname+"_noniso_realMC"

    hisST_noniso = gethisto_withFR_cate(ST,cutnonisoMC,cutnonisoMCname,weight,variable,channel)

    hisVV_noniso = gethisto_withFR_cate(VV,cutnonisoMC,cutnonisoMCname,weight,variable,channel)

    hisTT_noniso = gethisto_withFR_cate(TT,cutnonisoMC,cutnonisoMCname,weight,variable,channel)

    hisZTT_noniso = gethisto_withFR_cate(ZTT,cutnonisoMC,cutnonisoMCname,weight,variable,channel)

    data_noniso =  gethisto_withFR_cate(data_obs,cutnonisodata,cutnonisodataname,"1",variable,channel)
    print("data")
    Fake = data_noniso.Clone("Fake")
    Fake.Add(hisST_noniso,-1)
    Fake.Add(hisVV_noniso,-1)
    Fake.Add(hisTT_noniso,-1)
    Fake.Add(hisZTT_noniso,-1)
    
    hisST_iso = gethisto_cate(ST,cutisoMC,cutisoMCname,weight,variable,channel)
    hisVV_iso = gethisto_cate(VV,cutisoMC,cutisoMCname,weight,variable,channel)
    hisTT_iso = gethisto_cate(TT,cutisoMC,cutisoMCname,weight,variable,channel)
    hisZTT_iso = gethisto_cate(ZTT,cutisoMC,cutisoMCname,weight,variable,channel)
    hisGGTT_iso = gethisto_cate(GGTT,cutisoMC,cutisoMCname,weight,variable,channel)
    data_iso =  gethisto_cate(data_obs,cutisodata,cutisodataname,"1",variable,channel)
    
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


def getallhisto_mutau(cut,cutname,variable):
    channel="mutau"
    ST = cate("ST",["ST_t_top","ST_t_antitop","ST_tW_top","ST_tW_antitop"])
    VV = cate("VV",["WW2L2Nu","WZ2Q2L","WZ3LNu","ZZ2Q2L","ZZ2L2Nu","ZZ4L"])
    TT = cate("TT",["TTTo2L2Nu","TTToHadronic","TTToSemiLeptonic"])
    ZTT = cate("ZTT",["DYJetsToLL_M-50"])
    GGTT = cate("GGTT",["GGToTauTau"])
    data_obs = cate("data_obs",["dataA","dataB","dataC","dataD"])
    weight = "xsweight*SFweight*Acoweight*npvsweight*nPUtrkweight*nHStrkweight"
    
    
    cutisodata = cut+" && isOS && is_isolated"
    cutnonisodata = cut+" && isOS && !is_isolated"
    
    cutisodataname = cutname+"_iso_data"
    cutnonisodataname = cutname+"_noniso_data"
    
    cutisoMC = cut+" && isOS && is_isolated  && LepCand_gen[tauindex]!=0"
    cutnonisoMC = cut+" && isOS && !is_isolated  && LepCand_gen[tauindex]!=0"
    
    cutisoMCname = cutname+"_iso_realMC"
    cutnonisoMCname = cutname+"_noniso_realMC"
    
    
    hisST_noniso = gethisto_withFR_cate(ST,cutnonisoMC,cutnonisoMCname,weight,variable,channel)

    hisVV_noniso = gethisto_withFR_cate(VV,cutnonisoMC,cutnonisoMCname,weight,variable,channel)

    hisTT_noniso = gethisto_withFR_cate(TT,cutnonisoMC,cutnonisoMCname,weight,variable,channel)

    hisZTT_noniso = gethisto_withFR_cate(ZTT,cutnonisoMC+"&& LepCand_gen[tauindex]==5",cutnonisoMCname+"_ZTT",weight,variable,channel)
    hisZLL_noniso = gethisto_withFR_cate(ZTT,cutnonisoMC+"&& LepCand_gen[tauindex]!=5",cutnonisoMCname+"_ZLL",weight,variable,channel)

    data_noniso =  gethisto_withFR_cate(data_obs,cutnonisodata,cutnonisodataname,"1",variable,channel)
    print("data")
    Fake = data_noniso.Clone("Fake")
    Fake.Add(hisST_noniso,-1)
    Fake.Add(hisVV_noniso,-1)
    Fake.Add(hisTT_noniso,-1)
    Fake.Add(hisZTT_noniso,-1)
    Fake.Add(hisZLL_noniso,-1)
    
    hisST_iso = gethisto_cate(ST,cutisoMC,cutisoMCname,weight,variable,channel)
    hisVV_iso = gethisto_cate(VV,cutisoMC,cutisoMCname,weight,variable,channel)
    hisTT_iso = gethisto_cate(TT,cutisoMC,cutisoMCname,weight,variable,channel)
    hisZTT_iso = gethisto_cate(ZTT,cutisoMC+"&& LepCand_gen[tauindex]==5",cutisoMCname+"_ZTT",weight,variable,channel)
    hisZLL_iso = gethisto_cate(ZTT,cutisoMC+"&& LepCand_gen[tauindex]!=5",cutisoMCname+"_ZLL",weight,variable,channel)
    
    hisGGTT_iso = gethisto_cate(GGTT,cutisoMC,cutisoMCname,weight,variable,channel)
    data_iso =  gethisto_cate(data_obs,cutisodata,cutisodataname,"1",variable,channel)
    
    hisST_iso.SetName("ST")
    hisVV_iso.SetName("VV")
    hisTT_iso.SetName("TT")
    hisZTT_iso.SetName("ZTT")
    hisZLL_iso.SetName("ZLL")
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
        if hisZLL_iso.GetBinContent(i)<=0:
            hisZLL_iso.SetBinContent(i,0)
            hisZLL_iso.SetBinError(i,0) 
        if hisGGTT_iso.GetBinContent(i)<=0:
            hisGGTT_iso.SetBinContent(i,0)
            hisGGTT_iso.SetBinError(i,0) 
        
    
    return hisST_iso,hisVV_iso,hisTT_iso, hisZTT_iso,hisZLL_iso, hisGGTT_iso,Fake,data_iso



def getallhisto_mutau_relaxDY(cut,DYshapecut,cutname,variable):
    channel="mutau"
    ST = cate("ST",["ST_t_top","ST_t_antitop","ST_tW_top","ST_tW_antitop"])
    VV = cate("VV",["WW2L2Nu","WZ2Q2L","WZ3LNu","ZZ2Q2L","ZZ2L2Nu","ZZ4L"])
    TT = cate("TT",["TTTo2L2Nu","TTToHadronic","TTToSemiLeptonic"])
    ZTT = cate("ZTT",["DYJetsToLL_M-50"])
    GGTT = cate("GGTT",["GGToTauTau"])
    data_obs = cate("data_obs",["dataA","dataB","dataC","dataD"])
    weight = "xsweight*SFweight*Acoweight*npvsweight*nPUtrkweight*nHStrkweight"
    
    cutisodata = cut+" && isOS && is_isolated"
    cutnonisodata = cut+" && isOS && !is_isolated"
    
    cutisodataname = cutname+"_iso_data"
    cutnonisodataname = cutname+"_noniso_data"
    
    cutisoMC = cut+" && isOS && is_isolated  && LepCand_gen[tauindex]!=0"
    cutnonisoMC = cut+" && isOS && !is_isolated  && LepCand_gen[tauindex]!=0"
    
    cutisoMCname = cutname+"_iso_realMC"
    cutnonisoMCname = cutname+"_noniso_realMC"
    
    
    cutisoDYshape = DYshapecut+" && isOS && is_isolated  && LepCand_gen[tauindex]!=0"
    cutnonisoDYshape = DYshapecut+" && isOS && !is_isolated  && LepCand_gen[tauindex]!=0"
    
    cutisoDYshapename = cutname+"_iso_realDYshape"
    cutnonisoDYshapename = cutname+"_noniso_realDYshape"

    hisST_noniso = gethisto_withFR_cate(ST,cutnonisoMC,cutnonisoMCname,weight,variable,channel)

    hisVV_noniso = gethisto_withFR_cate(VV,cutnonisoMC,cutnonisoMCname,weight,variable,channel)

    hisTT_noniso = gethisto_withFR_cate(TT,cutnonisoMC,cutnonisoMCname,weight,variable,channel)

    hisZTT_noniso = gethisto_withFR_cate(ZTT,cutnonisoMC+"&& LepCand_gen[tauindex]==5",cutnonisoMCname+"_ZTT",weight,variable,channel)
    hisZLL_noniso = gethisto_withFR_cate(ZTT,cutnonisoMC+"&& LepCand_gen[tauindex]!=5",cutnonisoMCname+"_ZLL",weight,variable,channel)

    hisZTTshape_noniso = gethisto_withFR_cate(ZTT,cutnonisoDYshape+"&& LepCand_gen[tauindex]==5",cutnonisoDYshapename+"_ZTT",weight,variable,channel)
    hisZLLshape_noniso = gethisto_withFR_cate(ZTT,cutnonisoDYshape+"&& LepCand_gen[tauindex]!=5",cutnonisoDYshapename+"_ZLL",weight,variable,channel)

    SFnoniso_ZTT = hisZTT_noniso.Integral()/hisZTTshape_noniso.Integral()
    SFnoniso_ZLL = hisZLL_noniso.Integral()/hisZLLshape_noniso.Integral()
    
    hisZTT_noniso_relax = hisZTTshape_noniso.Clone()
    hisZTT_noniso_relax.Scale(SFnoniso_ZTT)
    hisZLL_noniso_relax = hisZLLshape_noniso.Clone()
    hisZLL_noniso_relax.Scale(SFnoniso_ZLL)
    
    data_noniso =  gethisto_withFR_cate(data_obs,cutnonisodata,cutnonisodataname,"1",variable,channel)
    
    print("data")
    Fake = data_noniso.Clone("Fake")
    Fake.Add(hisST_noniso,-1)
    Fake.Add(hisVV_noniso,-1)
    Fake.Add(hisTT_noniso,-1)
    Fake.Add(hisZTT_noniso_relax,-1)
    Fake.Add(hisZLL_noniso_relax,-1)
    
    hisST_iso = gethisto_cate(ST,cutisoMC,cutisoMCname,weight,variable,channel)
    hisVV_iso = gethisto_cate(VV,cutisoMC,cutisoMCname,weight,variable,channel)
    hisTT_iso = gethisto_cate(TT,cutisoMC,cutisoMCname,weight,variable,channel)
    
    hisZTT_iso = gethisto_cate(ZTT,cutisoMC+"&& LepCand_gen[tauindex]==5",cutisoMCname+"_ZTT",weight,variable,channel)
    hisZLL_iso = gethisto_cate(ZTT,cutisoMC+"&& LepCand_gen[tauindex]!=5",cutisoMCname+"_ZLL",weight,variable,channel)

    hisZTTshape_iso = gethisto_cate(ZTT,cutisoDYshape+"&& LepCand_gen[tauindex]==5",cutisoDYshapename+"_ZTT",weight,variable,channel)
    hisZLLshape_iso = gethisto_cate(ZTT,cutisoDYshape+"&& LepCand_gen[tauindex]!=5",cutisoDYshapename+"_ZLL",weight,variable,channel)

    SFiso_ZTT = hisZTT_iso.Integral()/hisZTTshape_iso.Integral()
    SFiso_ZLL = hisZLL_iso.Integral()/hisZLLshape_iso.Integral()
    
    hisZTT_iso_relax = hisZTTshape_iso.Clone()
    hisZTT_iso_relax.Scale(SFiso_ZTT)
    hisZLL_iso_relax = hisZLLshape_iso.Clone()
    hisZLL_iso_relax.Scale(SFiso_ZLL)
    hisGGTT_iso = gethisto_cate(GGTT,cutisoMC,cutisoMCname,weight,variable,channel)
    data_iso =  gethisto_cate(data_obs,cutisodata,cutisodataname,"1",variable,channel)
    
    hisST_iso.SetName("ST")
    hisVV_iso.SetName("VV")
    hisTT_iso.SetName("TT")
    hisZTT_iso_relax.SetName("ZTT")
    hisZLL_iso_relax.SetName("ZLL")
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
        if hisZLL_iso.GetBinContent(i)<=0:
            hisZLL_iso.SetBinContent(i,0)
            hisZLL_iso.SetBinError(i,0) 
        if hisGGTT_iso.GetBinContent(i)<=0:
            hisGGTT_iso.SetBinContent(i,0)
            hisGGTT_iso.SetBinError(i,0) 
        
    
    return hisST_iso,hisVV_iso,hisTT_iso, hisZTT_iso_relax,hisZLL_iso_relax, hisGGTT_iso,Fake,data_iso

def getallhisto_tautau_relaxDY(cut,DYshapecut,cutname,variable):
    channel="tautau"
    ST = cate("ST",["ST_t_top","ST_t_antitop","ST_tW_top","ST_tW_antitop"])
    VV = cate("VV",["WW2L2Nu","WZ2Q2L","WZ3LNu","ZZ2Q2L","ZZ2L2Nu","ZZ4L"])
    TT = cate("TT",["TTTo2L2Nu","TTToHadronic","TTToSemiLeptonic"])
    ZTT = cate("ZTT",["DYJetsToLL_M-50"])
    GGTT = cate("GGTT",["GGToTauTau"])
    data_obs = cate("data_obs",["dataA","dataB","dataC","dataD"])
    weight = "xsweight*SFweight*Acoweight*npvsweight*nPUtrkweight*nHStrkweight"
    
    cutisodata = cut+" && isOS && is_isolated"
    cutnonisodata = cut+" && isOS && !is_isolated"
    
    cutisodataname = cutname+"_iso_data"
    cutnonisodataname = cutname+"_noniso_data"
    
    cutisoMC = cut+" && isOS && is_isolated  && LepCand_gen[tau2index]!=0"
    cutnonisoMC = cut+" && isOS && !is_isolated  && LepCand_gen[tau2index]!=0"
    
    cutisoMCname = cutname+"_iso_realMC"
    cutnonisoMCname = cutname+"_noniso_realMC"
    
    
    cutisoDYshape = DYshapecut+" && isOS && is_isolated  && LepCand_gen[tau2index]!=0"
    cutnonisoDYshape = DYshapecut+" && isOS && !is_isolated  && LepCand_gen[tau2index]!=0"
    
    cutisoDYshapename = cutname+"_iso_realDYshape"
    cutnonisoDYshapename = cutname+"_noniso_realDYshape"

    hisST_noniso = gethisto_withFR_cate(ST,cutnonisoMC,cutnonisoMCname,weight,variable,channel)

    hisVV_noniso = gethisto_withFR_cate(VV,cutnonisoMC,cutnonisoMCname,weight,variable,channel)

    hisTT_noniso = gethisto_withFR_cate(TT,cutnonisoMC,cutnonisoMCname,weight,variable,channel)

    hisZTT_noniso = gethisto_withFR_cate(ZTT,cutnonisoMC,cutnonisoMCname,weight,variable,channel)

    hisZTTshape_noniso = gethisto_withFR_cate(ZTT,cutnonisoDYshape,cutnonisoDYshapename,weight,variable,channel)

    SFnoniso_ZTT = hisZTT_noniso.Integral()/hisZTTshape_noniso.Integral()
    
    hisZTT_noniso_relax = hisZTTshape_noniso.Clone()
    hisZTT_noniso_relax.Scale(SFnoniso_ZTT)
    
    data_noniso =  gethisto_withFR_cate(data_obs,cutnonisodata,cutnonisodataname,"1",variable,channel)
    
    print("data")
    Fake = data_noniso.Clone("Fake")
    Fake.Add(hisST_noniso,-1)
    Fake.Add(hisVV_noniso,-1)
    Fake.Add(hisTT_noniso,-1)
    Fake.Add(hisZTT_noniso_relax,-1)
    
    hisST_iso = gethisto_cate(ST,cutisoMC,cutisoMCname,weight,variable,channel)
    hisVV_iso = gethisto_cate(VV,cutisoMC,cutisoMCname,weight,variable,channel)
    hisTT_iso = gethisto_cate(TT,cutisoMC,cutisoMCname,weight,variable,channel)
    
    hisZTT_iso = gethisto_cate(ZTT,cutisoMC,cutisoMCname,weight,variable,channel)

    hisZTTshape_iso = gethisto_cate(ZTT,cutisoDYshape,cutisoDYshapename,weight,variable,channel)

    SFiso_ZTT = hisZTT_iso.Integral()/hisZTTshape_iso.Integral()
    
    hisZTT_iso_relax = hisZTTshape_iso.Clone()
    hisZTT_iso_relax.Scale(SFiso_ZTT)
    hisGGTT_iso = gethisto_cate(GGTT,cutisoMC,cutisoMCname,weight,variable,channel)
    data_iso =  gethisto_cate(data_obs,cutisodata,cutisodataname,"1",variable,channel)
    
    hisST_iso.SetName("ST")
    hisVV_iso.SetName("VV")
    hisTT_iso.SetName("TT")
    hisZTT_iso_relax.SetName("ZTT")
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
    return hisST_iso,hisVV_iso,hisTT_iso, hisZTT_iso_relax, hisGGTT_iso,Fake,data_iso


def getsyshisto_mutau(cut,DYshapecut,cutname,variable):
    weight = "xsweight*SFweight*Acoweight*npvsweight*nPUtrkweight*nHStrkweight"
    #uncertainty that only need to add an additional weight
    uncertainties_weight = ["_CMS_tauid_pt30to35_2018Down","_CMS_tauid_pt30to35_2018Up","_CMS_tauid_pt35to40_2018Down","_CMS_tauid_pt35to40_2018Up","_CMS_tauid_ptgt40_2018Down","_CMS_tauid_ptgt40_2018Up",\
        "_CMS_mutauFR_barrel_2018Down","_CMS_mutauFR_barrel_2018Up","_CMS_mutauFR_endcap_2018Down","_CMS_mutauFR_endcap_2018Up",]
    #uncertainty that will change taupt so that change mvis
    uncertainties_newtaupt = ["_CMS_taues_dm0_2018Down","_CMS_taues_dm0_2018Up","_CMS_taues_dm1_2018Down","_CMS_taues_dm1_2018Up","_CMS_taues_3prong_2018Down","_CMS_taues_3prong_2018Up",\
        "_CMS_mutauFES_dm0_2018Down","_CMS_mutauFES_dm0_2018Up","_CMS_mutauFES_dm1_2018Down","_CMS_mutauFES_dm1_2018Up" ]
    # function name of uncertainties_weight
    function_weight = ["Gettauidsysweight(taupt,30,35,false,LepCand_gen, LepCand_tauidMsf, LepCand_tauidMsf_up, LepCand_tauidMsf_down, tauindex)",\
        "Gettauidsysweight(taupt,30,35,true,LepCand_gen, LepCand_tauidMsf, LepCand_tauidMsf_up, LepCand_tauidMsf_down, tauindex)",\
        "Gettauidsysweight(taupt,35,40,false,LepCand_gen, LepCand_tauidMsf, LepCand_tauidMsf_up, LepCand_tauidMsf_down, tauindex)",\
        "Gettauidsysweight(taupt,35,40,true,LepCand_gen, LepCand_tauidMsf, LepCand_tauidMsf_up, LepCand_tauidMsf_down, tauindex)",\
        "Gettauidsysweight(taupt,40,40,false,LepCand_gen, LepCand_tauidMsf, LepCand_tauidMsf_up, LepCand_tauidMsf_down, tauindex)",\
        "Gettauidsysweight(taupt,40,40,true,LepCand_gen, LepCand_tauidMsf, LepCand_tauidMsf_up, LepCand_tauidMsf_down, tauindex)",\
        "Gettauantimusysweight(false, true,LepCand_gen, LepCand_antimusf, LepCand_antimusf_up, LepCand_antimusf_down, tauindex, taueta)",\
        "Gettauantimusysweight(true, true,LepCand_gen, LepCand_antimusf, LepCand_antimusf_up, LepCand_antimusf_down, tauindex, taueta)",\
        "Gettauantimusysweight(false, false,LepCand_gen, LepCand_antimusf, LepCand_antimusf_up, LepCand_antimusf_down, tauindex, taueta)",\
        "Gettauantimusysweight(true, false,LepCand_gen, LepCand_antimusf, LepCand_antimusf_up, LepCand_antimusf_down, tauindex, taueta)"\
        ]
    
    function_newtaupt = ["Gettauessys(false, LepCand_DecayMode, LepCand_gen, LepCand_taues, LepCand_taues_down, LepCand_taues_up, tauindex, my_tau, 0)",\
        "Gettauessys(true, LepCand_DecayMode, LepCand_gen, LepCand_taues, LepCand_taues_down, LepCand_taues_up, tauindex, my_tau, 0)",\
        "Gettauessys(false, LepCand_DecayMode, LepCand_gen, LepCand_taues, LepCand_taues_down, LepCand_taues_up, tauindex, my_tau, 1)",\
        "Gettauessys(true, LepCand_DecayMode, LepCand_gen, LepCand_taues, LepCand_taues_down, LepCand_taues_up, tauindex, my_tau, 1)",\
        "Gettauessys(false, LepCand_DecayMode, LepCand_gen, LepCand_taues, LepCand_taues_down, LepCand_taues_up, tauindex, my_tau, 1011)",\
        "Gettauessys(true, LepCand_DecayMode, LepCand_gen, LepCand_taues, LepCand_taues_down, LepCand_taues_up, tauindex, my_tau, 1011)",\
        "Gettaufessys(false, LepCand_DecayMode, LepCand_gen, LepCand_fes, LepCand_fes_down,  LepCand_fes_up, tauindex, my_tau, 0)",\
        "Gettaufessys(true, LepCand_DecayMode, LepCand_gen, LepCand_fes, LepCand_fes_down,  LepCand_fes_up, tauindex, my_tau, 0)",\
        "Gettaufessys(false, LepCand_DecayMode, LepCand_gen, LepCand_fes, LepCand_fes_down,  LepCand_fes_up, tauindex, my_tau, 1)",\
        "Gettaufessys(true, LepCand_DecayMode, LepCand_gen, LepCand_fes, LepCand_fes_down,  LepCand_fes_up, tauindex, my_tau, 1)"\
        ]
    
    channel="mutau"
    ST = cate("ST",["ST_t_top","ST_t_antitop","ST_tW_top","ST_tW_antitop"])
    VV = cate("VV",["WW2L2Nu","WZ2Q2L","WZ3LNu","ZZ2Q2L","ZZ2L2Nu","ZZ4L"])
    TT = cate("TT",["TTTo2L2Nu","TTToHadronic","TTToSemiLeptonic"])
    ZTT = cate("ZTT",["DYJetsToLL_M-50"])
    GGTT = cate("GGTT",["GGToTauTau"])
    
    SThisto = []
    VVhisto = []
    TThisto = []
    ZTThisto = []
    ZLLhisto = []
    GGTThisto = []
    
    cutisoMC = cut+" && isOS && is_isolated  && LepCand_gen[tauindex]!=0"
    cutnonisoMC = cut+" && isOS && !is_isolated  && LepCand_gen[tauindex]!=0"
    
    cutisoMCname = cutname+"_iso_realMC"
    cutnonisoMCname = cutname+"_noniso_realMC"
    
    
    cutisoDYshape = DYshapecut+" && isOS && is_isolated  && LepCand_gen[tauindex]!=0"
    cutnonisoDYshape = DYshapecut+" && isOS && !is_isolated  && LepCand_gen[tauindex]!=0"
    
    cutisoDYshapename = cutname+"_iso_realDYshape"
    cutnonisoDYshapename = cutname+"_noniso_realDYshape"
    
    for i in range(len(function_weight)):
    #for i in range(4,5):
        print ("begin to get syshisto ", uncertainties_weight[i])
        print ("func : ", function_weight[i])
        func  = function_weight[i]
        cutisoMCname = cutisoMCname + uncertainties_weight[i]
        cutisoDYshapename = cutisoDYshapename + uncertainties_weight[i]
        #hisZTTshape_iso = gethisto_cate_sysweight(ZTT,cutisoDYshape+"&& LepCand_gen[tauindex]==5",cutisoDYshapename+"_ZTT",weight,variable,channel,func)
        hisST_iso = gethisto_cate_sysweight(ST,cutisoMC,cutisoMCname,weight,variable,channel,func)
        hisVV_iso = gethisto_cate_sysweight(VV,cutisoMC,cutisoMCname,weight,variable,channel,func)
        hisTT_iso = gethisto_cate_sysweight(TT,cutisoMC,cutisoMCname,weight,variable,channel,func)
        
        hisZTT_iso = gethisto_cate_sysweight(ZTT,cutisoMC+"&& LepCand_gen[tauindex]==5",cutisoMCname+"_ZTT",weight,variable,channel,func)
        hisZLL_iso = gethisto_cate_sysweight(ZTT,cutisoMC+"&& LepCand_gen[tauindex]!=5",cutisoMCname+"_ZLL",weight,variable,channel,func)

        hisZTTshape_iso = gethisto_cate_sysweight(ZTT,cutisoDYshape+"&& LepCand_gen[tauindex]==5",cutisoDYshapename+"_ZTT",weight,variable,channel,func)
        hisZLLshape_iso = gethisto_cate_sysweight(ZTT,cutisoDYshape+"&& LepCand_gen[tauindex]!=5",cutisoDYshapename+"_ZLL",weight,variable,channel,func)

        SFiso_ZTT = hisZTT_iso.Integral()/hisZTTshape_iso.Integral()
        SFiso_ZLL = hisZLL_iso.Integral()/hisZLLshape_iso.Integral()
        
        hisZTT_iso_relax = hisZTTshape_iso.Clone()
        hisZTT_iso_relax.Scale(SFiso_ZTT)
        hisZLL_iso_relax = hisZLLshape_iso.Clone()
        hisZLL_iso_relax.Scale(SFiso_ZLL)
        
        hisGGTT_iso = gethisto_cate_sysweight(GGTT,cutisoMC,cutisoMCname,weight,variable,channel,func)

        hisST_iso.SetName("ST{}".format(uncertainties_weight[i]))
        hisVV_iso.SetName("VV{}".format(uncertainties_weight[i]))
        hisTT_iso.SetName("TT{}".format(uncertainties_weight[i]))
        hisZTT_iso_relax.SetName("ZTT{}".format(uncertainties_weight[i]))
        hisZLL_iso_relax.SetName("ZLL{}".format(uncertainties_weight[i]))
        hisGGTT_iso.SetName("GGTT{}".format(uncertainties_weight[i]))
        
        SThisto.append(hisST_iso)
        VVhisto.append(hisVV_iso)
        TThisto.append(hisTT_iso)
        ZTThisto.append(hisZTT_iso_relax)
        ZLLhisto.append(hisZLL_iso_relax)
        GGTThisto.append(hisGGTT_iso)
    #sys.exit(0)
    for i in range(len(function_newtaupt)):
        print ("begin to get syshisto ", uncertainties_newtaupt[i])
        print ("func : ", function_newtaupt[i])
        func  = function_newtaupt[i]
        cutisoMCname = cutisoMCname + uncertainties_newtaupt[i]
        cutisoDYshapename = cutisoDYshapename + uncertainties_newtaupt[i]
        hisST_iso = gethisto_cate_sysnewtaupt(ST,cutisoMC,cutisoMCname,weight,variable,channel,func)
        hisVV_iso = gethisto_cate_sysnewtaupt(VV,cutisoMC,cutisoMCname,weight,variable,channel,func)
        hisTT_iso = gethisto_cate_sysnewtaupt(TT,cutisoMC,cutisoMCname,weight,variable,channel,func)
        
        hisZTT_iso = gethisto_cate_sysnewtaupt(ZTT,cutisoMC+"&& LepCand_gen[tauindex]==5",cutisoMCname+"_ZTT",weight,variable,channel,func)
        hisZLL_iso = gethisto_cate_sysnewtaupt(ZTT,cutisoMC+"&& LepCand_gen[tauindex]!=5",cutisoMCname+"_ZLL",weight,variable,channel,func)

        hisZTTshape_iso = gethisto_cate_sysnewtaupt(ZTT,cutisoDYshape+"&& LepCand_gen[tauindex]==5",cutisoDYshapename+"_ZTT",weight,variable,channel,func)
        hisZLLshape_iso = gethisto_cate_sysnewtaupt(ZTT,cutisoDYshape+"&& LepCand_gen[tauindex]!=5",cutisoDYshapename+"_ZLL",weight,variable,channel,func)

        SFiso_ZTT = hisZTT_iso.Integral()/hisZTTshape_iso.Integral()
        SFiso_ZLL = hisZLL_iso.Integral()/hisZLLshape_iso.Integral()
        
        hisZTT_iso_relax = hisZTTshape_iso.Clone()
        hisZTT_iso_relax.Scale(SFiso_ZTT)
        hisZLL_iso_relax = hisZLLshape_iso.Clone()
        hisZLL_iso_relax.Scale(SFiso_ZLL)
        
        hisGGTT_iso = gethisto_cate_sysnewtaupt(GGTT,cutisoMC,cutisoMCname,weight,variable,channel,func)

        hisST_iso.SetName("ST{}".format(uncertainties_newtaupt[i]))
        hisVV_iso.SetName("VV{}".format(uncertainties_newtaupt[i]))
        hisTT_iso.SetName("TT{}".format(uncertainties_newtaupt[i]))
        hisZTT_iso_relax.SetName("ZTT{}".format(uncertainties_newtaupt[i]))
        hisZLL_iso_relax.SetName("ZLL{}".format(uncertainties_newtaupt[i]))
        hisGGTT_iso.SetName("GGTT{}".format(uncertainties_newtaupt[i]))
        
        SThisto.append(hisST_iso)
        VVhisto.append(hisVV_iso)
        TThisto.append(hisTT_iso)
        ZTThisto.append(hisZTT_iso_relax)
        ZLLhisto.append(hisZLL_iso_relax)
        GGTThisto.append(hisGGTT_iso)
    
    return SThisto, VVhisto, TThisto, ZTThisto,ZLLhisto,GGTThisto
    
    
    
    
    