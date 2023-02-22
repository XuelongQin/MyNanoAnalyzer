#include "Correction.h"

//Get Correction on Acopolanarity only for DY
TFile* f_aco=new TFile("./corrections/correction_acoplanarity_2018.root","read");
TF1* fit_aco = (TF1*) f_aco->Get("fit_A");

float GetGenAco(int nZGenCand, Vec_t &ZGenCand_phi, float Acopl){
    float genaco = 1.;
    if (nZGenCand==2){//if we have 2 ZGenCand, we use genaco 
        genaco = 1-fabs(ZGenCand_phi[0]-ZGenCand_phi[1])/TMath::Pi();
    }
    else{//else use recoaco
        genaco = Acopl;
    }
    return genaco;
}


float Get_Aweight(float gen_aco){
    float Acocut = 0.35;
    float A_weight = fit_aco->Eval(TMath::Min(Acocut,gen_aco));
    return A_weight;
}

//Get Correction on N_PV for all simulation
TFile* f_npvs=new TFile("./corrections/correction_npvs_2018.root","read");
TH1F* h_npvs_weight = (TH1F*) f_npvs->Get("correction_hist_npvs");
float Get_npvsweight(int PV_npvs){
    float npvs_weight=h_npvs_weight->GetBinContent(h_npvs_weight->GetXaxis()->FindBin(PV_npvs));
    return npvs_weight;
}

//Get Correction on beamspot for all simulation only for isMatchedToGenHS=0

TFile* f_bsz=new TFile("./corrections/beamspotz_2018.root","read");
TF1* f_beamspotz=(TF1*) f_bsz->Get("f_beamspotz");

TFile* f_bs=new TFile("./corrections/beamspot_TF1_2018.root","read");
TF1* h_bs_width = (TF1*) f_bs->Get("f1");

ROOT::RVec<float> Get_BScor_ditaudz( Vec_t &PF_dz, ROOT::RVec<bool> &PF_isMatchedToGenHS,float PV_z, float zvtxll ){
    float rnd_beamspot=h_bs_width->GetRandom(); // to do once per event, and use the same value for all tracks in the same event
    float rnd_beamspotz=f_beamspotz->GetRandom();
    auto mod = [PV_z, zvtxll,rnd_beamspot,rnd_beamspotz](float dz, bool HS ){
        float BScorrected_dz;
        if (HS){
            BScorrected_dz = fabs(PV_z+dz-zvtxll);
        }
        else{
            BScorrected_dz=fabs(((PV_z+dz)*rnd_beamspot/3.5 + (rnd_beamspotz-0.02488))-zvtxll);
        }
        return BScorrected_dz;
    };
    ROOT::RVec<float> BScordz_ditaudz = Map(PF_dz,PF_isMatchedToGenHS,mod);
    return BScordz_ditaudz;
}

//Get Correction on n_putracks, apply to all simulation samples
TFile *f_punt=new TFile("./corrections/npu_correction_2018.root");
TH2F* correction_map=(TH2F*) f_punt->Get("correction_map");

float Get_ntpuweight(int ntpu, float zvtxll){
    float ntpu_weight=correction_map->GetBinContent(correction_map->GetXaxis()->FindBin(ntpu),correction_map->GetYaxis()->FindBin(zvtxll)); // where zvtxll is the ditau vertex z, and ntpu is the number of BS corrected PU tracks inside the window
    return ntpu_weight;
}

//Get Correction on NHS_tracks, apply only to DY sample
TFile *f_hsnt=new TFile("./corrections/nhs_correction_2018.root");
TH2F* correction_mapHS=(TH2F*) f_hsnt->Get("correction_map");
float Get_ntHSweight(int ntracksHS, float gen_aco){
    float nths_weight=correction_mapHS->GetBinContent(correction_mapHS->GetXaxis()->FindBin(TMath::Min(30,ntracksHS)),correction_mapHS->GetYaxis()->FindBin(gen_aco)); // here ntracksHS is number of HS tracks in window not matched to the tautau decay products
    return nths_weight;
}








