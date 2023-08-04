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
        

def df_withFR_anti(df,year):
    df_withFR  = df.Define("qcdFR","GetFR_mutau_qcd(LepCand_DecayMode[tauindex],taupt,nTrk, isMuonTauTrigger,\"{}\")".format(year))\
        .Define("wFR","GetFR_mutau_w(LepCand_DecayMode[tauindex],taupt,nTrk, isMuonTauTrigger,\"{}\")".format(year)).Define("wfraction", "Getwfraction(mvis, mtrans,\"{}\")".format(year))\
        .Define("FR", "GetFR_mutau(qcdFR,wFR,wfraction)")
    return df_withFR

def df_withFR_anti_sys(df_withFR, sysflag, func):
    df_withnewFR=0
    #sysflag: 0: qcd, 1: w, 2: wfraction
    if sysflag==0:
        df_withnewFR = df_withFR.Redefine("qcdFR",func).Redefine("FR","GetFR_mutau(qcdFR,wFR,wfraction)")
    elif sysflag==2:
        df_withnewFR = df_withFR.Redefine("wfraction",func).Redefine("FR","GetFR_mutau(qcdFR,wFR,wfraction)")
    else:
        df_withnewFR = df_withFR.Redefine("wFR",func).Redefine("FR","GetFR_mutau(qcdFR,wFR,wfraction)")
    return df_withnewFR

def gethisto_anti(df,name,nbins,binning):
    hmodel = TH1DModel("h_{}_{}".format("mvis",name),"",nbins,binning)
    histo = df.Redefine("mvis","TMath::Min(float(249.),float(mvis))")\
        .Define("plotweight","totalweight*FR").Histo1D(hmodel,"mvis","plotweight").GetPtr()
    return histo
    
    
def df_sys(df,cut,sysflag,func):
    #sysflag: 0: newweight, 1: new tauhpt
    df_new = 0
    if sysflag==0:
        df_new = df.Filter(cut).Define("weight2",func).Redefine("totalweight", "totalweight*weight2")
    else:
        df_new = df.Redefine("my_tau",func).Redefine("taupt","my_tau.Pt()").Redefine("mvis","(my_mu + my_tau).M()").Filter(cut)
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



def DY_rescale(histoDY_highntrk,histoDY,SF):
    histo_rescale = histoDY_highntrk.Clone("DY_rescale")
    #SF = histoDY.Integral()/histoDY_highntrk.Integral()
    histo_rescale.Scale(SF)
    return histo_rescale



