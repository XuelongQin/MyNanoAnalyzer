#ifndef ApplyFR_H
#define ApplyFR_H
#include <ROOT/RDataFrame.hxx>
#include "TLorentzVector.h"

#include "TFile.h"
#include "TH1F.h"
#include "TF1.h"
#include "TMath.h"
#include <cmath>
#include "ROOT/RVec.hxx"
#include "ROOT/RDF/RInterface.hxx"
#include <vector>
#include <map>
using namespace std;
using namespace ROOT;
using namespace ROOT::VecOps;
using Vec_t = const ROOT::RVec<float>&;

class mutauFR
{
    public:
    string yearconf;
    TH2D *WFR_allDM;
    TF1 *FRQCD_taupt_DM0;
    TF1 *FRQCD_lownTrk_DM0;
    TF1 *FRQCD_highnTrk_DM0;
    TF1 *FRQCD_taupt_DM1;
    TF1 *FRQCD_lownTrk_DM1;
    TF1 *FRQCD_highnTrk_DM1;
    TF1 *FRQCD_taupt_DM10;
    TF1 *FRQCD_lownTrk_DM10;
    TF1 *FRQCD_highnTrk_DM10;
    TF1 *FRQCD_taupt_DM11;
    TF1 *FRQCD_lownTrk_DM11;
    TF1 *FRQCD_highnTrk_DM11;
    TF1 *FRW_taupt_DM0;
    TF1 *FRW_lownTrk_DM0;
    TF1 *FRW_highnTrk_DM0;
    TF1 *FRW_taupt_DM1;
    TF1 *FRW_lownTrk_DM1;
    TF1 *FRW_highnTrk_DM1;
    TF1 *FRW_taupt_DM10;
    TF1 *FRW_lownTrk_DM10;
    TF1 *FRW_highnTrk_DM10;
    TF1 *FRW_taupt_DM11;
    TF1 *FRW_lownTrk_DM11;
    TF1 *FRW_highnTrk_DM11;
    TH1F *err_nt0_ffQCD;
    TH1F *err_nt0_ffW;
    float QCDxtrgSF;
    float WxtrgSF;
    mutauFR();
    mutauFR(string year);
};



//float GetFR_mutau(int taudecaymode, float mvis, float mtrans, float taupt, int nTrk, bool isMuonTauTrigger);
float GetFR_mutau_qcd(int taudecaymode, float taupt, int nTrk, bool isMuonTauTrigger,string year);
float GetFR_mutau_w(int taudecaymode, float taupt, int nTrk, bool isMuonTauTrigger, string year);
float Getwfraction(float mvis, float mtrans,string year);
float GetFR_mutau_qcd_sys_invertOS(float qcdFR,float FRratio);
float GetFR_mutau_w_sys_invertmT(float wFR,float FRratio);
float GetFR_mutau_qcd_sys_taupt(float qcdFR, float taupt, int decaymode, int taudecaymode, bool down);
float GetFR_mutau_w_sys_taupt(float wFR, float taupt, int decaymode, int taudecaymode, bool down);
float GetFR_mutau_qcd_sys_ntrk_dm(float qcdFR, int decaymode, int taudecaymode, bool down,string year);
float GetFR_mutau_w_sys_ntrk_dm(float qcdFR, int decaymode, int taudecaymode, bool down, string year);
float GetFR_mutau_qcd_sys_ntrk(float qcdFR, float FRratio);
float GetFR_mutau_w_sys_ntrk(float wFR, float FRratio);
float Getwfraction_sys(float wfraction, bool down);
float GetFR_mutau(float qcdFR, float wFR, float wfraction);


class tautauFR
{
    public:
    string yearconf;
    TF1 *FRQCD_tau1pt_DM0_leading;
    TF1 *FRQCD_lownTrk_DM0_leading;
    TF1 *FRQCD_highnTrk_DM0_leading;

    TF1 *FRQCD_tau1pt_DM1_leading;
    TF1 *FRQCD_lownTrk_DM1_leading;
    TF1 *FRQCD_highnTrk_DM1_leading;

    TF1 *FRQCD_tau1pt_DM10_leading;
    TF1 *FRQCD_lownTrk_DM10_leading;
    TF1 *FRQCD_highnTrk_DM10_leading;

    TF1 *FRQCD_tau1pt_DM11_leading;
    TF1 *FRQCD_lownTrk_DM11_leading;
    TF1 *FRQCD_highnTrk_DM11_leading;


    TF1 *FRQCD_tau2pt_DM0_subleading;
    TF1 *FRQCD_lownTrk_DM0_subleading;
    TF1 *FRQCD_highnTrk_DM0_subleading;

    TF1 *FRQCD_tau2pt_DM1_subleading;
    TF1 *FRQCD_lownTrk_DM1_subleading;
    TF1 *FRQCD_highnTrk_DM1_subleading;

    TF1 *FRQCD_tau2pt_DM10_subleading;;
    TF1 *FRQCD_lownTrk_DM10_subleading;
    TF1 *FRQCD_highnTrk_DM10_subleading;

    TF1 *FRQCD_tau2pt_DM11_subleading;
    TF1 *FRQCD_lownTrk_DM11_subleading;
    TF1 *FRQCD_highnTrk_DM11_subleading;

    TH1F *err_nt0_ffQCD_leading;
    TH1F *err_nt0_ffQCD_subleading;
    tautauFR();
    tautauFR(string year);
};


float GetFR_tautau(int taudecaymode,float taupt, int nTrk,int fake, string year);
float GetFR_tautau_qcd_sys_taupt(float qcdFR, float taupt, int decaymode, int taudecaymode, bool down);
float GetFR_tautau_qcd_sys_ntrk_dm(float qcdFR, int decaymode, int taudecaymode, bool down, int leading, string year);



#endif