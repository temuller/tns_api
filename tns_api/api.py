import json
import requests
from pathlib import Path
from tns_api.utils import (set_headers, validate_response, 
                           dict_to_dataframe, TNS_API_KEY)


def search(object_info: dict | str) -> dict | None:
    """Looks for information of a given object or pair of coordinates.

    Parameters
    ----------
    object_info: Object's information.

    Returns
    -------
    object_data: Object's data.
    """
    url_tns_api = "https://www.wis-tns.org/api"
    search_url = url_tns_api + "/get/search"
    headers = set_headers()
    if isinstance(object_info, str):
        # str to dict
        split_info = object_info.split()
        if len(split_info) == 2:
            # assume coordinates
            object_info = {"ra": split_info[0], 
                           "dec": split_info[1]
                           }  
        elif object_info.startswith("19") or object_info.startswith("20"):
            object_info = {"objname": object_info}
    search_data = {'api_key': TNS_API_KEY, 'data': object_info}
    response = requests.post(search_url, headers=headers, data=search_data)
    object_data = validate_response(response)
    return object_data

def get_spectra(iau_name: str, parent_dir: str=None) -> None:
    obj_info = {"objname": iau_name,
                "spectra": "1"
                }
    spec_data = search(obj_info)["spectra"]
    spec_df = dict_to_dataframe(spec_data)
    # save spec info
    outfile = Path(parent_dir, iau_name, "spectra.csv")
    spec_df.to_csv(outfile, index=False)
    # download files
    outdir = Path(parent_dir, iau_name, "spectra")
    for file_url in spec_df.asciifile.values:
        download_file(file_url, outdir)
    
def download_file(file_url, outdir):
    file_url = Path(file_url)
    headers = set_headers()
    api_data = {'api_key': TNS_API_KEY}
    response = requests.post(str(file_url), headers=headers, data=api_data, stream=True)    
    if response.status_code == 200:
        outfile = Path(outdir) + file_url.name
        with open(outfile, 'wb') as file:
            for chunk in response:
                file.write(chunk)
        print ("File was successfully downloaded.\n")
    else:
        print ("File was not downloaded.\n")

def get_response(url: str, iau_name: str) -> requests.Response | None:
    """Obtains the response from a given TNS URL.

    Parameters
    ----------
    url: TNS URL.

    Returns
    -------
    response: Response object.
    """
    headers = set_headers()
    sn_info = {"objname": iau_name}
    json_data = [('api_key', (None, TNS_API_KEY)),
                            ('data', (None, json.dumps(sn_info)))]
    response = requests.post(url, headers=headers, files=json_data)
    return response
    
def get_object(iau_name: str) -> dict | None:
    """Obtains the objects information.

    Parameters
    ----------
    iau_name: IAU name of the object (e.g. 2020xne).

    Returns
    -------
    object_data: Object's data.
    """
    # look for the target ID in the search webpage
    tns_url = "https://www.wis-tns.org/api/get/object"
    response = get_response(tns_url, iau_name)
    object_data = validate_response(response)
    return object_data
