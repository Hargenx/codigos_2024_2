from prov.model import ProvDocument
import entradas, datetime
def desenho():
    ### BEGIN - Registering Retrospective Provenance -             #PROV-MODEL
    ### Experiment Randon Walk Experiment

    # Creating an empty provenance document
    d1 = ProvDocument()

    # Declaring namespaces for various prefixes used in the excution of Randon Walk Experiment
    d1.add_namespace("ufrj", "http://www.ufrj.br/ppgi/")
    d1.add_namespace("foaf", "http://xmlns.com/foaf/0.1/")
    d1.add_namespace("greco", "http://www.ufrj.br/ppgi/greco/#")

    # Adding an entity
    entity = "ufrj:" + entradas.entity
    e1 = d1.entity(entity)

    # Adding an Agent
    agent = "foaf:" + entradas.agent
    d1.agent(agent)

    # Attributing the execution of the experiment to the PROV-Agent
    d1.wasAttributedTo(e1, agent)

    # Adding an activity
    activity = "greco:" + entradas.activity
    d1.activity(activity)

    # Generation
    d1.wasGeneratedBy(entity, activity)

    # Adding a role to the PROV-Agent and timestamp to dataset
    d1.agent(
        agent,
        {
            "prov:hadRole": "Executor",
            "foaf:mbox": "sergioserra@gmail.com",
            "prov:attributedAtTime": str(datetime.datetime.utcnow()),
        },
    )
    d1.entity(entity, {"prov:generatedAtTime": str(datetime.datetime.utcnow())})

    ### END - Registering Retrospective Provenance

    ### Optional outputs ####

    # Generating the outup - a  Provenance Graph
    from prov.dot import prov_to_dot

    dot = prov_to_dot(d1)
    graph = graph + ".png"
    dot.write_png(graph)

    # Generating the Serialization - Output XML
    d1.serialize(entity + ".xml", format="xml")

    # Generating the Serialization - Output Turtle
    d1.serialize(entity + ".ttl", format="rdf", rdf_format="ttl")

    # Adding Vizualization the provenance graph in the Jupyter notebook
    from IPython.display import Image

    Image(graph)
