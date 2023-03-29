#!/bin/bash
startMsg="Job started on "`date`
echo $startMsg

year=${1}
sample=${2}
name=${3}
cd /afs/cern.ch/user/x/xuqin/work/taug-2/nanoAOD/CMSSW_12_4_2
eval `scram r -sh`

cd /afs/cern.ch/user/x/xuqin/work/taug-2/nanoAOD/CMSSW_12_4_2/src/MyNanoAnalyzer/NtupleAnalyzerXuelong_RDF/scripts_tautau

echo "python3 FinalSelection_tautau.py ${year} ${sample} ${name}"
python3 FinalSelection_tautau.py ${year} ${sample} ${name}

echo $startMsg
echo job finished on `date`