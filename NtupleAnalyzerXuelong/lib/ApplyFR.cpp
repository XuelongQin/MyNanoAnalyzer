#include "ApplyFR.h"



TFile *fFRw = new TFile("FRW_mutau.root","read");
TFile *fFR = new TFile("FRfit_mutau.root","read");

float GetFR_mutau(int taudecaymode, float mvis, float mtrans, float taupt, int nTrk){
    TH2F *WFR = (TH2F*)fFRw->Get(Form("hWFR_mvis_mtrans_DM%i",taudecaymode));
    float fracW= 0;
    float mymvis = mvis;
    float mymtrans = mtrans;
    if (mymvis>300) mymvis=299;
    if (mymvis<50) mymvis=51;
    if (mymtrans>75) {
        fracW=1.0;
    }
    else{
        fracW=WFR->GetBinContent(WFR->GetXaxis()->FindBin(mymtrans),WFR->GetYaxis()->FindBin(mymvis));
    }

    TF1 *FRQCD_taupt = (TF1*)fFR->Get(Form("fitfunc_QCD_DM%i_taupt",taudecaymode));
    TF1 *FRW_taupt = (TF1*)fFR->Get(Form("fitfunc_W_DM%i_taupt",taudecaymode));
    TF1 *FRQCD_nTrk = (TF1*)fFR->Get(Form("fitfunc_QCD_DM%i_nTrk",taudecaymode));
    TF1 *FRW_nTrk = (TF1*)fFR->Get(Form("fitfunc_W_DM%i_nTrk",taudecaymode));

    float mytaupt = taupt;
    if (taupt>300) mytaupt=299;
    float mynTrk=nTrk;
    if (nTrk>=100) mynTrk=99;
    float tfr_W = TMath::Min(1.0,FRW_taupt->Eval(mytaupt)*FRW_nTrk->Eval(mynTrk));
    float tfr_QCD = TMath::Min(1.0,FRQCD_taupt->Eval(mytaupt)*FRQCD_nTrk->Eval(mynTrk));
    float tfr=fracW*tfr_W + (1-fracW)*tfr_QCD;
    return tfr;
}

