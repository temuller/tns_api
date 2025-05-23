# tns_api
API to access Transient Name Server (TNS) data

[![repo](https://img.shields.io/badge/GitHub-temuller%2Ftns_api-blue.svg?style=flat)](https://github.com/temuller/tns_api)
[![license](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/temuller/tns_api/blob/master/LICENSE)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
[![PyPI](https://img.shields.io/pypi/v/tns_api?label=PyPI&logo=pypi&logoColor=white)](https://pypi.org/project/tns_api/)
[![DOI](https://zenodo.org/badge/660091525.svg)](https://zenodo.org/badge/latestdoi/660091525)

This code is largely based on the scripts already provided by TNS!

## Installation

It is recommended to install ``tns_api`` from pip:

```python
pip install tns_api
```
or it can be installed from source in the usual way.

## Usage Example

Below are some basic examples of what the user can do with this package.

### Environmental Variables

First of all, you will need to set a `.env` file in the current directory with the following variables:

```code
tns_id = 'YOUR_TNS_ID'
tns_bot_name = 'YOUR_BOT_NAME'
tns_api_key = 'YOUR_API_KEY'
```

where the values for these can be obtained by creating a [BOT](https://www.wis-tns.org/bots) (for mor information, check the [TNS Help page](https://www.wis-tns.org/content/tns-getting-started)).


### Retrieving Properties

All the properties of an object can be obtained with a single line:

```python
from tns_api.api import get_object
get_object('2004eo')
```
```python
{'objname': '2004eo',
 'name_prefix': 'SN',
 'objid': 2980,
 'object_type': {'name': 'SN Ia', 'id': 3},
 'redshift': None,
 'ra': '20:32:54.190',
 'dec': '+09:55:42.71',
 'radeg': 308.22579,
 'decdeg': 9.92853,
 'radeg_err': None,
 'decdeg_err': None,
 'hostname': 'NGC 6928        ',
 'host_redshift': None,
 'internal_names': None,
 'discoverer_internal_name': None,
 'discoverydate': '2004-09-17 00:00:00.000',
 'discoverer': None,
 'reporter': None,
 'reporterid': None,
 'source': 'bot',
 'discoverymag': 17.8,
 'discmagfilter': {'id': None, 'name': None, 'family': None},
 'reporting_group': {'groupid': None, 'group_name': None},
 'discovery_data_source': {'groupid': None, 'group_name': None},
 'public': 1,
 'end_prop_period': None}
```

An object name can be retrieved using its coordinates:

```python
from tns_api.api import search
api.search("6.37483128187 20.24293729")
```
```python
{'objname': '2024ryv', 'prefix': 'SN', 'objid': 159459}
```

### Retrieving Photometry and Spectra

The new version of TNS (v2) includes photometry and spectra for recent objects.

```python
from tns_api.api import get_photometry
get_photometry('2024ryv', parent_dir='.')
```
This downloads a CSV file with the available photometry.

```python
from tns_api.api import get_spectra
get_spectra('2024ryv', parent_dir='.', verbose=False)
```
This downloads a CSV file with the available spectroscopic information and also the ASCII files.

## Contributing

To contribute, either open an issue or send a pull request (prefered option). You can also contact me directly (check my profile: https://github.com/temuller).

## Citing TNS API

If you make use of this code, please cite it:

```code
@software{tomas_e_muller_bravo_2023_8181824,
  author       = {{M{\"u}ller-Bravo}, Tom{\'a}s E.},
  title        = {temuller/tns\_api: First Release (for zenodo)!},
  month        = jul,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {zenodo\_version},
  doi          = {10.5281/zenodo.8181824},
  url          = {https://doi.org/10.5281/zenodo.8181824}
}
```
Don't forget to acknowledge TNS!
