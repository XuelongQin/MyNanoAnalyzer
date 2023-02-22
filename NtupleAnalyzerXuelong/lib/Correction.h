#ifndef Correction_H
#define Correction_H
#include <ROOT/RDataFrame.hxx>
#include "TLorentzVector.h"

#include "TFile.h"
#include "TH1F.h"
#include "TF1.h"
#include "TMath.h"
#include <cmath>
#include "ROOT/RVec.hxx"
#include "ROOT/RDF/RInterface.hxx"
using namespace std;
using namespace ROOT;
using namespace ROOT::VecOps;
using Vec_t = const ROOT::RVec<float>&;

float GetGenAco(int nZGenCand, Vec_t &ZGenCand_phi, float Acopl);
float Get_Aweight(float gen_aco);
float Get_npvsweight(int PV_npvs);
ROOT::RVec<float> Get_BScor_ditaudz( Vec_t &PF_dz, ROOT::RVec<bool> &PF_isMatchedToGenHS,float PV_z, float zvtxll );
float Get_ntpuweight(int ntpu, float zvtxll);
float Get_ntHSweight(int ntracksHS, float gen_aco);
#endif


