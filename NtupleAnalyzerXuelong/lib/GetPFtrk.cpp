#include "GetPFtrk.h"

ROOT::RVec<float> Computedz_mu(Vec_t Muontrk_dz, float mudz) {
    auto mod = [mudz]( float dz) { return fabs(dz-mudz); };
    ROOT::RVec<float>  dz_mu = Map(Muontrk_dz,mod);
    return dz_mu;
}

ROOT::RVec<float> Computediffpt_mu(Vec_t Muontrk_pt, float mupt) {
    auto mod = [mupt]( float pt) { return fabs(pt-mupt)/mupt; };
    ROOT::RVec<float> diffpt_mu = Map(Muontrk_pt,mod);
    return diffpt_mu;
}

ROOT::RVec<float> ComputedeltaR_mu(Vec_t Muontrk_pt, Vec_t Muontrk_eta,Vec_t Muontrk_phi, TLorentzVector my_mu) {
    auto mod = [my_mu](float pt, float eta, float phi){
        TLorentzVector Muontrk;
        Muontrk.SetPtEtaPhiM(pt,eta,phi,0);
        return my_mu.DeltaR(Muontrk);
    };
    ROOT::RVec<float> deltaR_mu = Map(Muontrk_pt,Muontrk_eta,Muontrk_phi,mod);
    return deltaR_mu;
}

ROOT::RVec<float> Compute_ditaudz(Vec_t trk_dz, float PV_z, float zvtxll){
    auto mod = [PV_z, zvtxll](float dz){
        float ditaudz = dz+PV_z-zvtxll;
        return fabs(ditaudz);
    };
    ROOT::RVec<float> ditaudz = Map(trk_dz,mod);
    return ditaudz;
}

ROOT::RVec<int> Getntrkcut_mutau(Vec_t ChargedPFCandidates_pt,Vec_t ChargedPFCandidates_eta,Vec_t ChargedPFCandidates_phi,Vec_t ChargedPFCandidates_dz,\
    Vec_t FinalMuontrk_pt, Vec_t FinalMuontrk_eta, Vec_t FinalMuontrk_phi, Vec_t FinalMuontrk_dz,\
    Vec_t FinalTautrk_pt, Vec_t FinalTautrk_eta, Vec_t FinalTautrk_phi, Vec_t FinalTautrk_dz){
    auto mod = [FinalMuontrk_pt,FinalMuontrk_eta,FinalMuontrk_phi,FinalMuontrk_dz,\
        FinalTautrk_pt,FinalTautrk_eta,FinalTautrk_phi,FinalTautrk_dz](float PF_pt, float PF_eta, float PF_phi, float PF_dz){
        bool ismuontrk=false;
        bool istautrk=false;
        if (FinalMuontrk_pt.size()>0){
            for (unsigned int i =0; i<FinalMuontrk_pt.size();i++ ){
                if (PF_pt==FinalMuontrk_pt[i] && PF_eta==FinalMuontrk_eta[i] && PF_phi==FinalMuontrk_phi[i] && PF_dz==FinalMuontrk_dz[i])
                ismuontrk=true;
            }
        }
        
        if (FinalTautrk_pt.size()>0){
            for (unsigned int i =0; i<FinalTautrk_pt.size();i++ ){
                if (PF_pt==FinalTautrk_pt[i] && PF_eta==FinalTautrk_eta[i] && PF_phi==FinalTautrk_phi[i] && PF_dz==FinalTautrk_dz[i])
                istautrk=true;
            }
        }
        if (ismuontrk || istautrk){
            return 0;
        }
        else{
            return 1;
        }
    };
    ROOT::RVec<int> cut_excludemutau = Map(ChargedPFCandidates_pt,ChargedPFCandidates_eta,ChargedPFCandidates_phi,ChargedPFCandidates_dz,mod);
    return cut_excludemutau;
}


ROOT::RVec<int> Getntrkcut_tautau(Vec_t ChargedPFCandidates_pt,Vec_t ChargedPFCandidates_eta,Vec_t ChargedPFCandidates_phi,Vec_t ChargedPFCandidates_dz,\
    Vec_t FinalTautrk_pt, Vec_t FinalTautrk_eta, Vec_t FinalTautrk_phi, Vec_t FinalTautrk_dz){
    auto mod = [FinalTautrk_pt,FinalTautrk_eta,FinalTautrk_phi,FinalTautrk_dz](float PF_pt, float PF_eta, float PF_phi, float PF_dz){
        bool istautrk=false;
        if (FinalTautrk_pt.size()>0){
            for (unsigned int i =0; i<FinalTautrk_pt.size();i++ ){
                if (PF_pt==FinalTautrk_pt[i] && PF_eta==FinalTautrk_eta[i] && PF_phi==FinalTautrk_phi[i] && PF_dz==FinalTautrk_dz[i])
                istautrk=true;
            }
        }
        if (istautrk){
            return 0;
        }
        else{
            return 1;
        }
    };
    ROOT::RVec<int> cut_excludetautau = Map(ChargedPFCandidates_pt,ChargedPFCandidates_eta,ChargedPFCandidates_phi,ChargedPFCandidates_dz,mod);
    return cut_excludetautau;
    }








