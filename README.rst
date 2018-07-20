Annotationz Module Repository
========================

This project is intendet to annotate data according to the ALKIS Ontology.

Additionally it is desired for the tool to be generic.


Getting Started
---------------
Given that 'ontology.owl' and 'data.xml' directories are known::

	a = Annotation()
	a.importOntology("ontology.owl", "ontologyPrefix")
	a.importData("data.xml")

	elements = a.getElementsByTagName("elementName", "parentName")
	for element in elements:
		a.annotate(element)

	a.output()