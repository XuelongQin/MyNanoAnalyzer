from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas,TH1, TH2, TH1F
import numpy as np
from ROOT.RDF import TH1DModel, TH2DModel
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
import ctypes
sys.path.append("..")
from pyFunc.gethisto_SR_tautau import df_sys,gethisto,DY_rescale
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


nbins = int(5)
binning = np.array([70,85,100,150,200,250],dtype=float)


year = sys.argv[1]
sample = sys.argv[2]
name = sys.argv[3]

realcut = " && LepCand_gen[tau1index]!=0 && LepCand_gen[tau2index]!=0 "
if "Tau" in sample:
    realcut = ""
    
weight = "xsweight*SFweight*Acoweight*nPUtrkweight*nHStrkweight*eeSF"
if "GGTT" in name:
    if name == "GGTT":
        weight = "xsweight*SFweight*Acoweight*nPUtrkweight*nHStrkweight*eeSF*TauG2Weights_ceBRe33_0p0"
    else:
        weight = "xsweight*SFweight*Acoweight*nPUtrkweight*nHStrkweight*eeSF*TauG2Weights_ceBRe33"+name[4:]
    print ("name is ", name, " weight is ", weight)

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
    "Getpusysweight(puWeight,puWeightDown,1.0,1.0)",\
    "Getpusysweight(puWeight,puWeightUp,1.0,1.0)",\
    "Gettauessys(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_down[tauindex],my_tau)",\
    "Gettauessys(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_up[tauindex],my_tau)",\
    "Gettauessys(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_down[tauindex],my_tau)",\
    "Gettauessys(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_up[tauindex],my_tau)",\
    "Gettauessys(1011,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_down[tauindex],my_tau)",\
    "Gettauessys(1011,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_up[tauindex],my_tau)",\
    ]

uncertainty.append("_CMS_L1PrefiringDown")
uncertainty.append("_CMS_L1PrefiringUp")
uncertainty_func.append("GetL1PrefiringWeight(L1PreFiringWeight_Nom, L1PreFiringWeight_Dn)")
uncertainty_func.append("GetL1PrefiringWeight(L1PreFiringWeight_Nom, L1PreFiringWeight_Up)")

if "GGTT" in name or name=="GGWW":
    uncertainty.append("_CMS_elasticRescalingDown")
    uncertainty.append("_CMS_elasticRescalingUp")
    uncertainty_func.append("GeteeSFsysweight(eeSF,nTrk,true)")
    uncertainty_func.append("GeteeSFsysweight(eeSF,nTrk,false)")

print ("year is ", year , " sample is ", sample, " name is ", name)
df= RDataFrame("Events","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuples_tautau_{}_basicsel/{}.root".format(year,sample))
df = df.Define("totalweight",weight)
fout=0
year4 = year

if year=="2016pre": year4="2016preVFP"
if year=="2016post": year4="2016postVFP"

if sample == "DY":
    fout = TFile("Histo/HistoSR_{}/{}.root".format(year,name),"recreate")
elif "GGToTauTau" in sample:
    if name == "GGTT":
        fout = TFile("Histo/HistoSR_{}/{}.root".format(year,sample),"recreate")
    else: 
        fout = TFile("Histo/HistoSR_{}/BSM/{}.root".format(year,name),"recreate")
else:
    fout = TFile("Histo/HistoSR_{}/{}.root".format(year,sample),"recreate")
    
tt_0cut = "(nTrk==0) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40"
tt_1cut = "(nTrk==1) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40"
DYshapecut = "(nTrk<10) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40"

#if year=="2017":
#    tt_0cut = "(nTrk==0) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40 && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]"
#    tt_1cut = "(nTrk==1) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40 && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]"
#    DYshapecut = "(nTrk<10) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40 && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]"
    

isocut = "&& isOS && leading_isolated && subleading_isolated "

dir0 = fout.mkdir("tt_0")
dir1 = fout.mkdir("tt_1")

tt_0cut = tt_0cut + realcut
tt_1cut = tt_1cut + realcut
DYshapecut = DYshapecut + realcut

if sample == "DY":
    df_DYhigh = df.Filter(DYshapecut+isocut)
    df_tt0 = df.Filter(tt_0cut+isocut)
    df_tt1 = df.Filter(tt_1cut+isocut)
    
    histoDYhigh = gethisto(df_DYhigh,"DYhigh", nbins, binning)
    histoDY_tt0 = gethisto(df_tt0,"tt0", nbins, binning)
    histoDY_tt1 = gethisto(df_tt1,"tt1", nbins, binning)

    '''err = ctypes.c_double(1.0)
    highvalue = histoDYhigh.IntegralAndError(1,10,err)
    print (name ," high ", highvalue, " +- ", err.value )
    tt_0value = histoDY_tt0.IntegralAndError(1,10,err)
    print (name ," tt_0 ", tt_0value, " +- ", err.value  )
    tt_1value = histoDY_tt1.IntegralAndError(1,10,err)
    print (name ," tt_1 ", tt_1value, " +- ", err.value  )

    fout.Close()
    exit(0)'''
    histo_tt0 = DY_rescale(histoDYhigh,histoDY_tt0,0.0242)
    histo_tt1 = DY_rescale(histoDYhigh,histoDY_tt1,0.0501)
    
    print ("tt_0 basic ", histo_tt0.Integral())
    print ("tt_1 basic ", histo_tt1.Integral())
    
    dir0.cd()
    histo_tt0.SetName("{}".format(name))
    histo_tt0.Write()
    dir1.cd()
    histo_tt1.SetName("{}".format(name))
    histo_tt1.Write()
    
    ### now systematic part
    for i in range(len(uncertainty)):
        uncertainty_name = str.replace(uncertainty[i],"year",year4)
        if ("taues" in uncertainty_name):
            sysflag = 2
        elif ("pileup" in uncertainty_name or "elasticRescaling" in uncertainty_name):
            sysflag = 1
        else:
            sysflag = 0
        df_DYhigh_sys = df_sys(df,DYshapecut+isocut, sysflag, uncertainty_func[i])
        df_tt0_sys = df_sys(df,tt_0cut+isocut, sysflag, uncertainty_func[i])
        df_tt1_sys = df_sys(df,tt_1cut+isocut, sysflag, uncertainty_func[i])
        histoDYhigh_sys = gethisto(df_DYhigh_sys,"DYhigh_{}".format(uncertainty_name), nbins, binning)
        histoDY_tt0_sys = gethisto(df_tt0_sys,"tt0_{}".format(uncertainty_name), nbins, binning)
        histoDY_tt1_sys = gethisto(df_tt1_sys,"tt1_{}".format(uncertainty_name), nbins, binning)
        histo_tt0_sys = DY_rescale(histoDYhigh_sys,histoDY_tt0_sys,0.0242)
        histo_tt1_sys = DY_rescale(histoDYhigh_sys,histoDY_tt1_sys,0.0501)
        print ("tt_0 ", uncertainty_name, " ", histo_tt0_sys.Integral())
        print ("tt_1 ", uncertainty_name, " ", histo_tt1_sys.Integral())
        dir0.cd()
        histo_tt0_sys.SetName("{}{}".format(name,uncertainty_name))
        histo_tt0_sys.Write()
        dir1.cd()
        histo_tt1_sys.SetName("{}{}".format(name,uncertainty_name))
        histo_tt1_sys.Write()


else:
    df_tt0 = df.Filter(tt_0cut+isocut)
    df_tt1 = df.Filter(tt_1cut+isocut)
    histo_tt0 = gethisto(df_tt0,"tt0", nbins, binning)
    histo_tt1 = gethisto(df_tt1,"tt1", nbins, binning)
    print ("tt_0 basic ", histo_tt0.Integral())
    print ("tt_1 basic ", histo_tt1.Integral())
    dir0.cd()
    histo_tt0.SetName("{}".format(name))
    histo_tt0.Write()
    dir1.cd()
    histo_tt1.SetName("{}".format(name))
    histo_tt1.Write()

    
    ### now systematic part
    if (name != "data_obs"):
        for i in range(len(uncertainty)):
            uncertainty_name = str.replace(uncertainty[i],"year",year4)
            if ("taues" in uncertainty_name):
                sysflag = 2
            elif ("pileup" in uncertainty_name or "elasticRescaling" in uncertainty_name):
                sysflag = 1
            else:
                sysflag = 0
            df_tt0_sys = df_sys(df,tt_0cut+isocut, sysflag, uncertainty_func[i])
            df_tt1_sys = df_sys(df,tt_1cut+isocut, sysflag, uncertainty_func[i])
            histo_tt0_sys = gethisto(df_tt0_sys,"tt0_{}".format(uncertainty_name), nbins, binning)
            histo_tt1_sys = gethisto(df_tt1_sys,"tt1_{}".format(uncertainty_name), nbins, binning)
            print ("tt_0 ", uncertainty_name, " ", histo_tt0_sys.Integral())
            print ("tt_1 ", uncertainty_name, " ", histo_tt1_sys.Integral())
            dir0.cd()
            histo_tt0_sys.SetName("{}{}".format(name,uncertainty_name))
            histo_tt0_sys.Write()
            dir1.cd()
            histo_tt1_sys.SetName("{}{}".format(name,uncertainty_name))
            histo_tt1_sys.Write()
fout.Close()
        
    
        
        
        
    
    
    






