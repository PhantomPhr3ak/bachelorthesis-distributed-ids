# Securing SCADA networks for smart grids via adistributed evaluation of local sensor data

This repository is a proof of concept work to investigate the possibilities of the usage of local information to help raise the overall security in SCADA networks via a hieracichal, process-aware monitoring approach.

This repository is a combination of the three groups [Secure communication](https://zivgitlab.uni-muenster.de/ag-lammers/itsis-blackout/seccomm), [Attack](https://zivgitlab.uni-muenster.de/ag-lammers/itsis-blackout/gruppe-2-attack) and [Simualtion](https://zivgitlab.uni-muenster.de/ag-lammers/itsis-blackout/gruppe-1-simulation) which further developed the [distributed_ids_prototype](https://gitlab.utwente.nl/vmenzel/distributed_ids_prototype) by [Verena Menzel](https://gitlab.utwente.nl/vmenzel) during their "Projektseminar" at the University of Münster. We thank Piet Björn Adick, Hassan Alamou, Rasim Gürkam Almaz, Lisa Angold, Ben Brooksnieder, Tom Deuschle, Kai Oliver Großhanten, Daniel Krug, Gelieza Kötterheinrich, Linus Lehbrink, Justus Pancke and Jan Speckamp for their work. 
See the original [README](https://gitlab.utwente.nl/vmenzel/distributed_ids_prototype) for details.


-------------------------------------------

taken from one of the readmes, will be updated later 
## Major changes
- Distributed communication, server (command & control) <-> client architecture
- Secure communication through the OPC-UA protocol
  - Authentication through certificates
  - SHA256 Encryption on all traffic
- Added web-based visualization of requirement violations
- Dynamic calculation of border regions during runtime

# Documentation

- Architectural/Conceptual work is documented in the [Gitlab Wiki](https://zivgitlab.uni-muenster.de/ag-lammers/itsis-blackout/seccomm/-/wikis/home)
- All code is documented inline.
- The individual parts each have a specific associated README.md. 

### Directory Overview
- **ids**: Implementation of networked IDS
  - **contrib**: collection of utility scripts
  - **deployment**: Configuration of `Docker`-based distributed deployment. (See [deployment/README](ids/deployment/README.md) for details)
  - **implementation**: Implementation of IDS System. (See [implementation/README](ids/implementation/README.md) for details)
  - **visualization**: Interactive Visualization of IDS. (See [visualization/README](ids/visualization/README.md) for details)
- **NOTICE**: Third Party libraries and their licenses
- **AUTHORS.txt**: Attributions

# License
Individual Licenses for the different parts can be found in the respective directories.