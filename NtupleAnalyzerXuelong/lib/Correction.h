#ifndef Correction_H
#define Correction_H
#include <ROOT/RDataFrame.hxx>
#include "TLorentzVector.h"

#include "TFile.h"
#include "TH1F.h"
#include "TF1.h"
#include "TMath.h"
#include <cmath>
#include <TRandom3.h>
#include <map>
#include "ROOT/RVec.hxx"
#include "ROOT/RDF/RInterface.hxx"
using namespace std;
using namespace ROOT;
using namespace ROOT::VecOps;
using Vec_t = const ROOT::RVec<float>&;

class spe_cor{
public:
    string yearconf;
    TF1* fit_aco_2030_2030;
    TF1* fit_aco_3040_2030 ;
    TF1* fit_aco_4050_2030;
    TF1* fit_aco_gt50_2030;
    TF1* fit_aco_3040_3040;
    TF1* fit_aco_4050_3040;
    TF1* fit_aco_gt50_3040;
    TF1* fit_aco_4050_4050;
    TF1* fit_aco_gt50_4050;
    TF1* fit_aco_gt50_gt50;
    TH1F* h_bs_sigma;
    TH1F* h_bs_z;
    TH1F* h_bs_sigma_mc;
    TH1F* h_bs_z_mc;
    float bs_z_mc;
    float bs_zsigma_mc;
    TH2F* correction_map;
    TH2F* correction_mapHS;
    spe_cor();
    spe_cor(string year);
};

float GetGenAco(int nZGenCand, Vec_t &ZGenCand_pt, Vec_t &ZGenCand_eta,Vec_t &ZGenCand_phi ,float Acopl);
float Get_Aweight(int nZGenCand, Vec_t &ZGenCand_pt, Vec_t &ZGenCand_eta,Vec_t &ZGenCand_phi,float gen_aco, string year);
//float Get_npvs_weight(int PV_npvs);
//float Get_npvsDown_weight(int PV_npvs);
//float Get_npvsUp_weight(int PV_npvs);
ROOT::RVec<float> Get_BScor_ditaudz( Vec_t &PF_dz, ROOT::RVec<int> &PF_isMatchedToGenHS,float PV_z, float zvtxll,string year );
float Get_ntpuweight(int ntpu, float zvtxll,string year);
float Get_ntHSweight(int ntracksHS, float gen_aco,string year);
#endif


