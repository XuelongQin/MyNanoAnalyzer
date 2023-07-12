from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas,TH1, TH2, TH1F
import numpy as np
from ROOT.RDF import TH1DModel, TH2DModel
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
sys.path.append("..")
from pyFunc.gethisto_SR_tautau import df_sys,gethisto,DY_rescale,gethisto_BSM
time_start=timer.time()
ROOT.gInterpreter.AddIncludePath('/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/lib')
ROOT.gInterpreter.Declare('#include "basic_sel.h"')
ROOT.gInterpreter.Declare('#include "GetPFtrk.h"')
ROOT.gInterpreter.Declare('#include "Correction.h"')
ROOT.gInterpreter.Declare('#include "ApplyFR.h"')
ROOT.gSystem.Load('/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/lib/RDFfunc.so')


TH1.SetDefaultSumw2(True)
TH2.SetDefaultSumw2(True)

nbins = int(8)
binning = np.array([40,55,70,85,100,150,200,350,500],dtype=float)


year = sys.argv[1]
sample = "GGToTauTau_Ctb20"

def getBSMhisto(df, channel, name ):
    hisGGTTlist = []
    integer = 0
    decimals = 0
    ceBRname = ""
    TauG2weightsname = ""
    TauG2weightsname = "TauG2Weights_ceBRe33_0p0"
    histo_normal = gethisto_BSM(df,channel,TauG2weightsname,nbins,binning)
    histo_normal.SetName("GGTT{}".format(name))
    print ("SM basic ", histo_normal.Integral())
    hisGGTTlist.append(histo_normal)
    for i in np.arange(-40.0,40.8,0.8):
        if (i<-0.4):
            integer = int(i-0.1)
        else:
            integer = int(i+0.1)
        decimals = int(round(abs(i-integer)*10,0))
        print ("i = ", i , " integer ", integer, " decimals ", decimals)
        if (i<-0.4):
            ceBRname = "_m{}p{}".format(abs(integer),decimals)
        else:
            ceBRname = "_{}p{}".format(integer,decimals)
        TauG2weightsname = "TauG2Weights_ceBRe33"+ceBRname
        histo = gethisto_BSM(df,channel,TauG2weightsname,nbins,binning)
        histo.SetName("GGTT{}{}".format(ceBRname,name))
        print ("BSM ", ceBRname , " " ,histo.Integral())
        hisGGTTlist.append(histo)
    return hisGGTTlist


realcut = ""
    
weight = "xsweight*SFweight*Acoweight*npvs_weight*nPUtrkweight*nHStrkweight*eeSF"
    
uncertainty = ["_CMS_tauid_stat1_dm0_yearDown","_CMS_tauid_stat1_dm0_yearUp","_CMS_tauid_stat1_dm1_yearDown","_CMS_tauid_stat1_dm1_yearUp","_CMS_tauid_stat1_dm10_yearDown","_CMS_tauid_stat1_dm10_yearUp","_CMS_tauid_stat1_dm11_yearDown","_CMS_tauid_stat1_dm11_yearUp",\
    "_CMS_tauid_stat2_dm0_yearDown","_CMS_tauid_stat2_dm0_yearUp","_CMS_tauid_stat2_dm1_yearDown","_CMS_tauid_stat2_dm1_yearUp","_CMS_tauid_stat2_dm10_yearDown","_CMS_tauid_stat2_dm10_yearUp","_CMS_tauid_stat2_dm11_yearDown","_CMS_tauid_stat2_dm11_yearUp", \
    "_CMS_tauid_syst_allerasDown", "_CMS_tauid_syst_allerasUp","_CMS_tauid_syst_yearDown", "_CMS_tauid_syst_yearUp", \
    "_CMS_tauid_syst_dm0_yearDown","_CMS_tauid_syst_dm0_yearUp","_CMS_tauid_syst_dm1_yearDown","_CMS_tauid_syst_dm1_yearUp","_CMS_tauid_syst_dm10_yearDown","_CMS_tauid_syst_dm10_yearUp","_CMS_tauid_syst_dm11_yearDown","_CMS_tauid_syst_dm11_yearUp",\
    "_CMS_ditautrg_dm0_yearDown","_CMS_ditautrg_dm0_yearUp", "_CMS_ditautrg_dm1_yearDown","_CMS_ditautrg_dm1_yearUp","_CMS_ditautrg_3prong_yearDown","_CMS_ditautrg_3prong_yearUp",\
    "_CMS_pileup_yearDown","_CMS_pileup_yearUp","_CMS_taues_dm0_yearDown","_CMS_taues_dm0_yearUp","_CMS_taues_dm1_yearDown","_CMS_taues_dm1_yearUp","_CMS_taues_3prong_yearDown","_CMS_taues_3prong_yearUp"]

uncertainty_func = ["Gettauidsysweight_dm(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_down[tauindex])",\
    "Gettauidsysweight_dm(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_up[tauindex])",\
    "Gettauidsysweight_dm(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_down[tauindex])",\
    "Gettauidsysweight_dm(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_up[tauindex])",\
    "Gettauidsysweight_dm(10,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_down[tauindex])",\
    "Gettauidsysweight_dm(10,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_up[tauindex])",\
    "Gettauidsysweight_dm(11,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_down[tauindex])",\
    "Gettauidsysweight_dm(11,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_up[tauindex])",\
    "Gettauidsysweight_dm(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_down[tauindex])",\
    "Gettauidsysweight_dm(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_up[tauindex])",\
    "Gettauidsysweight_dm(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_down[tauindex])",\
    "Gettauidsysweight_dm(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_up[tauindex])",\
    "Gettauidsysweight_dm(10,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_down[tauindex])",\
    "Gettauidsysweight_dm(10,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_up[tauindex])",\
    "Gettauidsysweight_dm(11,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_down[tauindex])",\
    "Gettauidsysweight_dm(11,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_up[tauindex])",\
    "Gettauidsysweight(LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_alleras_down[tauindex])",\
    "Gettauidsysweight(LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_alleras_up[tauindex])",\
    "Gettauidsysweight(LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_era_down[tauindex])",\
    "Gettauidsysweight(LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_era_up[tauindex])",\
    "Gettauidsysweight_dm(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_down[tauindex])",\
    "Gettauidsysweight_dm(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_up[tauindex])",\
    "Gettauidsysweight_dm(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_down[tauindex])",\
    "Gettauidsysweight_dm(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_up[tauindex])",\
    "Gettauidsysweight_dm(10,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_down[tauindex])",\
    "Gettauidsysweight_dm(10,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_up[tauindex])",\
    "Gettauidsysweight_dm(11,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_down[tauindex])",\
    "Gettauidsysweight_dm(11,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_up[tauindex])",\
    "Getditautrigweight(0,LepCand_DecayMode[tauindex],LepCand_tautriggersf[tauindex],LepCand_tautriggersf_down[tauindex])",\
    "Getditautrigweight(0,LepCand_DecayMode[tauindex],LepCand_tautriggersf[tauindex],LepCand_tautriggersf_up[tauindex])",\
    "Getditautrigweight(1,LepCand_DecayMode[tauindex],LepCand_tautriggersf[tauindex],LepCand_tautriggersf_down[tauindex])",\
    "Getditautrigweight(1,LepCand_DecayMode[tauindex],LepCand_tautriggersf[tauindex],LepCand_tautriggersf_up[tauindex])",\
    "Getditautrigweight(1011,LepCand_DecayMode[tauindex],LepCand_tautriggersf[tauindex],LepCand_tautriggersf_down[tauindex])",\
    "Getditautrigweight(1011,LepCand_DecayMode[tauindex],LepCand_tautriggersf[tauindex],LepCand_tautriggersf_up[tauindex])",\
    "Getpusysweight(puWeight,puWeightDown,npvs_weight,npvsDown_weight)",\
    "Getpusysweight(puWeight,puWeightUp,npvs_weight,npvsUp_weight)",\
    "Gettauessys(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_down[tauindex],my_tau)",\
    "Gettauessys(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_up[tauindex],my_tau)",\
    "Gettauessys(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_down[tauindex],my_tau)",\
    "Gettauessys(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_up[tauindex],my_tau)",\
    "Gettauessys(1011,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_down[tauindex],my_tau)",\
    "Gettauessys(1011,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_up[tauindex],my_tau)",\
    ]

uncertainty.append("_CMS_elasticRescalingDown")
uncertainty.append("_CMS_elasticRescalingUp")
uncertainty_func.append("GeteeSFsysweight(eeSF,nTrk,true)")
uncertainty_func.append("GeteeSFsysweight(eeSF,nTrk,false)")

print ("year is ", year , " sample is ", sample)
df= RDataFrame("Events","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuples_tautau_{}_basicsel/{}.root".format(year,sample))
df = df.Define("totalweight",weight)
fout=0

fout = TFile("Histo/HistoSR_{}/Taug2_tautau_{}_BSM.root".format(year,year),"recreate")


tt_0cut = "(nTrk==0) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40"
tt_1cut = "(nTrk==1) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40"
if (year == "2017"):
    tt_0cut = "(nTrk==0) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40 && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]"
    tt_1cut = "(nTrk==1) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40 && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]"

isocut = "&& isOS && leading_isolated && subleading_isolated "

dir0 = fout.mkdir("tt_0")
dir1 = fout.mkdir("tt_1")

tt_0cut = tt_0cut + realcut
tt_1cut = tt_1cut + realcut

df_tt0 = df.Filter(tt_0cut+isocut)
df_tt1 = df.Filter(tt_1cut+isocut)

print ("tt_0 basic ")
histo_tt0_list = getBSMhisto(df_tt0,"tt0","")
print ("tt_1 basic ")
histo_tt1_list = getBSMhisto(df_tt1,"tt1","")

dir0.cd()
for histo_tt0 in histo_tt0_list:
    histo_tt0.Write()
dir1.cd()
for histo_tt1 in histo_tt1_list:
    histo_tt1.Write()


for i in range(len(uncertainty)):
    uncertainty_name = str.replace(uncertainty[i],"year",year)
    if ("taues" in uncertainty_name):
        sysflag = 2
    elif ("pileup" in uncertainty_name or "elasticRescaling" in uncertainty_name):
        sysflag = 1
    else:
        sysflag = 0
    df_tt0_sys = df_sys(df,tt_0cut+isocut, sysflag, uncertainty_func[i])
    df_tt1_sys = df_sys(df,tt_1cut+isocut, sysflag, uncertainty_func[i])
    
    print ("tt_0 ", uncertainty_name, " " , uncertainty_func[i], " sysflag ", sysflag)
    histo_tt0_sys_list = getBSMhisto(df_tt0_sys,"tt0_{}".format(uncertainty_name),uncertainty_name)
    print ("tt_1 ", uncertainty_name, " " , uncertainty_func[i], " sysflag ", sysflag)
    histo_tt1_sys_list = getBSMhisto(df_tt1_sys,"tt1_{}".format(uncertainty_name),uncertainty_name)
    
    dir0.cd()
    for histo_tt0_sys in histo_tt0_sys_list:
        histo_tt0_sys.Write()
    dir1.cd()
    for histo_tt1_sys in histo_tt1_sys_list:
        histo_tt1_sys.Write()
fout.Close()
    



