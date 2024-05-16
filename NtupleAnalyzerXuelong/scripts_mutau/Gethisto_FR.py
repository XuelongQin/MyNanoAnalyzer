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


def Gethisto_taupt_nTrk(cutname, cut, isoname, iso, variable, binning,nbins, decaymode, df):
    print ("nbins ", nbins)
    print ("binning", binning)
    hmodel = TH1DModel("h_tauFR_{}_dm{}_{}".format(cutname,decaymode,isoname),"",nbins,binning)
    if (variable == "nTrk"):
        hmodel = TH1DModel("h_tauFRnt_{}_dm{}_{}".format(cutname,decaymode,isoname),"",nbins,binning)
    dmcut = "&& LepCand_DecayMode[tauindex]=={}".format(decaymode)
    fullcut = cut + iso + dmcut
    print ("generate histogram with cut ", fullcut)
    histo = df.Filter(fullcut).Histo1D(hmodel,variable,"totalweight").GetPtr()
    return histo

def Gethisto_xtrg(cutname, cut, isoname, iso, df):
    histo=TH1F("h_tauFR_{}_xtrg_{}".format(cutname,isoname),"h_tauFR_{}_xtrg_{}".format(cutname,isoname),3,0,3)
    #alltrgcut = cut + iso + " && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex]))"
    alltrgcut = cut + iso + " && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger ))"
    #mutautrgcut = cut + iso + "&& (taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex])"
    mutautrgcut = cut + iso + "&& (taupt>32 && isMuonTauTrigger )"
    singlemutrgcut = cut + iso + "&& (taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])"
    if year=="2016pre" or year=="2016post":
        #alltrgcut = cut + iso + " && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger && LepCand_trgmatch[muindex]))"
        #mutautrgcut = cut + iso + "&& (taupt>30 && isMuonTauTrigger && LepCand_trgmatch[muindex])"
        alltrgcut = cut + iso + " && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger))"
        mutautrgcut = cut + iso + "&& (taupt>30 && isMuonTauTrigger )"
    if year=="2017":
        #alltrgcut = cut + iso + " && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex] && LepCand_trgmatch[tauindex]))"
        #mutautrgcut = cut + iso + "&& (taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex] && LepCand_trgmatch[tauindex])"
        alltrgcut = cut + iso + " && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger))"
        mutautrgcut = cut + iso + "&& (taupt>32 && isMuonTauTrigger )"

    alltrgnum = df.Filter(alltrgcut).Sum("totalweight").GetValue()
    alltrgerr = sqrt(df.Filter(alltrgcut).Sum("totalweight2").GetValue())

    mutautrgnum = df.Filter(mutautrgcut).Sum("totalweight").GetValue()
    mutautrgerr = sqrt(df.Filter(mutautrgcut).Sum("totalweight2").GetValue())
   
    singlemutrgnum = df.Filter(singlemutrgcut).Sum("totalweight").GetValue()
    singlemutrgerr = sqrt(df.Filter(singlemutrgcut).Sum("totalweight2").GetValue())

    histo.SetBinContent(1, alltrgnum)
    histo.SetBinError(1, alltrgerr)
    
    histo.SetBinContent(2, mutautrgnum)
    histo.SetBinError(2, mutautrgerr)
    
    histo.SetBinContent(3, singlemutrgnum)
    histo.SetBinError(3, singlemutrgerr)
    print ("generate xtrg histogram with cut ", alltrgcut)
    print (" alltrg ", alltrgnum, " mutautrg ", mutautrgnum, " singlemutrg ", singlemutrgnum)
    return histo

def Get2Dhisto(cutname, cut, signname,sign,df):
    hmodel = TH2DModel("fraction{}".format(signname),"fraction{}".format(signname),3,0,75,4,50,250)
    allcut = cut + sign
    print ("generate 2D histo with cut", allcut)
    histo = df.Filter(allcut).Define("mytrans", "TMath::Min(float(249.0),mtrans)").Histo2D(hmodel,"mytrans","mvis","totalweight").GetPtr()
    return histo
    

print ("year is ", year , " sample is ", sample)
df= RDataFrame("Events","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuples_mutau_{}_basicsel/{}.root".format(year,sample))

realcut = " && LepCand_gen[tauindex]!=0"
if "SingleMuon" in sample:
    realcut = ""
    
variablelist = ["taupt", "nTrk"]

bins_taupt0 = np.array([30,40,50,75,100,200,300],dtype=float)
binnum_taupt0 = bins_taupt0.size-1

bins_taupt1 = np.array([30,35,40,45,50,60,80,100,150,200,300],dtype=float)
binnum_taupt1 = bins_taupt1.size-1

bins_taupt10 = np.array([30,35,40,45,50,60,80,100,150,200,250,300],dtype=float)
binnum_taupt10 = bins_taupt10.size-1

bins_taupt11 = np.array([30,35,40,45,50,60,80,100,150,200,250,300],dtype=float)
binnum_taupt11 = bins_taupt11.size-1

bins_nt = np.array([-1,0,1,2,3,4,5,7,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],dtype=float)
binnum_nt = bins_nt.size-1

bins = bins_nt
binnum = binnum_nt
print ("xixi")
weight = "xsweight*SFweight*Acoweight*nPUtrkweight*nHStrkweight*eeSF*tausfcor"
if (sample=="GGToTauTau_Ctb20"):
    weight = "xsweight*SFweight*Acoweight*nPUtrkweight*nHStrkweight*eeSF*tausfcor*TauG2Weights_ceBRe_0p0"
df = df.Define("totalweight",weight).Define("totalweight2","totalweight*totalweight")
fout = TFile("Histo/HistoforFR_{}/{}.root".format(year,sample),"recreate")

print ("Get histo for FR for sample ", sample, " year ", year, " weight ", weight)

print ("###############first all histo of nTrk and taupt ################")
for DM in [0,1,10,11]:
    for variable in variablelist:
        if variable == "nTrk":
            bins = bins_nt
            binnum = binnum_nt
        else:
            if DM==0:
                bins = bins_taupt0
                binnum = binnum_taupt0
            elif DM==1:
                bins = bins_taupt1
                binnum = binnum_taupt1
            elif DM==10:
                bins = bins_taupt10
                binnum = binnum_taupt10
            else:
                bins = bins_taupt11
                binnum = binnum_taupt11
        QCDcut = "mtrans<50 && !isOS && taupt>30 && mvis>40 && isSingleMuonTrigger && LepCand_trgmatch[muindex]" + realcut
        Wcut = "isOS && mtrans>75 && taupt>30 && mvis>40 && isSingleMuonTrigger && LepCand_trgmatch[muindex]" + realcut
        histoQCDM = Gethisto_taupt_nTrk("QCD", QCDcut, "M", " && is_isolated", variable, bins, binnum,DM,df)
        histoQCDVVVL = Gethisto_taupt_nTrk("QCD", QCDcut, "VVVL", " && !is_isolated", variable, bins, binnum,DM,df)
        histoWM = Gethisto_taupt_nTrk("W", Wcut, "M", " && is_isolated", variable, bins, binnum,DM,df)
        histoWVVVL = Gethisto_taupt_nTrk("W", Wcut, "VVVL", " && !is_isolated", variable, bins, binnum,DM,df)
        fout.cd()
        histoQCDM.Write()
        histoQCDVVVL.Write()
        histoWM.Write()
        histoWVVVL.Write()

print ("###############Then all histo of xtrg################")
QCDcut = "mtrans<50 && !isOS && mvis>40" + realcut
Wcut = "isOS && mtrans>75 && mvis>40 " + realcut
histoxtrgQCDM =  Gethisto_xtrg("QCD", QCDcut, "M","&& is_isolated", df)
histoxtrgQCDVVVL =  Gethisto_xtrg("QCD", QCDcut, "VVVL","&& !is_isolated", df)
histoxtrgWM =  Gethisto_xtrg("W", Wcut, "M","&& is_isolated", df)
histoxtrgWVVVL =  Gethisto_xtrg("W", Wcut, "VVVL","&& !is_isolated", df)
fout.cd()
histoxtrgQCDM.Write()
histoxtrgQCDVVVL.Write()
histoxtrgWM .Write()
histoxtrgWVVVL.Write()

print ("###############Finally 2D histo to generate W fraction################")

'''cutWfraction = "taupt>30 && mvis>40 && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex])) && is_isolated"
if year=="2016pre" or year=="2016post":
    cutWfraction = "taupt>30 && mvis>40 && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger && LepCand_trgmatch[muindex])) && is_isolated"
if year=="2017":
    cutWfraction = "taupt>30 && mvis>40 && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex] && LepCand_trgmatch[tauindex])) && is_isolated"'''
cutWfraction = "taupt>30 && mvis>40 && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger)) && is_isolated"
if year=="2016pre" or year=="2016post":
    cutWfraction = "taupt>30 && mvis>40 && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger )) && is_isolated"
if year=="2017":
    cutWfraction = "taupt>30 && mvis>40 && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger )) && is_isolated"
histoWfractionOS = Get2Dhisto("cutWfractionOS",cutWfraction,"OS", " & isOS ", df)
histoWfractionSS = Get2Dhisto("cutWfractionSS",cutWfraction,"SS", " & !isOS ", df)
fout.cd()
histoWfractionOS.Write()
histoWfractionSS.Write()

fout.Close()


