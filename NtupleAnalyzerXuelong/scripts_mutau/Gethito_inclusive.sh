#!/bin/bash
startMsg="Job started on "`date`
echo $startMsg

cd /afs/cern.ch/user/x/xuqin/work/taug-2/nanoAOD/CMSSW_12_4_2/src/MyNanoAnalyzer/NtupleAnalyzerXuelong_RDF
source setup.sh

cd /afs/cern.ch/user/x/xuqin/work/taug-2/nanoAOD/CMSSW_12_4_2/src/MyNanoAnalyzer/NtupleAnalyzerXuelong_RDF/scripts_mutau

#for v in mvis Acopl taupt mupt mtrans nTrk MET_pt taueta mueta
for v in mvis taupt
do 
    echo "python3 Inclusive_histo_mutau.py ${v}"
    python3 Inclusive_histo_mutau.py ${v}
    echo "python3 plotInclusive_mutau.py -y 2018 -c full -v ${v}"
    python3 plotInclusive_mutau.py -y 2018 -c full -v ${v}
done

