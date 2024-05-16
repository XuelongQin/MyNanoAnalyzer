#ifndef Sys_H
#define Sys_H
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

float Gettauidsysweight_dm(int decaymode, int taudecaymode, float taugen, float tauidsf, float tauidsf_change);
float Gettauidsysweight(float taugen, float tauidsf, float tauidsf_change);
float Getpusysweight( float puWeight, float puWeight_change,  float npvs_weight, float npvs_weight_change);
float Getditautrigweight(int decaymode, int taudecaymode, float tautrigweight, float tautrigweight_change);
TLorentzVector Gettauessys(int decaymode, int taudecaymode, float taugen, float taues, float taues_change, TLorentzVector my_tau);
float Gettauantimusysweight( bool barrel, float taugen, float tau_antimusf, float tau_antimusf_change, float taueta);
float Getmutautrgweight(bool isMuonTauTrigger, float tautrigsf, float tautrigsf_change);
float Getsinglemutrgweight(bool isSingleMuonTrigger, float mutrgSF, float mutrgSFchange);
float GetL1PrefiringWeight(float  L1PreFiringWeight_Nom, float  L1PreFiringWeight_Change);
float Getmusysweight(float muSF, float muSFchange);
float GeteeSFsysweight(float eeSF, int nTrk, bool down);
float GetPSsysweight(float PSweight, float Acoweight_ps, float Acoweight);
float GetPDFsysweight(Vec_t LHEPdfWeight, bool down);
float GetScalesysweight(float LHEScaleWeight, float sf_normal, float Acoweight_scale, float Acoweight);

#endif