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
        
        

def df_withFR_anti(df,anti,year):
    #anti0 double fake, anti1 leading fake, anti2 subleading fake
    if anti==0:
        df_withFR = df.Define("FR1","GetFR_tautau(LepCand_DecayMode[tau1index],tau1pt,nTrk,1,\"{}\")".format(year))\
                .Define("FR2","GetFR_tautau(LepCand_DecayMode[tau2index],tau2pt,nTrk,2,\"{}\")".format(year)).Define("FR", "FR1*FR2")
    elif anti==1:
        df_withFR = df.Define("FR","GetFR_tautau(LepCand_DecayMode[tau1index],tau1pt,nTrk,1,\"{}\")".format(year))
    else:
        df_withFR = df.Define("FR","GetFR_tautau(LepCand_DecayMode[tau2index],tau2pt,nTrk,2,\"{}\")".format(year))
    return df_withFR


def df_withFR_anti_sys(df_withFR, sysflag, func):
    df_withnewFR=0
    #sysflag: 0: double , 1: leading, 2: subleading
    func1 = str.replace(func,"leading","0")
    func1 = str.replace(func1,"taukpt","tau1pt")
    func1 = str.replace(func1,"tauindex","tau1index")
    
    func2 = str.replace(func,"leading","1")
    func2 = str.replace(func2,"taukpt","tau2pt")
    func2 = str.replace(func2,"tauindex","tau2index")
    
    if sysflag==0:
        func1 = str.replace(func1,"qcdFR","FR1")
        func2 = str.replace(func2,"qcdFR","FR2")
        print ("sysflag is 0 ", " func1 ", func1, " func2 ", func2)
        df_withnewFR = df_withFR.Redefine("FR1",func1).Redefine("FR2",func2).Redefine("FR","FR1*FR2")
    elif sysflag==1:
        func1 = str.replace(func1,"qcdFR","FR")
        print ("sysflag is 1 ", " func1 ", func1)
        df_withnewFR = df_withFR.Redefine("FR",func1)

    elif sysflag==2:
        func2 = str.replace(func2,"qcdFR","FR")
        print ("sysflag is 2 ", " func2 ", func2)
        df_withnewFR = df_withFR.Redefine("FR",func2)
    return df_withnewFR

def gethisto_anti(df,name,nbins,binning):
    hmodel = TH1DModel("h_{}_{}".format("mvis",name),"",nbins,binning)
    histo = df.Redefine("mvis","TMath::Min(float(249.),float(mvis))")\
        .Define("plotweight","totalweight*FR").Histo1D(hmodel,"mvis","plotweight").GetPtr()
    return histo


def DY_rescale(histoDY_highntrk,histoDY,SF):
    histo_rescale = histoDY_highntrk.Clone("DY_rescale")
    #SF = histoDY.Integral()/histoDY_highntrk.Integral()
    histo_rescale.Scale(SF)
    return histo_rescale


def df_sys(df,cut,sysflag,func):
    #sysflag: 0: newweight for 2 taus, 1: new puweight,2: new tauhpt
    df_new = 0
    if sysflag==0:
        func1 = str.replace(func,"tauindex","tau1index")
        func2 = str.replace(func,"tauindex","tau2index")
        print ("sysflag is 0 ", " func1 ", func1, " func2 ", func2)
        df_new = df.Filter(cut).Define("weight1",func1).Define("weight2",func2).Redefine("totalweight", "totalweight*weight1*weight2")
    elif sysflag==1:
        print ("sysflag is 1 ", " func ", func)
        df_new = df.Filter(cut).Define("weight2",func).Redefine("totalweight", "totalweight*weight2")
    else:
        func1 = str.replace(func,"tauindex","tau1index")
        func2 = str.replace(func,"tauindex","tau2index")
        func1 = str.replace(func1,"my_tau","my_tau1")
        func2 = str.replace(func2,"my_tau","my_tau2")
        print ("sysflag is 0 ", " func1 ", func1, " func2 ", func2)
        df_new = df.Redefine("my_tau1",func1).Redefine("tau1pt","my_tau1.Pt()").Redefine("my_tau2",func2).Redefine("tau2pt","my_tau2.Pt()").\
            Redefine("mvis","(my_tau1 + my_tau2).M()").Filter(cut)
    return df_new

def gethisto(df,name,nbins,binning):
    hmodel = TH1DModel("h_{}_{}".format("mvis",name),"",nbins,binning)
    histo = df.Redefine("mvis","TMath::Min(float(249.),float(mvis))")\
        .Define("plotweight","totalweight").Histo1D(hmodel,"mvis","plotweight").GetPtr()
    return histo

def gethisto_BSM(df,name,TauG2Weights,nbins,binning):
    hmodel = TH1DModel("h_{}_{}_{}".format("mvis",name,TauG2Weights),"",nbins,binning)
    histo = df.Redefine("mvis","TMath::Min(float(249.),float(mvis))")\
        .Define("plotweight","totalweight*{}".format(TauG2Weights)).Histo1D(hmodel,"mvis","plotweight").GetPtr()
    return histo
