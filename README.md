# Securing SCADA networks for smart grids via adistributed evaluation of local sensor data

This repository is a proof of concept work to investigate the possibilities of the usage of local information to help raise the overall security in SCADA networks via a hieracichal, process-aware monitoring approach.

This repository is a combination of the three groups [Secure communication](https://zivgitlab.uni-muenster.de/ag-lammers/itsis-blackout/seccomm), [Attack](https://zivgitlab.uni-muenster.de/ag-lammers/itsis-blackout/gruppe-2-attack) and [Simualtion](https://zivgitlab.uni-muenster.de/ag-lammers/itsis-blackout/gruppe-1-simulation) which further developed the [distributed_ids_prototype](https://gitlab.utwente.nl/vmenzel/distributed_ids_prototype) by [Verena Menzel](https://gitlab.utwente.nl/vmenzel) during their Capstone project at the University of Münster. We thank Piet Björn Adick, Hassan Alamou, Rasim Gürkam Almaz, Lisa Angold, Ben Brooksnieder, Tom Deuschle, Kai Oliver Großhanten, Daniel Krug, Gelieza Kötterheinrich, Linus Lehbrink, Justus Pancke and Jan Speckamp for their work. 
See the original [README](https://gitlab.utwente.nl/vmenzel/distributed_ids_prototype) for details.


### Directory Overview
- **ids**: Implementation of networked IDS
  - **contrib**: collection of utility scripts
  - **deployment**: Configuration of `Docker`-based distributed deployment. (See [deployment/README](ids/deployment/README.md) for details)
  - **implementation**: Implementation of IDS System. (See [implementation/README](ids/implementation/README.md) for details)
  - **visualization**: Interactive Visualization of IDS. (See [visualization/README](ids/visualization/README.md) for details)
- **NOTICE**: Third Party libraries and their licenses
- **AUTHORS.txt**: Attributions
- **attack-tool** : The attack tool 

# License
Individual Licenses for the different parts can be found in the respective directories.
