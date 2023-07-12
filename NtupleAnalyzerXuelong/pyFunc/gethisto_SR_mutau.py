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
    '''columns = ROOT.std.vector("string")()
    for c in ("run", "luminosityBlock", "event", \
        "isSingleMuonTrigger","isMuonTauTrigger",\
        "MET_phi","MET_pt","PV_ndof","PV_x","PV_y","PV_z","PV_chi2","PV_score","PV_npvs","PV_npvsGood",\
        "nLepCand","LepCand_id","LepCand_pt","LepCand_eta","LepCand_phi","LepCand_charge","LepCand_dxy","LepCand_dz","LepCand_gen",\
        "LepCand_vse","LepCand_vsmu","LepCand_vsjet","LepCand_muonMediumId","LepCand_muonIso",\
        "LepCand_tauidMsf","LepCand_tauidMsf_uncert0_up","LepCand_tauidMsf_uncert1_up", "LepCand_tauidMsf_syst_alleras_up", "LepCand_tauidMsf_syst_era_up", "LepCand_tauidMsf_syst_dm_era_up",\
        "LepCand_tauidMsf_uncert0_down", "LepCand_tauidMsf_uncert1_down", "LepCand_tauidMsf_syst_alleras_down", "LepCand_tauidMsf_syst_era_down", "LepCand_tauidMsf_syst_dm_era_down",\
        "LepCand_taues","LepCand_taues_up","LepCand_taues_down",\
        "LepCand_fes","LepCand_fes_up","LepCand_fes_down",\
        "LepCand_antimusf","LepCand_antimusf_up","LepCand_antimusf_down",\
        "LepCand_antielesf","LepCand_antielesf_up","LepCand_antielesf_down",\
        "LepCand_tautriggersf","LepCand_tautriggersf_up","LepCand_tautriggersf_down",\
        "LepCand_DecayMode","LepCand_trgmatch",\
        "LepCand_tk1Pt","LepCand_tk2Pt","LepCand_tk3Pt","LepCand_tk1Eta","LepCand_tk2Eta","LepCand_tk3Eta",\
        "LepCand_tk1Phi","LepCand_tk2Phi","LepCand_tk3Phi","LepCand_dz2","LepCand_dz3",\
        "nGenCand","GenCand_id","GenCand_pt","GenCand_eta","GenCand_phi",\
        "V_genpt","puWeight","puWeightUp","puWeightDown","tauindex","muindex","my_tau","my_mu","taupt","taueta","tauphi","taudz","mupt","mueta","muphi",\
        "mudz","isOS","is_isolated","xsweight","SFweight","mvis","mtrans","mcol","Acopl","zvtxll1",\
        "murecosf","murecosf_stat","murecosf_syst","muidsf","muidsf_stat","muidsf_syst","muisosf","muisosf_stat","muisosf_syst","mutrgsf","mutrgsf_stat","mutrgsf_syst","mutrgsf_crosstrg",\
        "nTrk","nPUtrk","nHStrk","Acoweight","npvs_weight","npvsDown_weight","npvsUp_weight","nPUtrkweight","nHStrkweight","genAco","eeSF", "wFR", "qcdFR", "FR"):
        columns.push_back(c)
    df_withFR.Snapshot("Events","test.root",columns)'''
    return df_withFR

def df_withFR_anti_sys(df_withFR, sysflag, func):
    df_withnewFR=0
    #sysflag: 0: qcd, 1: w, 2: wfraction
    if sysflag==0:
        df_withnewFR = df_withFR.Redefine("qcdFR",func).Redefine("FR","GetFR_mutau(qcdFR,wFR,wfraction)")
    else:
        df_withnewFR = df_withFR.Redefine("wFR",func).Redefine("FR","GetFR_mutau(qcdFR,wFR,wfraction)")
    #elif sysflag==2:
    #    df_withnewFR = df_withFR.Redefine("wfraction",func).Redefine("FR","GetFR_mutau(qcdFR,wFR,wfraction)")
    return df_withnewFR

def gethisto_anti(df,name,nbins,binning):
    hmodel = TH1DModel("h_{}_{}".format("mvis",name),"",nbins,binning)
    histo = df.Redefine("mvis","TMath::Min(float(499.),float(mvis))")\
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
    histo = df.Redefine("mvis","TMath::Min(float(499.),float(mvis))")\
        .Define("plotweight","totalweight").Histo1D(hmodel,"mvis","plotweight").GetPtr()
    return histo

def gethisto_BSM(df,name,TauG2Weights,nbins,binning):
    hmodel = TH1DModel("h_{}_{}_{}".format("mvis",name,TauG2Weights),"",nbins,binning)
    histo = df.Redefine("mvis","TMath::Min(float(499.),float(mvis))")\
        .Define("plotweight","totalweight*{}".format(TauG2Weights)).Histo1D(hmodel,"mvis","plotweight").GetPtr()
    return histo



def DY_rescale(histoDY_highntrk,histoDY):
    histo_rescale = histoDY_highntrk.Clone("DY_rescale")
    SF = histoDY.Integral()/histoDY_highntrk.Integral()
    histo_rescale.Scale(SF)
    return histo_rescale



