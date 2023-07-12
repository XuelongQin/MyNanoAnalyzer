#!/bin/bash
year=${1}
startMsg="Job started on "`date`
echo $startMsg

cd /afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong
source setup.sh

cd /afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/scripts_mutau

for v in mvis Acopl taupt mupt mtrans nTrk MET_pt taueta mueta
#for v in mvis
do 
    echo "python3 plotInclusive_mutau.py -y ${year} -c ${v} -v ${v}"
    python3 plotInclusive_mutau.py -y ${year} -c ${v} -v ${v}
done

