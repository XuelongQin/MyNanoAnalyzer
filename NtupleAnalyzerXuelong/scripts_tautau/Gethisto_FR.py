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


TH1.SetDefaultSumw2(True)
TH2.SetDefaultSumw2(True)

def Gethisto_taupt_nTrk(cutname, cut, isoname, iso, variable, binning,nbins, decaymode, df, leadingname):
    print ("nbins ", nbins)
    print ("binning", binning)
    hmodel = TH1DModel("h_tau{}FR_{}_dm{}_{}".format(leadingname,cutname,decaymode,isoname),"",nbins,binning)
    if (variable == "nTrk"):
        hmodel = TH1DModel("h_tau{}FRnt_{}_dm{}_{}".format(leadingname,cutname,decaymode,isoname),"",nbins,binning)
    dmcut = "&& LepCand_DecayMode[tau{}index]=={}".format(leadingname,decaymode)
    fullcut = cut + iso + dmcut
    print ("generate histogram with cut ", fullcut)
    histo = df.Filter(fullcut).Histo1D(hmodel,variable,"totalweight").GetPtr()
    return histo

year = sys.argv[1]
sample = sys.argv[2]


print ("year is ", year , " sample is ", sample)
df= RDataFrame("Events","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuples_tautau_{}_basicsel/{}.root".format(year,sample))

realcutleading = " && LepCand_gen[tau1index]!=0"
realcutsubleading = " && LepCand_gen[tau2index]!=0"
if "Tau" in sample:
    realcutleading = ""
    realcutsubleading = ""
    
variablelist = ["taupt","nTrk"]

bins_taupt0 = np.array([40,50,60,80,100,200,300],dtype=float)
binnum_taupt0 = bins_taupt0.size-1

bins_taupt1 = np.array([40,45,50,55,60,70,80,100,150,200,300],dtype=float)
binnum_taupt1 = bins_taupt1.size-1

bins_taupt10 = np.array([40,45,50,55,60,70,80,100,150,200,250,300],dtype=float)
binnum_taupt10 = bins_taupt10.size-1

bins_taupt11 = np.array([40,45,50,55,60,70,80,100,150,200,250,300],dtype=float)
binnum_taupt11 = bins_taupt11.size-1

bins_nt = np.array([-1,0,1,2,3,4,5,7,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],dtype=float)
binnum_nt = bins_nt.size-1

bins = bins_nt
binnum = binnum_nt

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
            QCDcutleading = "!isOS && tau1pt>40 && tau2pt>40 && mvis>40 && !subleading_isolated" + realcutleading
            QCDcutsubleading = "!isOS && tau1pt>40 && tau2pt>40 && mvis>40 && !leading_isolated" + realcutsubleading
            #if year=="2017":
            #    QCDcutleading = "!isOS && tau1pt>40 && tau2pt>40 && mvis>40 && subleading_isolated && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index] " + realcutleading
            #    QCDcutsubleading = "!isOS && tau1pt>40 && tau2pt>40 && mvis>40 && leading_isolated && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]" + realcutsubleading
                
            histoleading_M = Gethisto_taupt_nTrk("QCD",QCDcutleading,"M", " && leading_isolated",variable, bins, binnum, DM, df, "1")
            histoleading_VVVL = Gethisto_taupt_nTrk("QCD",QCDcutleading,"VVVL", " && !leading_isolated",variable, bins, binnum, DM, df, "1")
            histosubleading_M = Gethisto_taupt_nTrk("QCD",QCDcutsubleading,"M", " && subleading_isolated",variable, bins, binnum, DM, df, "2")
            histosubleading_VVVL = Gethisto_taupt_nTrk("QCD",QCDcutsubleading,"VVVL", " && !subleading_isolated",variable, bins, binnum, DM, df, "2")
            fout.cd()
            histoleading_M.Write()
            histoleading_VVVL.Write()
            histosubleading_M .Write()
            histosubleading_VVVL.Write()
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
                

            QCDcutleading = "!isOS && tau1pt>40 && tau2pt>40 && mvis>40 && !subleading_isolated" + realcutleading
            QCDcutsubleading = "!isOS && tau1pt>40 && tau2pt>40 && mvis>40 && !leading_isolated" + realcutsubleading
            #if year=="2017":
            #    QCDcutleading = "!isOS && tau1pt>40 && tau2pt>40 && mvis>40 && subleading_isolated && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]" + realcutleading
            #    QCDcutsubleading = "!isOS && tau1pt>40 && tau2pt>40 && mvis>40 && leading_isolated && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]" + realcutsubleading
            histoleading_M = Gethisto_taupt_nTrk("QCD",QCDcutleading,"M", " && leading_isolated","tau1pt", bins, binnum, DM, df, "1")
            histoleading_VVVL = Gethisto_taupt_nTrk("QCD",QCDcutleading,"VVVL", " && !leading_isolated","tau1pt", bins, binnum, DM, df, "1")
            histosubleading_M = Gethisto_taupt_nTrk("QCD",QCDcutsubleading,"M", " && subleading_isolated","tau2pt", bins, binnum, DM, df, "2")
            histosubleading_VVVL = Gethisto_taupt_nTrk("QCD",QCDcutsubleading,"VVVL", " && !subleading_isolated","tau2pt", bins, binnum, DM, df, "2")
            fout.cd()
            histoleading_M.Write()
            histoleading_VVVL.Write()
            histosubleading_M .Write()
            histosubleading_VVVL.Write()
            
fout.Close()


