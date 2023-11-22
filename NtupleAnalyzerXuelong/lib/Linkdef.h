#ifdef __CINT__

#pragma link C++ nestedclass;
#pragma link C++ nestedtypedef;

// includes all header files
#include "basic_sel.h"
#include "Correction.h"
#include "GetPFtrk.h"
#include "ApplyFR.h"
#include "Sys.h"

// All classes
#pragma link C++ class musf+;
#pragma link C++ class Getxsw_W+;
#pragma link C++ class tauid_multicor+;
#pragma link C++ class spe_cor;
#pragma link C++ class mutauFR+;
#pragma link C++ class tautauFR+;
// all functions
#pragma link C++ function Getmutauindex Gettautauindex GetLepVector GetSFweight_mutau Getxsweight_W GetSFweight_tautau GetisOS Getis_isolated GetTransmass GetCollMass GetAcopl GeteeSF Get_tausfcor_mutau Get_tausfcor_tautau;
#pragma link C++ function GetMuonrecoSF GetMuonrecoSF_stat GetMuonrecoSF_syst GetMuonIsoSF GetMuonIsoSF_stat GetMuonIsoSF_syst GetMuonIDSF GetMuonIDSF_stat GetMuonIDSF_syst GetMuonTriggerSF GetMuonTriggerSF_stat GetMuonTriggerSF_syst GetMuonSF_HLTMu20Tau27;
#pragma link C++ function recovtxz1 recovtxz2 recovtxz3;
#pragma link C++ function Computedz_lep Computediffpt_lep ComputedeltaR_lep Compute_ditaudz Gettrkmatch Getntrkcut_mutau Getntrkcut_tautau;
#pragma link C++ function GetGenAco Get_Aweight Get_BScor_ditaudz Get_ntpuweight Get_ntHSweight;
#pragma link C++ function GetFR_mutau_qcd GetFR_mutau_w Getwfraction GetFR_mutau_qcd_sys_invertOS GetFR_mutau_w_sys_invertmT GetFR_mutau_qcd_sys_taupt GetFR_mutau_w_sys_taupt GetFR_mutau_qcd_sys_ntrk_dm GetFR_mutau_w_sys_ntrk_dm GetFR_mutau_qcd_sys_ntrk GetFR_mutau_w_sys_ntrk Getwfraction_sys GetFR_mutau;
#pragma link C++ function GetFR_tautau GetFR_tautau_qcd_sys_taupt GetFR_tautau_qcd_sys_ntrk_dm;
#pragma link C++ function Gettauidsysweight_dm Gettauidsysweight Getpusysweight Getditautrigweight Gettauessys Gettauantimusysweight Getmutautrgweight Getsinglemutrgweight GetL1PrefiringWeight Getmusysweight GeteeSFsysweight;
#endif