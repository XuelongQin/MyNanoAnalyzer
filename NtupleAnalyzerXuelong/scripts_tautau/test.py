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
ROOT.gSystem.Load('../lib/RDFfunc.so')

channel = "tautau"
sample = "DYJetsToLL_M-50"
f1 = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/{}/RDF/{}_friend.root".format(channel,sample))
print ("f1",sample)
t1 = f1.Get("ntrktuple")
print ("t1",sample)

df = RDataFrame(t1)

df = df.Define("FR","GetFR_tautau(LepCand_DecayMode[tau2index],tau2pt,nTrk)")
df.Snapshot("testtuple","test.root")
