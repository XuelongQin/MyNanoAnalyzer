#ifndef basic_sel_H
#define basic_sel_H

#include <ROOT/RDataFrame.hxx>
#include "TLorentzVector.h"

#include "TFile.h"
#include "TH1F.h"
#include "TH1D.h"
#include "TF1.h"
#include "TMath.h"
#include <cmath>
#include <string>
#include <map>
#include "ROOT/RVec.hxx"
#include "ROOT/RDF/RInterface.hxx"
using namespace std;
using namespace ROOT;
using namespace ROOT::VecOps;
//using Vec_t = const ROOT::RVec<float>&;

class musf
{
public:
    string yearconf;
    TH1F* h_muonRecoeff;
    TH1F* h_muonRecoeff_stat;
    TH1F* h_muonRecoeff_syst;
    TH2F* h_muonIsoSF;
    TH2F* h_muonIsoSF_stat;
    TH2F* h_muonIsoSF_syst;
    TH2F* h_muonIDSF;
    TH2F* h_muonIDSF_stat;
    TH2F* h_muonIDSF_syst;
    TH2F* h_muonTrgSF;
    TH2F* h_muonTrgSF_stat;
    TH2F* h_muonTrgSF_syst;
    TH2F* h_muonTrgSF_crosstrg;
    musf();
    musf(string year);
};


class Getxsw_W{
public:
    string yearconf;
    float weight0;
    float weight1;
    float weight2;
    float weight3;
    float weight4;
    Getxsw_W();
    Getxsw_W(string year);
};

class tauid_multicor{
public:
    string yearconf;
    float tauid_cor;
    float tauantimu_cor;
    float tauantie_cor;
    tauid_multicor();
    tauid_multicor(string year);
};


ROOT::RVec<int> Getmutauindex(int nLepCand, ROOT::VecOps::RVec<int> &LepCand_id ,ROOT::VecOps::RVec<float> &LepCand_dz);
ROOT::RVec<int> Gettautauindex(int nLepCand, ROOT::VecOps::RVec<float> &LepCand_dz);
TLorentzVector GetLepVector(int Lepindex, ROOT::VecOps::RVec<Float_t> &LepCand_pt, ROOT::VecOps::RVec<Float_t> &LepCand_eta,ROOT::VecOps::RVec<Float_t> &LepCand_phi,ROOT::VecOps::RVec<Float_t> &LepCand_gen, ROOT::VecOps::RVec<Float_t> &LepCand_taues, ROOT::VecOps::RVec<Float_t> &LepCand_fes);
TLorentzVector GetLepVector(int Lepindex, ROOT::VecOps::RVec<Float_t> &LepCand_pt, ROOT::VecOps::RVec<Float_t> &LepCand_eta,ROOT::VecOps::RVec<Float_t> &LepCand_phi);
float Getxsweight_W(float LHE_Njets, string year);
float GetMuonrecoSF(TLorentzVector my_mu, string year);
float GetMuonrecoSF_stat(TLorentzVector my_mu, string year);
float GetMuonrecoSF_syst(TLorentzVector my_mu, string year);
float GetMuonIsoSF(TLorentzVector my_mu, string year);
float GetMuonIsoSF_stat(TLorentzVector my_mu, string year);
float GetMuonIsoSF_syst(TLorentzVector my_mu, string year);
float GetMuonIDSF(TLorentzVector my_mu, string year);
float GetMuonIDSF_stat(TLorentzVector my_mu, string year);
float GetMuonIDSF_syst(TLorentzVector my_mu, string year);
float GetMuonTriggerSF(TLorentzVector my_mu, string year);
float GetMuonTriggerSF_stat(TLorentzVector my_mu, string year);
float GetMuonTriggerSF_syst(TLorentzVector my_mu, string year);
float GetMuonTriggerSF_crosstrg(TLorentzVector my_mu, string year);
float GetSFweight_mutau(float murecosf, float muisosf,float muidsf, float mutrgsf,float mutrgsf_crosstrg, float puweight, int tauindex, bool isSingleMuonTrigger, bool isMuonTauTrigger,  ROOT::VecOps::RVec<Float_t> &LepCand_gen, ROOT::VecOps::RVec<Float_t> &LepCand_tauidMsf, ROOT::VecOps::RVec<Float_t> &LepCand_antielesf,ROOT::VecOps::RVec<Float_t> &LepCand_antimusf,ROOT::VecOps::RVec<Float_t> &LepCand_tautriggersf, bool is_isolated);
//float GetSFweight_mutau(TLorentzVector my_mu,float puweight, int tauindex, ROOT::VecOps::RVec<Float_t> &LepCand_gen, ROOT::VecOps::RVec<Float_t> &LepCand_tauidMsf, ROOT::VecOps::RVec<Float_t> &LepCand_antielesf,ROOT::VecOps::RVec<Float_t> &LepCand_antimusf);
float GetSFweight_tautau(float puweight, int tau1index, int tau2index, ROOT::VecOps::RVec<Float_t> &LepCand_gen, ROOT::VecOps::RVec<Float_t> &LepCand_tauidMsf, ROOT::VecOps::RVec<Float_t> &LepCand_antielesf,ROOT::VecOps::RVec<Float_t> &LepCand_antimusf,ROOT::VecOps::RVec<Float_t> &LepCand_tautriggersf, bool leading_isolated, bool subleading_isolated);
float Get_tausfcor_mutau(int nTrk, ROOT::VecOps::RVec<Float_t> &LepCand_gen, int tauindex, bool is_isolated, string year );
float Get_tausfcor_tautau(int nTrk, ROOT::VecOps::RVec<Float_t> &LepCand_gen, int tau1index, int tau2index,bool leading_isolated,bool subleading_isolated, string year );
bool GetisOS(ROOT::VecOps::RVec<Int_t> &LepCand_charge, int lep1index,int lep2index);
bool Getis_isolated(ROOT::VecOps::RVec<Int_t> &LepCand_vsjet,int tauindex);
float TMass_F(float pt3lep, float px3lep, float py3lep, float met, float metPhi);
bool Getisfid(int is_emu, int is_etau, int is_mutau, int is_tautau, float fidpt_1, float fideta_1, float fidphi_1, float fidm_1, float fidpt_2, float fideta_2, float fidphi_2, float fidm_2, float fidgen_mtt, float fidntracks, float GenMET_pt, float GenMET_phi);
float GetTransmass(TLorentzVector my_mu, float MET_pt, float MET_phi);
float GetCollMass(TLorentzVector my_lep1, TLorentzVector my_lep2, float MET_pt, float MET_phi);
float GetAcopl(TLorentzVector my_lep1, TLorentzVector my_lep2);
float recovtxz1(float lep1dz,float lep2dz,float PV_z);
float recovtxz2(TLorentzVector my_Lep1,TLorentzVector my_Lep2,float lep1dz,float lep2dz,float PV_z);
float recovtxz3(float lep1pt,float lep2pt,float lep1dz,float lep2dz,float PV_z);
float GeteeSF(ROOT::VecOps::RVec<Float_t> &GenCand_pt, ROOT::VecOps::RVec<Float_t> &GenCand_eta, ROOT::VecOps::RVec<Float_t> &GenCand_phi, int nTrk);
#endif

