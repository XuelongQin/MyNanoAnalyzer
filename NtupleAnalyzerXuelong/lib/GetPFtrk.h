#ifndef GetPFtrk_H
#define GetPFtrk_H

#include <ROOT/RDataFrame.hxx>
#include "TLorentzVector.h"

#include "TFile.h"
#include "TH1F.h"
#include "TMath.h"
#include <cmath>
#include "ROOT/RVec.hxx"
#include "ROOT/RDF/RInterface.hxx"
using namespace std;
using namespace ROOT;
using namespace ROOT::VecOps;

using Vec_t = const ROOT::RVec<float>&;
ROOT::RVec<float> Computedz_mu(Vec_t Muontrk_dz, float mudz);

ROOT::RVec<float> Computediffpt_mu(Vec_t Muontrk_pt, float mupt);

ROOT::RVec<float> ComputedeltaR_mu(Vec_t Muontrk_pt, Vec_t Muontrk_eta,Vec_t Muontrk_phi, TLorentzVector my_mu);

ROOT::RVec<float> Compute_ditaudz(Vec_t trk_dz, float PV_z, float zvtxll);

ROOT::RVec<int> Getntrkcut_mutau(Vec_t ChargedPFCandidates_pt,Vec_t ChargedPFCandidates_eta,Vec_t ChargedPFCandidates_phi,Vec_t ChargedPFCandidates_dz,\
    Vec_t FinalMuontrk_pt, Vec_t FinalMuontrk_eta, Vec_t FinalMuontrk_phi, Vec_t FinalMuontrk_dz,\
    Vec_t FinalTautrk_pt, Vec_t FinalTautrk_eta, Vec_t FinalTautrk_phi, Vec_t FinalTautrk_dz);
ROOT::RVec<int> Getntrkcut_tautau(Vec_t ChargedPFCandidates_pt,Vec_t ChargedPFCandidates_eta,Vec_t ChargedPFCandidates_phi,Vec_t ChargedPFCandidates_dz,\
    Vec_t FinalTautrk_pt, Vec_t FinalTautrk_eta, Vec_t FinalTautrk_phi, Vec_t FinalTautrk_dz);
#endif