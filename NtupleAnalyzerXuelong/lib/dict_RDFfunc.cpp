// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME dict_RDFfunc
#define R__NO_DEPRECATION

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "RConfig.h"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// Header files passed as explicit arguments
#include "basic_sel.h"
#include "GetPFtrk.h"
#include "Correction.h"
#include "ApplyFR.h"

// Header files passed via #pragma extra_include

// The generated code does not explicitly qualify STL entities
namespace std {} using namespace std;

namespace {
  void TriggerDictionaryInitialization_dict_RDFfunc_Impl() {
    static const char* headers[] = {
"basic_sel.h",
"GetPFtrk.h",
"Correction.h",
"ApplyFR.h",
0
    };
    static const char* includePaths[] = {
"/cvmfs/cms.cern.ch/slc7_amd64_gcc10/lcg/root/6.24.07-bf41b0420bc269850b74e23486e2953a/include/",
"/afs/cern.ch/work/x/xuqin/taug-2/nanoAOD/CMSSW_12_4_2/src/MyNanoAnalyzer/NtupleAnalyzerXuelong_RDF_combine/lib/",
0
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "dict_RDFfunc dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_AutoLoading_Map;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "dict_RDFfunc dictionary payload"


#define _BACKWARD_BACKWARD_WARNING_H
// Inline headers
#include "basic_sel.h"
#include "GetPFtrk.h"
#include "Correction.h"
#include "ApplyFR.h"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[] = {
"GetFR_mutau", payloadCode, "@",
nullptr
};
    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("dict_RDFfunc",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_dict_RDFfunc_Impl, {}, classesHeaders, /*hasCxxModule*/false);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_dict_RDFfunc_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_dict_RDFfunc() {
  TriggerDictionaryInitialization_dict_RDFfunc_Impl();
}
