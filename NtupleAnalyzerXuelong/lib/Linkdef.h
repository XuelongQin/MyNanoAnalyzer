#ifdef __CINT__

#pragma link C++ nestedclass;
#pragma link C++ nestedtypedef;

// includes all header files
#include "basic_sel.h"
#include "Correction.h"
#include "GetPFtrk.h"
#include "ApplyFR.h"

// All classes
//#pragma link C++ class HelloWorld+;

// all functions
#pragma link C++ function Getmutauindex Gettautauindex GetLepVector GetSFweight_mutau Getxsweight_W GetSFweight_tautau Getxsweight GetisOS Getis_isolated GetTransmass GetCollMass GetAcopl;
#pragma link C++ function recovtxz1 recovtxz2 recovtxz3;
#pragma link C++ function Computedz_mu Computediffpt_mu ComputedeltaR_mu Compute_ditaudz Getntrkcut_mutau Getntrkcut_tautau;
#pragma link C++ function GetGenAco Get_Aweight Get_npvsweight Get_BScor_ditaudz Get_ntpuweight Get_ntHSweight;
#pragma link C++ function GetFR_mutau;
#endif