__version__ = "0.0.4"
from h2ogpuml.types import FUNCTION, STATUS, FunctionVector
from h2ogpuml.solvers.cpu import SolverCPU
from h2ogpuml.solvers.gpu import SolverGPU
from h2ogpuml.solvers.elastic_net_cpu import ElasticNetSolverCPU
from h2ogpuml.solvers.elastic_net_gpu import ElasticNetSolverGPU
#from h2ogpuml.solvers.kmeans_cpu import KMeansSolverCPU
#from h2ogpuml.solvers.kmeans_gpu import KMeansSolverGPU
from h2ogpuml.solvers.kmeans_base import KMeans
from h2ogpuml.solvers.kmeans_gpu import KMeansGPU2
