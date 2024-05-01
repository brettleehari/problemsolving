from diagrams import Cluster, Diagram
from diagrams.onprem.ci import Jenkins
from diagrams.programming.language import Java, Javascript, Python
with Diagram("Virtuora CI", show=False):




    with Cluster("Language"):
        master = Jenkins("master")
        master - [Java("Language1"), Javascript("Language2"), Python("Language3")]
