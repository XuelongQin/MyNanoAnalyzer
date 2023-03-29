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

float Gettauidsysweight(float taupt ,float ptlow, float pthigh, bool up, Vec_t LepCand_gen,Vec_t LepCand_tauidMsf, Vec_t LepCand_tauidMsf_up, Vec_t LepCand_tauidMsf_down, int tauindex);
TLorentzVector Gettauessys(bool up, Vec_t LepCand_DecayMode, Vec_t LepCand_gen,Vec_t LepCand_taues, Vec_t LepCand_taues_down, Vec_t LepCand_taues_up, int tauindex, TLorentzVector my_tau, int decaymode);
float Gettauantimusysweight( bool up, bool barrel, Vec_t LepCand_gen, Vec_t LepCand_antimusf, Vec_t LepCand_antimusf_up, Vec_t LepCand_antimusf_down, int tauindex, float taueta);
float Gettauantielesysweight( bool up, bool barrel, Vec_t LepCand_gen, Vec_t LepCand_antielesf, Vec_t LepCand_antielesf_up, Vec_t LepCand_antielesf_down, int tauindex, float taueta);
TLorentzVector Gettaufessys(bool up, Vec_t LepCand_DecayMode, Vec_t LepCand_gen,Vec_t LepCand_fes, Vec_t LepCand_fes_down, Vec_t LepCand_fes_up, int tauindex, TLorentzVector my_tau, int decaymode);
#endif