# Ravpy - The Provider's Library

Introducing Raven Protocol's Python SDK for Providers that allows compute nodes across the world to participate in the Ravenverse. 

## Working

In the Ravenverse, Providers are those who are willing to contribute their local system's idle compute power to execute the requester's computational requirements in return for rewards (Raven Tokens).

Ravpy is a python SDK that allows providers to intuitively participate in any ongoing graph computations in the Ravenverse. Ravpy nodes are authenticated based on their Ravenverse tokens which must be first generated by visiting the ```Ravenverse website```.

Ravpy connects to Ravsock (backbone server) from which it receives subgraphs (small groupings of Ravop operations) based on a benchmarking procedure. During this procedure, Ravpy client systems are rigorously tested on a variety of operations and the results are utilized by Ravsock for efficiently assigning complex subgraphs to the provider.  

## Installation

### With Pip

```bash
pip install ravpy
```

### From Source Code

#### Clone
```bash
git clone https://github.com/ravenprotocol/ravpy.git
```

#### Dependencies
```bash
cd ravpy/
python setup.py install
```

## Usage

### Setting Environment Variables
Create a .env file and add the following environment variables:

```bash
RAVENVERSE_URL=http://0.0.0.0:9999
RAVENVERSE_FTP_URL=0.0.0.0
```

Load environment variables at the beginning of your code using:

```python
from dotenv import load_dotenv
load_dotenv()
```

### Authentication

The Provider must connect to the Ravenverse using a unique token that they can generate by logging in on the Ravenverse Website using their MetaMask wallet credentials.   

```python
from ravpy.initialize import initialize

initialize(ravenverse_token = '<token>')
```

### Participate in Distributed Computing

```python
from ravpy.distributed.participate import participate

participate()
```

Upon participation, the Provider will be assigned a subgraph to execute. Once executed, the results will be sent to the Ravsock server.

![provider](https://user-images.githubusercontent.com/36446402/190107295-d1c0fb74-d894-4fea-b1d3-5354352d4f84.gif)

### Participate in Federated Analytics

```python
from ravpy.federated.participate import participate

participate(graph_id=3, file_path="<file_path>")
```

<!-- ## How to Contribute -->

## License

<a href="https://github.com/ravenprotocol/ravpy/blob/master/LICENSE"><img src="https://img.shields.io/github/license/ravenprotocol/ravpy"></a>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details