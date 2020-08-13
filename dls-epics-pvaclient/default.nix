{ epicsRepoBaseUrl, buildEpicsModule, dls-epics-pvdata, dls-epics-normativetypes
, dls-epics-pvaccess }:

buildEpicsModule rec {
  name = "dls-epics-pvaclient";
  buildInputs =
    [ dls-epics-pvdata dls-epics-normativetypes dls-epics-pvaccess ];
  preConfigure = ''
    sed -i 's/EPICS_//g' configure/RELEASE.local
  '';
  src = builtins.fetchGit {
    url = "${epicsRepoBaseUrl}/pvaclientcpp";
    ref = "dls-master";
  };
}
