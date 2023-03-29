#include "Sys.h"


//up: true indicates up, false indicates down
float Gettauidsysweight(float taupt ,float ptlow, float pthigh, bool up, Vec_t LepCand_gen,Vec_t LepCand_tauidMsf, Vec_t LepCand_tauidMsf_up, Vec_t LepCand_tauidMsf_down, int tauindex){
    float tauidsysweight=1.0;
    if ((ptlow==40 && taupt>=40) || (ptlow!=40 && taupt>=ptlow && taupt<pthigh)){
        if (LepCand_gen[tauindex]==5){
            if (up){
                tauidsysweight = LepCand_tauidMsf_up[tauindex] / LepCand_tauidMsf[tauindex];
            }
            else{
                tauidsysweight = LepCand_tauidMsf_down[tauindex] / LepCand_tauidMsf[tauindex];
            }
        }
    }
    return tauidsysweight;
}


TLorentzVector Gettauessys(bool up, Vec_t LepCand_DecayMode, Vec_t LepCand_gen,Vec_t LepCand_taues, Vec_t LepCand_taues_down, Vec_t LepCand_taues_up, int tauindex, TLorentzVector my_tau, int decaymode){
    //decaymode: 0, 1 , 1011 indicates 10 and 11, 3prong
    TLorentzVector my_newtau = my_tau;

    if (LepCand_gen[tauindex]==5){
        if ((decaymode==1011 && (LepCand_DecayMode[tauindex]==10 || LepCand_DecayMode[tauindex]==11))|| (decaymode!=1011 && LepCand_DecayMode[tauindex]==decaymode) ){
            if (up){
                my_newtau*=LepCand_taues_up[tauindex]/LepCand_taues[tauindex];
            }
            else {
                my_newtau*=LepCand_taues_down[tauindex]/LepCand_taues[tauindex];
            }

        }

    }

    return my_newtau;
}


float Gettauantimusysweight( bool up, bool barrel, Vec_t LepCand_gen, Vec_t LepCand_antimusf, Vec_t LepCand_antimusf_up, Vec_t LepCand_antimusf_down, int tauindex, float taueta){
    float tauantimusysweight=1.0;

    if ((barrel && taueta<1.5) || (!barrel && taueta>=1.5)){
        if (LepCand_gen[tauindex]==2 or LepCand_gen[tauindex]==4){
            if (up){
                tauantimusysweight = LepCand_antimusf_up[tauindex] / LepCand_antimusf[tauindex];
            }
            else{
                tauantimusysweight = LepCand_antimusf_down[tauindex] / LepCand_antimusf[tauindex];
            }

        }
    }
    return tauantimusysweight;
}


float Gettauantielesysweight( bool up, bool barrel, Vec_t LepCand_gen, Vec_t LepCand_antielesf, Vec_t LepCand_antielesf_up, Vec_t LepCand_antielesf_down, int tauindex, float taueta){
    float tauantielesysweight=1.0;

    if ((barrel && taueta<1.5) || (!barrel && taueta>=1.5)){
        if (LepCand_gen[tauindex]==2 or LepCand_gen[tauindex]==4){
            if (up){
                tauantielesysweight = LepCand_antielesf_up[tauindex] / LepCand_antielesf[tauindex];
            }
            else{
                tauantielesysweight = LepCand_antielesf_down[tauindex] / LepCand_antielesf[tauindex];
            }

        }
    }
    return tauantielesysweight;
}


TLorentzVector Gettaufessys(bool up, Vec_t LepCand_DecayMode, Vec_t LepCand_gen,Vec_t LepCand_fes, Vec_t LepCand_fes_down, Vec_t LepCand_fes_up, int tauindex, TLorentzVector my_tau, int decaymode){
    //decaymode: 0, 1 
    TLorentzVector my_newtau = my_tau;

    if (LepCand_gen[tauindex]==1 || LepCand_gen[tauindex]==3 ){
        if ( LepCand_DecayMode[tauindex]==decaymode ){
            if (up){
                my_newtau*=LepCand_fes_up[tauindex]/LepCand_fes[tauindex];
            }
            else {
                my_newtau*=LepCand_fes_down[tauindex]/LepCand_fes[tauindex];
            }

        }
    }

    return my_newtau;
}



