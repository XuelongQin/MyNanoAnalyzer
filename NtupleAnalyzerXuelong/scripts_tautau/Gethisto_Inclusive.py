from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas,TH1, TH2, TH1F
import numpy as np
from ROOT.RDF import TH1DModel, TH2DModel
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
time_start=timer.time()
ROOT.gInterpreter.AddIncludePath('/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/lib')
ROOT.gInterpreter.Declare('#include "basic_sel.h"')
ROOT.gInterpreter.Declare('#include "GetPFtrk.h"')
ROOT.gInterpreter.Declare('#include "Correction.h"')
ROOT.gInterpreter.Declare('#include "ApplyFR.h"')
ROOT.gSystem.Load('/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/lib/RDFfunc.so')
ROOT.EnableImplicitMT()

TH1.SetDefaultSumw2(True)
TH2.SetDefaultSumw2(True)

year = sys.argv[1]
sample = sys.argv[2]
name = sys.argv[3]
def gethisto(cut,cutname,variable,df):
    histo=0
    hmodel = TH1DModel("h_{}_{}".format(variable.name,cutname),"",variable.nbins,variable.binning)
    if "anti" in cutname:
        ###anti0 : 2 fake, anti1: leading fake, anti2: subleading fake
        if cutname == "anti1":
            histo = df.Filter(cut).Define("FR","GetFR_tautau(LepCand_DecayMode[tau1index],tau1pt,nTrk,1,\"{}\")".format(year)).Define("plotweight","totalweight*FR").Histo1D(hmodel,variable.name,"plotweight").GetPtr()
        elif cutname == "anti2":
            histo = df.Filter(cut).Define("FR","GetFR_tautau(LepCand_DecayMode[tau2index],tau2pt,nTrk,2,\"{}\")".format(year)).Define("plotweight","totalweight*FR").Histo1D(hmodel,variable.name,"plotweight").GetPtr()
        elif cutname == "anti0":
            histo = df.Filter(cut).Define("FR1","GetFR_tautau(LepCand_DecayMode[tau1index],tau1pt,nTrk,1,\"{}\")".format(year))\
                .Define("FR2","GetFR_tautau(LepCand_DecayMode[tau2index],tau2pt,nTrk,2,\"{}\")".format(year)).Define("plotweight","totalweight*FR1*FR2").Histo1D(hmodel,variable.name,"plotweight").GetPtr()
    else:
        histo = df.Filter(cut).Histo1D(hmodel,variable.name,"totalweight").GetPtr()
    return histo

class variable:
    def __init__(self, name, title, nbins, binning):
        self.name=name
        self.title = title
        self.nbins=nbins
        self.binning = binning
mvis = variable("mvis","m_{vis}",int(32),np.array([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,400,500],dtype=float))
tau1pt = variable("tau1pt","leading #tau p_{T}",int(29),np.array([40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
tau2pt = variable("tau2pt","subleading #tau p_{T}",int(29),np.array([40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
Aco = variable("Acopl","acoplanarity",int(40),np.arange(0,1.025,0.025,dtype=float))
#mtranse = variable("mtrans","m_{T}(#mu,MET)",int(36),np.arange(0,185,5,dtype=float))
nTrk = variable("nTrk","N_{tracks}",int(50),np.arange(0,102,2,dtype=float))
MET = variable("MET_pt","MET",int(19),np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,80,90,100,110,120],dtype=float))
tau1eta = variable("tau1eta","leading #tau #eta", int(25), np.arange(-2.5,2.7,0.2,dtype=float))
tau2eta = variable("tau2eta","subleading #tau #eta", int(25), np.arange(-2.5,2.7,0.2,dtype=float))
#variablelist = [mvis,taupt,mupt,Aco,mtranse]
variablelist = [mvis,tau1pt,tau2pt,Aco,nTrk,MET,tau1eta,tau2eta]

realcutleading = " && LepCand_gen[tau1index]!=0"
realcutsubleading = " && LepCand_gen[tau2index]!=0"
realcutdouble = "&& (LepCand_gen[tau1index]!=0 || LepCand_gen[tau2index]!=0)"
if ("Tau" in sample):
    realcutleading = ""
    realcutsubleading = ""
    realcutdouble = ""
    
weight = "xsweight*SFweight*Acoweight*npvs_weight*nPUtrkweight*nHStrkweight*eeSF"

print ("year is ", year , " sample is ", sample)
df= RDataFrame("Events","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuples_tautau_{}_basicsel/{}.root".format(year,sample))
df = df.Define("totalweight",weight)
fout=0
if sample == "DY":
    fout = TFile("Histo/HistoInclu_{}/{}.root".format(year,name),"recreate")
else:
    fout = TFile("Histo/HistoInclu_{}/{}.root".format(year,sample),"recreate")
for var in variablelist:
    cut = "nTrk>=0 && tau1pt>40 && tau2pt>40 && mvis>40"
    if year == "2017":
        cut = "nTrk>=0 && tau1pt>40 && tau2pt>40 && mvis>40 && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]"
    cutiso = cut+" && isOS && leading_isolated && subleading_isolated" + realcutleading + realcutsubleading
    
    cutleadingfake = cut + " && isOS && !leading_isolated && subleading_isolated " + realcutleading
    cutsubleadingfake = cut + " && isOS && leading_isolated && !subleading_isolated " + realcutsubleading
    cutdoublefake = cut + " && isOS && !leading_isolated && !subleading_isolated " + realcutdouble
    
    histoanti_leadingfake = gethisto(cutleadingfake,"anti1",var,df)
    histoanti_subleadingfake = gethisto(cutsubleadingfake,"anti2",var,df)
    histoanti_doublefake = gethisto(cutdoublefake,"anti0",var,df)
    histoiso = gethisto(cutiso,"",var,df)
    vardir = fout.mkdir(var.name)
    vardir.cd()
    histoanti_leadingfake.SetName("{}_leadinganti".format(name))
    histoanti_subleadingfake.SetName("{}_subleadinganti".format(name))
    histoanti_doublefake.SetName("{}_doubleanti".format(name))
    histoiso.SetName("{}".format(name))
    histoanti_leadingfake.Write()
    histoanti_subleadingfake.Write()
    histoanti_doublefake.Write()
    histoiso.Write()
fout.Close()
    
    
    
    