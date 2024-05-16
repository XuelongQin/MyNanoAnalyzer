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
#include "Sys.h"

// Header files passed via #pragma extra_include

// The generated code does not explicitly qualify STL entities
namespace std {} using namespace std;

namespace ROOT {
   static TClass *musf_Dictionary();
   static void musf_TClassManip(TClass*);
   static void *new_musf(void *p = nullptr);
   static void *newArray_musf(Long_t size, void *p);
   static void delete_musf(void *p);
   static void deleteArray_musf(void *p);
   static void destruct_musf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::musf*)
   {
      ::musf *ptr = nullptr;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::musf));
      static ::ROOT::TGenericClassInfo 
         instance("musf", "basic_sel.h", 22,
                  typeid(::musf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &musf_Dictionary, isa_proxy, 4,
                  sizeof(::musf) );
      instance.SetNew(&new_musf);
      instance.SetNewArray(&newArray_musf);
      instance.SetDelete(&delete_musf);
      instance.SetDeleteArray(&deleteArray_musf);
      instance.SetDestructor(&destruct_musf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::musf*)
   {
      return GenerateInitInstanceLocal((::musf*)nullptr);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::musf*)nullptr); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *musf_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::musf*)nullptr)->GetClass();
      musf_TClassManip(theClass);
   return theClass;
   }

   static void musf_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *Getxsw_W_Dictionary();
   static void Getxsw_W_TClassManip(TClass*);
   static void *new_Getxsw_W(void *p = nullptr);
   static void *newArray_Getxsw_W(Long_t size, void *p);
   static void delete_Getxsw_W(void *p);
   static void deleteArray_Getxsw_W(void *p);
   static void destruct_Getxsw_W(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::Getxsw_W*)
   {
      ::Getxsw_W *ptr = nullptr;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::Getxsw_W));
      static ::ROOT::TGenericClassInfo 
         instance("Getxsw_W", "basic_sel.h", 44,
                  typeid(::Getxsw_W), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &Getxsw_W_Dictionary, isa_proxy, 4,
                  sizeof(::Getxsw_W) );
      instance.SetNew(&new_Getxsw_W);
      instance.SetNewArray(&newArray_Getxsw_W);
      instance.SetDelete(&delete_Getxsw_W);
      instance.SetDeleteArray(&deleteArray_Getxsw_W);
      instance.SetDestructor(&destruct_Getxsw_W);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::Getxsw_W*)
   {
      return GenerateInitInstanceLocal((::Getxsw_W*)nullptr);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::Getxsw_W*)nullptr); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *Getxsw_W_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::Getxsw_W*)nullptr)->GetClass();
      Getxsw_W_TClassManip(theClass);
   return theClass;
   }

   static void Getxsw_W_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *tauid_multicor_Dictionary();
   static void tauid_multicor_TClassManip(TClass*);
   static void *new_tauid_multicor(void *p = nullptr);
   static void *newArray_tauid_multicor(Long_t size, void *p);
   static void delete_tauid_multicor(void *p);
   static void deleteArray_tauid_multicor(void *p);
   static void destruct_tauid_multicor(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::tauid_multicor*)
   {
      ::tauid_multicor *ptr = nullptr;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::tauid_multicor));
      static ::ROOT::TGenericClassInfo 
         instance("tauid_multicor", "basic_sel.h", 56,
                  typeid(::tauid_multicor), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &tauid_multicor_Dictionary, isa_proxy, 4,
                  sizeof(::tauid_multicor) );
      instance.SetNew(&new_tauid_multicor);
      instance.SetNewArray(&newArray_tauid_multicor);
      instance.SetDelete(&delete_tauid_multicor);
      instance.SetDeleteArray(&deleteArray_tauid_multicor);
      instance.SetDestructor(&destruct_tauid_multicor);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::tauid_multicor*)
   {
      return GenerateInitInstanceLocal((::tauid_multicor*)nullptr);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::tauid_multicor*)nullptr); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *tauid_multicor_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::tauid_multicor*)nullptr)->GetClass();
      tauid_multicor_TClassManip(theClass);
   return theClass;
   }

   static void tauid_multicor_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *spe_cor_Dictionary();
   static void spe_cor_TClassManip(TClass*);
   static void *new_spe_cor(void *p = nullptr);
   static void *newArray_spe_cor(Long_t size, void *p);
   static void delete_spe_cor(void *p);
   static void deleteArray_spe_cor(void *p);
   static void destruct_spe_cor(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::spe_cor*)
   {
      ::spe_cor *ptr = nullptr;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::spe_cor));
      static ::ROOT::TGenericClassInfo 
         instance("spe_cor", "Correction.h", 20,
                  typeid(::spe_cor), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &spe_cor_Dictionary, isa_proxy, 0,
                  sizeof(::spe_cor) );
      instance.SetNew(&new_spe_cor);
      instance.SetNewArray(&newArray_spe_cor);
      instance.SetDelete(&delete_spe_cor);
      instance.SetDeleteArray(&deleteArray_spe_cor);
      instance.SetDestructor(&destruct_spe_cor);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::spe_cor*)
   {
      return GenerateInitInstanceLocal((::spe_cor*)nullptr);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::spe_cor*)nullptr); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *spe_cor_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::spe_cor*)nullptr)->GetClass();
      spe_cor_TClassManip(theClass);
   return theClass;
   }

   static void spe_cor_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *mutauFR_Dictionary();
   static void mutauFR_TClassManip(TClass*);
   static void *new_mutauFR(void *p = nullptr);
   static void *newArray_mutauFR(Long_t size, void *p);
   static void delete_mutauFR(void *p);
   static void deleteArray_mutauFR(void *p);
   static void destruct_mutauFR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::mutauFR*)
   {
      ::mutauFR *ptr = nullptr;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::mutauFR));
      static ::ROOT::TGenericClassInfo 
         instance("mutauFR", "ApplyFR.h", 20,
                  typeid(::mutauFR), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &mutauFR_Dictionary, isa_proxy, 4,
                  sizeof(::mutauFR) );
      instance.SetNew(&new_mutauFR);
      instance.SetNewArray(&newArray_mutauFR);
      instance.SetDelete(&delete_mutauFR);
      instance.SetDeleteArray(&deleteArray_mutauFR);
      instance.SetDestructor(&destruct_mutauFR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::mutauFR*)
   {
      return GenerateInitInstanceLocal((::mutauFR*)nullptr);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::mutauFR*)nullptr); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *mutauFR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::mutauFR*)nullptr)->GetClass();
      mutauFR_TClassManip(theClass);
   return theClass;
   }

   static void mutauFR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *tautauFR_Dictionary();
   static void tautauFR_TClassManip(TClass*);
   static void *new_tautauFR(void *p = nullptr);
   static void *newArray_tautauFR(Long_t size, void *p);
   static void delete_tautauFR(void *p);
   static void deleteArray_tautauFR(void *p);
   static void destruct_tautauFR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::tautauFR*)
   {
      ::tautauFR *ptr = nullptr;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::tautauFR));
      static ::ROOT::TGenericClassInfo 
         instance("tautauFR", "ApplyFR.h", 74,
                  typeid(::tautauFR), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &tautauFR_Dictionary, isa_proxy, 4,
                  sizeof(::tautauFR) );
      instance.SetNew(&new_tautauFR);
      instance.SetNewArray(&newArray_tautauFR);
      instance.SetDelete(&delete_tautauFR);
      instance.SetDeleteArray(&deleteArray_tautauFR);
      instance.SetDestructor(&destruct_tautauFR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::tautauFR*)
   {
      return GenerateInitInstanceLocal((::tautauFR*)nullptr);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::tautauFR*)nullptr); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *tautauFR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::tautauFR*)nullptr)->GetClass();
      tautauFR_TClassManip(theClass);
   return theClass;
   }

   static void tautauFR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_musf(void *p) {
      return  p ? new(p) ::musf : new ::musf;
   }
   static void *newArray_musf(Long_t nElements, void *p) {
      return p ? new(p) ::musf[nElements] : new ::musf[nElements];
   }
   // Wrapper around operator delete
   static void delete_musf(void *p) {
      delete ((::musf*)p);
   }
   static void deleteArray_musf(void *p) {
      delete [] ((::musf*)p);
   }
   static void destruct_musf(void *p) {
      typedef ::musf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::musf

namespace ROOT {
   // Wrappers around operator new
   static void *new_Getxsw_W(void *p) {
      return  p ? new(p) ::Getxsw_W : new ::Getxsw_W;
   }
   static void *newArray_Getxsw_W(Long_t nElements, void *p) {
      return p ? new(p) ::Getxsw_W[nElements] : new ::Getxsw_W[nElements];
   }
   // Wrapper around operator delete
   static void delete_Getxsw_W(void *p) {
      delete ((::Getxsw_W*)p);
   }
   static void deleteArray_Getxsw_W(void *p) {
      delete [] ((::Getxsw_W*)p);
   }
   static void destruct_Getxsw_W(void *p) {
      typedef ::Getxsw_W current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::Getxsw_W

namespace ROOT {
   // Wrappers around operator new
   static void *new_tauid_multicor(void *p) {
      return  p ? new(p) ::tauid_multicor : new ::tauid_multicor;
   }
   static void *newArray_tauid_multicor(Long_t nElements, void *p) {
      return p ? new(p) ::tauid_multicor[nElements] : new ::tauid_multicor[nElements];
   }
   // Wrapper around operator delete
   static void delete_tauid_multicor(void *p) {
      delete ((::tauid_multicor*)p);
   }
   static void deleteArray_tauid_multicor(void *p) {
      delete [] ((::tauid_multicor*)p);
   }
   static void destruct_tauid_multicor(void *p) {
      typedef ::tauid_multicor current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::tauid_multicor

namespace ROOT {
   // Wrappers around operator new
   static void *new_spe_cor(void *p) {
      return  p ? new(p) ::spe_cor : new ::spe_cor;
   }
   static void *newArray_spe_cor(Long_t nElements, void *p) {
      return p ? new(p) ::spe_cor[nElements] : new ::spe_cor[nElements];
   }
   // Wrapper around operator delete
   static void delete_spe_cor(void *p) {
      delete ((::spe_cor*)p);
   }
   static void deleteArray_spe_cor(void *p) {
      delete [] ((::spe_cor*)p);
   }
   static void destruct_spe_cor(void *p) {
      typedef ::spe_cor current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::spe_cor

namespace ROOT {
   // Wrappers around operator new
   static void *new_mutauFR(void *p) {
      return  p ? new(p) ::mutauFR : new ::mutauFR;
   }
   static void *newArray_mutauFR(Long_t nElements, void *p) {
      return p ? new(p) ::mutauFR[nElements] : new ::mutauFR[nElements];
   }
   // Wrapper around operator delete
   static void delete_mutauFR(void *p) {
      delete ((::mutauFR*)p);
   }
   static void deleteArray_mutauFR(void *p) {
      delete [] ((::mutauFR*)p);
   }
   static void destruct_mutauFR(void *p) {
      typedef ::mutauFR current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::mutauFR

namespace ROOT {
   // Wrappers around operator new
   static void *new_tautauFR(void *p) {
      return  p ? new(p) ::tautauFR : new ::tautauFR;
   }
   static void *newArray_tautauFR(Long_t nElements, void *p) {
      return p ? new(p) ::tautauFR[nElements] : new ::tautauFR[nElements];
   }
   // Wrapper around operator delete
   static void delete_tautauFR(void *p) {
      delete ((::tautauFR*)p);
   }
   static void deleteArray_tautauFR(void *p) {
      delete [] ((::tautauFR*)p);
   }
   static void destruct_tautauFR(void *p) {
      typedef ::tautauFR current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::tautauFR

namespace {
  void TriggerDictionaryInitialization_dict_RDFfunc_Impl() {
    static const char* headers[] = {
"basic_sel.h",
"GetPFtrk.h",
"Correction.h",
"ApplyFR.h",
"Sys.h",
nullptr
    };
    static const char* includePaths[] = {
"/cvmfs/sft.cern.ch/lcg/releases/ROOT/6.26.04-edd28/x86_64-centos7-gcc11-opt/include/",
"/afs/cern.ch/work/x/xuqin/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/lib/",
nullptr
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "dict_RDFfunc dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_AutoLoading_Map;
class __attribute__((annotate("$clingAutoload$basic_sel.h")))  musf;
class __attribute__((annotate("$clingAutoload$basic_sel.h")))  Getxsw_W;
class __attribute__((annotate("$clingAutoload$basic_sel.h")))  tauid_multicor;
class __attribute__((annotate("$clingAutoload$Correction.h")))  spe_cor;
class __attribute__((annotate("$clingAutoload$ApplyFR.h")))  mutauFR;
class __attribute__((annotate("$clingAutoload$ApplyFR.h")))  tautauFR;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "dict_RDFfunc dictionary payload"


#define _BACKWARD_BACKWARD_WARNING_H
// Inline headers
#include "basic_sel.h"
#include "GetPFtrk.h"
#include "Correction.h"
#include "ApplyFR.h"
#include "Sys.h"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[] = {
"Getxsw_W", payloadCode, "@",
"musf", payloadCode, "@",
"mutauFR", payloadCode, "@",
"spe_cor", payloadCode, "@",
"tauid_multicor", payloadCode, "@",
"tautauFR", payloadCode, "@",
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
